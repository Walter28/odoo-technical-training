#python imports goes here
from datetime import  timedelta

# odoo import goes here
from odoo import  fields, models, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = """
        This model describe the table that will store our different offers
    """
    _sql_constraints = [
        ("check_offer_price", "CHECK(price > 0)", "An offer price must be positive"),
        ("check_validity", "CHECK(validity > 0)", "Validity can not be a negative value")
    ]
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        [
            ('accepted', "Accepted"),
            ('refused', "Refused"),
        ],
        string = "Status",
        copy = False,
    )
    res_partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    partner_email = fields.Char(string="Buyer Email", related='res_partner_id.email')
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(string="Validity", default=7)
    # We put this into string to avoid error, in python we always define function first den declaration
    # U cant change the deadline, in order to do it, we add an *inverse* attribute
    # with this attribute if u change the deadline date, it will update the validity field
    # we do not do this with *compute* attribute, coz it will create a Infinite Loop
    deadline = fields.Date("Deadline", compute='_compute_deadline', inverse='_inverse_deadline')

    # Note : related & computed fields are both readonly, means they are non-storable
    # if u need to search theme, store them first, to do this, add *store* attribute as follows
    type_id = fields.Many2one(related="property_id.property_type_id", store=True)

    @api.depends("validity", "create_date")
    def _compute_deadline(self):
        for rec in self:
            # coz validity was int type, we cant compute this with a Date type
            # that why we use timedelta from date time to add days on our date type here
            if rec.create_date and rec.validity:
                rec.deadline = rec.create_date + timedelta(days=rec.validity)
            else:
                rec.deadline = fields.Date.today() + timedelta(days=rec.validity)

    # no need to use decorators here, coz this does not depend to any field
    # output will be visible only when u SAVE CHANGES
    # as well even *compute* field does that on the fly
    def _inverse_deadline(self):
        for rec in self:
            # convert this to days, never mind the output is. (it's the date, full date)
            rec.validity = (rec.deadline - rec.create_date.date()).days

    def action_accept(self):
        self.ensure_one()
        if "accepted" in self.property_id.offer_ids.mapped('status'):
            raise  UserError(
                _("This property already have an offer accepted")
            )
        if not self.property_id.res_partner_id:
            raise UserError(
                _("Please set up the Buyer first before u accepting the offer")
            )
        self.status = "accepted"
        self.property_id.state = "accepted"
        self.property_id.selling_price = self.price

    def action_refuse(self):
        self.status = "refused"


    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            if not rec.get('create_date'):
                rec['create_date'] = fields.Datetime.now()
        return super(EstatePropertyOffer, self).create(vals)

    @api.constrains('validity')
    def _check_validity(self):
        for rec in self:
            if rec.deadline <= rec.create_date.date():
                raise ValidationError(
                    _("Deadline cannot be before creation date")
                )

    @api.constrains('price')
    def _check_price(self):
        for rec in self:
            current_property_offers_rec = self.env['estate.property.offer'].search([('property_id', '=', rec.property_id.id)])
            #delete the actual record created bfr constraint verification
            current_property_offers_rec_filtered = current_property_offers_rec.filtered(lambda  r : r.id != rec.id)
            if current_property_offers_rec_filtered:
                if rec.price < min(current_property_offers_rec_filtered.mapped('price')):
                    raise ValidationError(
                        _("Your offer is cheap than existing ones")
                    )

    @api.model_create_multi
    def create(self, vals_dic):
        res = super().create(vals_dic)
        for vals in vals_dic:
            property = self.env['estate.property'].browse(vals.get('property_id'))
            property.write(
                {
                    'state': 'received'
                }
            )
            print(f"++++++++ Property of offer : {property} ")
        # if self.env
        return res

    def write(self, vals):
        print(vals)
        res_partner_ids = self.env['res.partner'].search(
            [
                ('is_company', '=', True),
            ],
            limit=5, order='name desc'
        )
        print(res_partner_ids)
        return  super(EstatePropertyOffer, self).write(vals)

    # SERVER ACTION
    def extend_offer_deadline(self):
        active_ids = self._context.get('active_ids', [])
        if active_ids:
            offer_ids = self.env['estate.property.offer'].browse(active_ids)
            for offer in offer_ids:
                offer.validity += 1

    # Scheduled action
    def _extend_offer_deadline(self):
        # this means to search all
        offer_ids = self.env['estate.property.offer'].search([])
        # every day increase offers validity with one digit
        for offer in offer_ids:
            offer.validity += 1

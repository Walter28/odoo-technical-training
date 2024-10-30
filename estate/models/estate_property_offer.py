#python imports goes here
from datetime import  timedelta

# odoo import goes here
from odoo import  fields, models, api, _
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = """
        This model describe the table that will store our different offers
    """
    _sql_constraints = [
        ("check_offer_price", "CHECK(price > 0)", "An offer price must be positive")
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
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer("Validity")
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
                rec.deadline = False

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
        self.property_id.selling_price = self.price

    def action_refuse(self):
        self.status = "refused"

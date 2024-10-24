#python import
from email.policy import default
from dateutil.relativedelta import relativedelta

#odoo import
from odoo import models, fields, api, _
from odoo.http import  request
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

from odoo.odoo.tools.populate import compute


# Utility functions outside the class
# this function return the day in 3 months starting to now
def date_in_three_months():
    return fields.Date.today() + relativedelta(months=3)

# this function fetch the actual user logged in
def get_current_user():
    # check if there is any connected into the actual session
    if request.session.uid:
        # get the current logged-in user using the session id
        user = request.env['res.users'].browse(request.session.uid)
        return user


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This model is for your real estate company"
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)", "Expected price must be strictly positive!!!"),
        ("check_selling_price", "CHECK(selling_price >= 0)", "Selling price must be a least positive!!!"),
    ]
    _order = "id desc"
    
    name = fields.Char(string="Name", required=True, default="House x")
    # this field is useless to get displayed in form view
    active = fields.Boolean(default=True, invisible=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("received", "Offer Received"),
            ("accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required = True,
        # if you duplicated any record this field will not be duplicated
        copy = False,
        default = "new"

    )
    description = fields.Text(string="Description")
    post_code = fields.Char(string="Postal")

    # We will call a custom function in order to get the date in 3 months from today for the default value
    date_availability = fields.Date(string="Available from", default=lambda self: date_in_three_months(), copy=False)
    expected_price = fields.Float(required=True, string="Expected price")
    best_offer = fields.Float(compute='_compute_best_offer')
    selling_price = fields.Float(string="Selling price", copy=False, readonly=True)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden area", default=False)
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ],
        string="Garden Orientation",
        default="north"
    )

    # relational property fields
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    # this is the buyer id
    res_partner_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    # this is the sales id : (Default) the current logged-in user
    res_users_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    # *property_id* => this is an inverse field, is he IF of the property offer
    # ie c'est dans l'offre quon aura le property_id, une offre ne peut avoir une et une seule propriete
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    has_accepted_offer = fields.Boolean(compute="_compute_accepted_offer")
    has_offers = fields.Boolean(compute="_compute_has_offers")
    # update_state = fiel
    property_tag_ids = fields.Many2many("estate.property.tag", string="Property tag")

    # For some of our widget, these fields are mendatory
    currency_id = fields.Integer()
    color = fields.Integer()

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    # computed fields
    total_area = fields.Integer(string="Total Area", compute=_compute_total_area)

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for property in self:
            property.best_offer = max(property.offer_ids.mapped('price')) if property.offer_ids else 0

    @api.onchange("garden")
    def _compute_garden(self):
        # self in an onchange context will always contain only one record at a time (the one currently being edited)
        # no need using for loop
        if not property.garden:
            property.garden_area = 0
            property.garden_orientation = False

    @api.onchange("date_availability")
    def _onchange_date_availability(self):
        for property in self:
            print(f"++++++++++++++++++++++++++++++++++++ Date today : {fields.Date.today()}")
            print(f"++++++++++++++++++++++++++++++++++++ Date Availability : {property.date_availability}")
            if property.date_availability < fields.Date.today():
                return {
                    "warning": {
                        "title": _("Warning"), # _(" ") this : bcz we wanna make the text translatable
                        "message": _("The Availability date must be today or in the feature")
                    }
                }

    @api.depends('offer_ids.status')
    def _compute_accepted_offer(self):
        for property in self:
            # Check if there is at least one offer with status 'accepted'
            property.has_accepted_offer = any(
                offer.status == 'accepted' for offer in property.offer_ids
            )
            if property.has_accepted_offer:
                property.state = 'accepted'

    @api.depends('offer_ids')
    def _compute_has_offers(self):
        """Compute if there are any offers."""
        for property in self:
            property.has_offers = bool(property.offer_ids)
            if property.has_offers and property.state not in ['accepted', 'sold', 'canceled']:
                property.state = 'received'

    def action_sell(self):
        if self.state == 'canceled':
            raise  UserError(
                _("Canceled Property can never be sold")
            )
        elif self.state == 'sold':
            raise UserError(
                _("This Property is already taken")
            )
        self.state = 'sold'

    def action_decline(self):
        if self.state == 'sold':
            raise  UserError(
                _("Sold Property can never be canceled")
            )
        elif self.state == 'canceled':
            raise UserError(
                _("The offer is already canceled, u can't do it twice")
            )
        self.state = 'canceled'

    @api.constrains('selling_price', 'expected_price')
    def _check_constraint(self):
        for estate in self:
            if 0 < estate.selling_price < (estate.expected_price * 0.9):
                raise ValidationError(
                    _("Your selling price is tooo lower, it must be upto 90% superior of your expected price ")
                )
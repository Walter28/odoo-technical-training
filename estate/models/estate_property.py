
#python import
from email.policy import default
from dateutil.relativedelta import relativedelta

#odoo import
from odoo import models, fields


def _date_in_three_months():
    return fields.Date.today() + relativedelta(months=3)


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This model is for your real estate company"
    
    name = fields.Char(string="Name", required=True, default="House")
    # this info is useless to get displayed in form view
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
    post_code = fields.Char(string="Postalcode")

    # We will call a custom function in order to get the date in 3 months from today for the default value
    date_availability = fields.Date(string="Available from", default=_date_in_three_months, copy=False)
    expected_price = fields.Float(required=True, string="Expected price", readonly=True)
    selling_price = fields.Float(string="Selling price", copy=False)
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

from email.policy import default

from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This model is for your real estate company"
    
    name = fields.Char(string="Name", required=True, default="House")
    description = fields.Text(string="Description")
    post_code = fields.Char(string="Postalcode")
    date_availability = fields.Date(string="Available from")
    expected_price = fields.Float(required=True, string="Expected price")
    selling_price = fields.Float(string="Selling price")
    bedrooms = fields.Integer(string="Bed rooms")
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
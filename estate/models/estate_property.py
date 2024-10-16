from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This model is for your real estate company"
    
    name = fields.Char(string="Name", required=True, default="House")
    description = fields.Text(string="Description")
    post_code = fields.Char(string="Postal code")
    date_availability = fields.Date(string="Date availability")
    excepted_price = fields.Float(required=True, string="Expected price")
    selling_price = fields.Float(string="Selling price")
    bedrooms = fields.Integer(string="Bed rooms")
    living_area = fields.Integer(string="Living area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden area")
    garden_orientation = fields.Selection(
        [
            ('option1', 'North'),
            ('option2', 'South'),
            ('option3', 'East'),
            ('option4', 'west')
        ],
        string="Garden Orientation"
    )
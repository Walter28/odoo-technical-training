#python imports goes here
from email.policy import default

# odoo import goes here
from odoo import  fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = """
        This model describe the table that will store our properties type
    """
    _order = "name, sequence desc"

    sequence = fields.Integer(default=1)
    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")

#python imports goes here

# odoo import goes here
from odoo import  fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = """
        This model describe the table that will store our properties type
    """

    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")

#python imports goes here

# odoo import goes here
from odoo import  fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = """
        This model link help us to link properties with tags.
        Note that many *properties* can be linked to many *tags*
        That why is model will be in Many2many relationship with estate.property
        Odoo will create a new in between table in the db
    """
    _sql_constraints = [
        ("unique_tag_name", "UNIQUE(name)", "Tag name should be unique !!!")
    ]

    name = fields.Char(string="Name", required=True)

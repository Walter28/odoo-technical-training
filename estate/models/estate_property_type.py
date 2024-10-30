#python imports goes here
from email.policy import default

# odoo import goes here
from odoo import  fields, models, api, _


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = """
        This model describe the table that will store our properties type
    """
    _order = "name, sequence desc"

    sequence = fields.Integer(default=1)
    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")
    property_count = fields.Integer(string="Property Count", compute="_compute_property_count")

    @api.depends("property_ids")
    def _compute_property_count(self):
        for property in self:
            property.property_count = len(property.property_ids)

    def action_open_property_ids(self):
        return  {
            "name" : _("Related Properties"),
            "type" : "ir.actions.act_window",
            "view_mode" : "tree,form",
            "res_model" : "estate.property",
            "target" : "current",
            "domain" : [("property_type_id", "=", self.id)],
            "context" : {
                "default_property_type_id" : self.id
            }
        }

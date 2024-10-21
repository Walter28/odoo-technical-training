#python imports goes here

# odoo import goes here
from odoo import  fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = """
        This model describe the table that will store our different offers
    """

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
    property_id = fields.Many2one("estate.property", string="Property", required=1)
    validity = fields.Integer("Validity")
    deadline = fields.Date("Deadline")
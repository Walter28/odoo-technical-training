#python imports goes here

#odoo imports goes here
from odoo import  fields, models, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many("estate.property", "res_users_id", domain=[('state', 'in', ('new', 'received'))])
from odoo import models, fields, api, _


class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'res_users_id', string='Properties')
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
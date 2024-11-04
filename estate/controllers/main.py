from odoo import http
from odoo.http import request


class PropertyController(http.Controller):

    @http.route(['/properties'], type='http', website=True, auth='public')
    def show_properties(self):
        ## this will not work bcz u need to auth this endpoint
        # property_ids = request.env['estate.property'].search([])
        ## use this instead, with a sudo, to use SU role
        property_ids = request.env['estate.property'].sudo().search([])
        print("Properties : ", property_ids)
        return  request.render('estate.property_list', {'property_ids': property_ids})

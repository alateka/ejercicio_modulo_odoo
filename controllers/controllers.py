# -*- coding: utf-8 -*-
# from odoo import http


# class ApfSge(http.Controller):
#     @http.route('/apf_sge/apf_sge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apf_sge/apf_sge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('apf_sge.listing', {
#             'root': '/apf_sge/apf_sge',
#             'objects': http.request.env['apf_sge.apf_sge'].search([]),
#         })

#     @http.route('/apf_sge/apf_sge/objects/<model("apf_sge.apf_sge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apf_sge.object', {
#             'object': obj
#         })

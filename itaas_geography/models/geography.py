# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
#from openerp import api, fields, models, _


class itaas_geography(models.Model):
    _name = "itaas.geography"
    _inherit = ['mail.thread']
    _description = "Geography"
    _order = 'code, name'

    name = fields.Char(string='Name', required=True, copy=False, index=True, track_visibility='onchange')
    code = fields.Char(string='Code', required=True, copy=False, index=True, track_visibility='onchange')
    active = fields.Boolean('Active', default=True)


class res_country_state(models.Model):
    _inherit = "res.country.state"

    geo_id = fields.Many2one('itaas.geography', string='Geography', copy=False, index=True, track_visibility='onchange' )
    active = fields.Boolean('Active', default=True)



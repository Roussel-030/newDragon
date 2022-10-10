# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Description module professor'

    nif = fields.Char(string='NIF')
    stat = fields.Char(string='STAT')
    rcs = fields.Char(string='RCS')




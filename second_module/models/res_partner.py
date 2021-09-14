from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')



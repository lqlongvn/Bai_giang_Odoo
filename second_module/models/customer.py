from odoo import fields, models, api


class Customer(models.Model):
    _inherit = 'customerfirst'

    description = fields.Text(string='Description')
    phone = fields.Char(string='Phone number', required=1)

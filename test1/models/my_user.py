from odoo import fields, models, api

class MyUser(models.Model):
    # _name = 'myuser'
    _inherit = 'res.users'

    chucvu = fields.Char(string='Chức vụ')

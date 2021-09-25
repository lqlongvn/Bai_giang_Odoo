from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')

    limit_credit = fields.Float(string= 'Nhập vào một giá trị bất kỳ')

    def action_confirm(self):
        res = super(ResPartner, self).action_confirm()
        if self. amount_total >= self.limit_credit:
            pass



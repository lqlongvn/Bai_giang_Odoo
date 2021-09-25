from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_cancel(self):
        # Nếu user admin hoặc có quyền admin thì thực hiện:
        super(SaleOrder, self).action_cancel()


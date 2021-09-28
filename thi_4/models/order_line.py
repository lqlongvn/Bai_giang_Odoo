from odoo import fields, models, api

# order_line (order_id, product_id, created_date, qty, amount, sub_total=qty * amount)

class OrderLine(models.Model):
    _name = 'orderline4'

    name = fields.Char(string='Tên order_line')
    created_date = fields.Date(string='Ngày đơn hàng')
    qty = fields.Integer(string='Số lượng')
    unit_price = fields.Integer(string='Đơn giá')

    order4_id = fields.Many2one(comodel_name='order4', string='Order')
    product4_id = fields.Many2one(comodel_name='product4', string='Product')
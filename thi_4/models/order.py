from odoo import fields, models, api

# model order (customer_id, order_date, total_amount=sum(line.sub_total), order_ids)

class Order(models.Model):
    _name = 'order4'

    name = fields.Char(string='Tên đơn hàng')
    order_date = fields.Date(string='Ngày đơn hàng')

    customer_id = fields.Many2one(comodel_name='customer4', string='Customers')
    orderline_ids = fields.One2many(comodel_name='orderline4', inverse_name='order4_id', string='Order Lines')
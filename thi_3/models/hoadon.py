from odoo import fields, models, api

# hoadon (name, ngay, tongtien (tính từ tổng tiền hóa đơn chi tiết))

class HoaDon(models.Model):
    _name = 'hoadon'

    name = fields.Char(string='Tên Hóa đơn')
    ngay = fields.Char(string='Ngày hóa đơn')
    tongtien = fields.Integer(string='Tổng tiền')
    hoadonchitiet_ids = fields.One2many(comodel_name='hoadonchitiet', inverse_name='hoadon_id', string='Hóa đơn chi tiết')

    # order_ids = fields.One2many(comodel_name='order4', inverse_name='customer_id', string='Orders')



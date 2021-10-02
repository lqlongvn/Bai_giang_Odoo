from odoo import fields, models, api

# hoadon (name, ngay, tongtien)

class HoaDon(models.Model):
    _name = 'hoadon'

    name = fields.Char(string='Tên Hóa đơn')
    ngay = fields.Char(string='Ngày hóa đơn')
    tongtien = fields.Integer(string='Tổng tiền')


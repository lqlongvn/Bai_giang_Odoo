from odoo import fields, models, api

# hoadon (name, soluong, dongia (lấy từ giá sản phẩm), tổng tiền=số lượng * đơn giá)

class HoaDonChiTiet(models.Model):
    _name = 'hoadonchitiet'

    name = fields.Char(string='Tên Hóa đơn')
    soluong = fields.Integer(string='Số lượng')
    dongia = fields.Integer(string='Đơn giá')
    # tongtien = fields.Integer(string='Tổng tiền')

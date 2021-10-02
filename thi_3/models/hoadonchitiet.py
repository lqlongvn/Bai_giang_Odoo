from odoo import fields, models, api

# hoadon (name, soluong, dongia (lấy từ giá sản phẩm), tổng tiền=số lượng * đơn giá)

class HoaDonChiTiet(models.Model):
    _name = 'hoadonchitiet'

    name = fields.Char(string='Tên Hóa đơn')
    soluong = fields.Integer(string='Số lượng')
    dongia = fields.Integer(string='Đơn giá')
    thanhtien = fields.Integer(string='Thành tiền', compute='total_money')

    hoadon_id = fields.Many2one(comodel_name='hoadon', string='Hóa đơn tổng')
    sp_id = fields.Many2one(comodel_name='sản phẩm', string='Sản phẩm có Hóa đơn chi tiết')


    @api.depends('soluong', 'dongia')
    def total_money(self):
        for hd_chitiet in self:
            hd_chitiet.thanhtien = hd_chitiet.soluong * hd_chitiet.dongia



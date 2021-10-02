from odoo import fields, models, api

# sanpham (name, gia_sanpham, mota)

class SanPham(models.Model):
    _name = 'sanpham'

    name = fields.Char(string='Tên sản phẩm')
    gia_sanpham = fields.Integer(string='Giá sản phẩm')
    mota = fields.Char(string='Mô tả')

    hoadonchitietsp_ids = fields.One2many(comodel_name='hoadonchitiet', inverse_name='sp_id',
                                        string='Hóa đơn chi tiết của Sản phẩm')



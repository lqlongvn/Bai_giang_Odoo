from odoo import fields, models, api

# sanpham (id, name, phone, address, gender - gan gender mac dinh la male)

class SanPham(models.Model):
    _name = 'sanpham'

    name = fields.Char(string='Tên sản phẩm')
    gia_sanpham = fields.Char(string='Giá sản phẩm')
    mota = fields.Char(string='Mô tả')


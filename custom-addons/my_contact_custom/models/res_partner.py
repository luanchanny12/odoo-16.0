# tên file của models và views phải trùng với model muốn sửa

# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    # --- PHÉP THUẬT KẾ THỪA ---
    # Thay vì '_name', chúng ta dùng '_inherit'
    # Báo Odoo: "Tôi không tạo model mới, tôi muốn
    #           thêm trường vào model 'res.partner' đã có."
    _inherit = 'res.partner'

    # --- TRƯỜNG MỚI BẠN MUỐN THÊM ---
    # Odoo sẽ tự động thêm cột 'customer_level' này
    # vào bảng 'res_partner' trong CSDL.
    customer_level = fields.Selection(
        [
            ('bronze', 'Đồng'),
            ('silver', 'Bạc'),
            ('gold', 'Vàng'),
        ],
        string='Cấp độ Khách hàng',
        default='bronze'
    )
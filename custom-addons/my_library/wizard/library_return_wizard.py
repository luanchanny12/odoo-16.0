# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryReturnWizard(models.TransientModel):
    _name = 'library.return.wizard'
    _description = 'Wizard Trả sách nhanh'

    # 1. Trường chọn nhiều (Many2many)
    # Để người dùng tích chọn các phiếu đang mượn
    borrow_ids = fields.Many2many(
        comodel_name='library.borrow',
        string='Chọn phiếu cần trả',
        # Domain: Chỉ hiện những phiếu đang có trạng thái là 'borrowed' (Đang mượn)
        domain=[('state', '=', 'borrowed')]
    )

    # 2. Hàm xử lý khi bấm nút "Trả sách"
    def action_return_books(self):
        for wizard in self:
            # Duyệt qua từng phiếu mượn được chọn
            for borrow in wizard.borrow_ids:
                # Gọi lại hàm 'action_return' cũ mà ta đã viết ở Bài 4
                # (Hàm này đã bao gồm cả logic cộng kho, đổi trạng thái...)
                borrow.action_return()
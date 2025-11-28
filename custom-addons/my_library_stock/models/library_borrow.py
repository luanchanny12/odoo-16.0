# -*- coding: utf-8 -*-
from odoo import models, api


class LibraryBorrow(models.Model):
    # Kế thừa model Phiếu mượn (của module cũ)
    _inherit = 'library.borrow'

    # --- 1. GHI ĐÈ NÚT "MƯỢN" ---
    def action_borrow(self):
        # Bước A: Gọi hàm gốc (để nó đổi state sang 'borrowed' như bình thường)
        res = super(LibraryBorrow, self).action_borrow()

        # Bước B: Code thêm - Tự động tạo phiếu XUẤT KHO (-1)
        # self.env['...'].create(...) là lệnh tạo bản ghi mới
        self.env['library.stock.move'].create({
            'name': 'Xuất kho (Mượn): ' + self.borrower_id.name,  # Tên phiếu
            'book_id': self.book_id.id,  # Lấy ID sách đang mượn
            'qty': -1,  # Trừ 1 cuốn
            'state': 'done',  # Đánh dấu xong luôn để trừ kho ngay
            'date': self.borrow_date,  # Lấy ngày mượn
        })

        return res

    # --- 2. GHI ĐÈ NÚT "TRẢ" ---
    def action_return(self):
        # Bước A: Gọi hàm gốc (đổi state sang 'returned')
        res = super(LibraryBorrow, self).action_return()

        # Bước B: Code thêm - Tự động tạo phiếu NHẬP KHO (+1)
        self.env['library.stock.move'].create({
            'name': 'Nhập kho (Trả): ' + self.borrower_id.name,
            'book_id': self.book_id.id,
            'qty': 1,  # Cộng 1 cuốn
            'state': 'done',  # Xong luôn
            'date': self.return_date,  # Lấy ngày trả
        })

        return res
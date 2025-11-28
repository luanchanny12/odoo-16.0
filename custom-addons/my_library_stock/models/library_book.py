# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryBook(models.Model):
    _inherit = 'library.book'

    # 1. Liên kết ngược để xem lịch sử kho của sách này
    stock_move_ids = fields.One2many(
        comodel_name='library.stock.move',
        inverse_name='book_id',
        string='Lịch sử Kho'
    )

    # 2. Trường tính toán Tồn kho
    qty_available = fields.Integer(
        string='Tồn kho',
        compute='_compute_qty_available',
        store=True # Lưu lại để tìm kiếm được
    )

    # 3. Hàm tính toán
    @api.depends('stock_move_ids', 'stock_move_ids.state', 'stock_move_ids.qty')
    def _compute_qty_available(self):
        for book in self:
            total = 0
            for move in book.stock_move_ids:
                # Chỉ cộng dồn các phiếu đã "Hoàn thành" (done)
                if move.state == 'done':
                    total += move.qty
            book.qty_available = total
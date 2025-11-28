# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError


class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Library borrow'

    # BỎ _rec_name = 'book_id' đi, vì chúng ta sẽ dùng trường 'name' làm mặc định
    # Odoo tự động dùng trường có tên là 'name' làm _rec_name nếu không chỉ định khác.

    # --- TRƯỜNG TÊN HIỂN THỊ (COMPUTED) ---
    # Đặt tên là 'name' để Odoo tự nhận làm tên bản ghi
    name = fields.Char(
        string='Tên hiển thị',
        compute='_compute_name',
        store=True,  # Lưu vào DB để tìm kiếm và hiển thị nhanh hơn
        readonly=True
    )

    # --- CÁC TRƯỜNG LIÊN KẾT ---
    borrower_id = fields.Many2one(
        comodel_name='res.partner',
        string='Người mượn',
        required=True,
    )

    book_id = fields.Many2one(
        comodel_name='library.book',
        string='Sách',
        required=True,
    )

    borrower_address = fields.Char(
        string='Địa chỉ liên hệ',
        related='borrower_id.contact_address',
        readonly=True,
        store=True,
    )

    # --- CÁC TRƯỜNG KHÁC ---
    borrow_date = fields.Date(string='Ngày mượn', default=fields.Date.today)
    return_date = fields.Date(string='Ngày trả')

    state = fields.Selection([
        ('draft', 'Nháp'),
        ('borrowed', 'Đã mượn'),
        ('returned', 'Đã trả'),
        ('lost', 'Báo mất')
    ], string='Trạng thái', default='draft', required=True)

    is_overdue = fields.Boolean(string='Đã quá hạn', default=False, readonly=True)

    # --- HÀM TÍNH TOÁN TÊN ---
    # Luôn đảm bảo gán giá trị cho rec.name
    @api.depends('book_id', 'book_id.name', 'borrower_id', 'borrower_id.name')
    def _compute_name(self):
        for rec in self:
            # Lấy tên sách và người mượn, nếu không có thì để trống
            book_name = rec.book_id.name or 'Chưa chọn sách'
            borrower_name = rec.borrower_id.name or 'Chưa chọn người'

            # Gán giá trị (BẮT BUỘC PHẢI CÓ DÒNG NÀY)
            rec.name = f"[{book_name}] - {borrower_name}"

    # --- CÁC HÀM KHÁC (Giữ nguyên) ---
    def action_borrow(self):
        self.write({'state': 'borrowed'})

    def action_return(self):
        self.write({
            'state': 'returned',
            'return_date': date.today(),
            'is_overdue': False
        })

    def action_lost(self):
        self.write({'state': 'lost'})

    def action_reset_to_draft(self):
        self.write({
            'state': 'draft',
            'is_overdue': False
        })

    # --- LOGIC CRON JOB ---
    @api.model
    def check_overdue_books(self):
        today = fields.Date.today()
        overdue_records = self.search([
            ('state', '=', 'borrowed'),
            ('return_date', '<', today)
        ])
        if overdue_records:
            overdue_records.write({'is_overdue': True})

    # --- RÀNG BUỘC ---
    @api.constrains('borrow_date', 'return_date')
    def _check_return_date(self):
        for borrow in self:
            if borrow.return_date and borrow.return_date < borrow.borrow_date:
                raise ValidationError("Ngày trả sách không thể nhỏ hơn ngày mượn sách!")
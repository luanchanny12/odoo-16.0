# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LibraryBook(models.Model):
    # Dùng _inherit để "kế thừa" (thêm trường vào) model gốc
    _inherit = 'library.book'

    # --- CODE MỚI CỦA NHIỆM VỤ 2 ---

    # 1. Thêm trường One2many (liên kết ngược tới các Đánh giá)
    # Giống hệt trường book_ids trong Tác giả
    review_ids = fields.One2many(
        comodel_name='library.book.review',  # Model "con"
        inverse_name='book_id',  # Trường Many2one ở model "con"
        string='Đánh giá'
    )

    # 2. Thêm trường Computed Field (tính điểm TB)
    average_rating = fields.Float(
        string='Điểm TB',
        compute='_compute_average_rating',  # Nối với hàm bên dưới
        store=True  # Lưu vào CSDL
    )

    # 3. Hàm tính toán Điểm TB
    # Phải "theo dõi" cả 'review_ids' và 'rating' của chúng

    @api.depends('review_ids', 'review_ids.rating')
    def _compute_average_rating(self):
        for book in self:
            # Nếu cuốn sách này có đánh giá
            if book.review_ids:
                # Tính tổng (sum) các điểm (rating)
                # (phải int() vì rating là text '1', '2'...)
                total_rating = sum(int(review.rating) for review in book.review_ids)

                # Tính điểm trung bình
                book.average_rating = total_rating / len(book.review_ids)
            else:
                # Nếu không có đánh giá, gán bằng 0
                book.average_rating = 0.0
# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date
import base64
import io
import logging

_logger = logging.getLogger(__name__)

# Try import Pillow
try:
    from PIL import Image
except Exception as e:
    Image = None
    _logger.warning("Pillow not available: %s", e)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    # --- Thông tin cơ bản ---
    name = fields.Char(string='Tên sách', required=True)
    author_id = fields.Many2one(
        comodel_name='library.author',
        string='Tác giả'
    )
    category_id = fields.Many2one(
        comodel_name='library.book_category',
        string='Thể loại'
    )
    publisher_id = fields.Many2one(
        comodel_name='library.publisher',
        string='Nhà xuất bản'
    )
    publication_date = fields.Date(string='Ngày xuất bản')
    isbn = fields.Char(string='Mã ISBN')
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Mô tả')

    # --- ẢNH BÌA SÁCH ---
    cover_image = fields.Binary(
        string='Ảnh bìa',
        attachment=True
    )

    # --- Lịch sử mượn ---
    borrow_history_ids = fields.One2many(
        comodel_name='library.borrow',
        inverse_name='book_id',
        string='Lịch sử Mượn/Trả',
        readonly=True
    )

    # --- Tuổi sách ---
    age = fields.Integer(
        string='Tuổi sách (năm)',
        compute='_compute_age',
        readonly=True,
        store=True
    )

    @api.depends('publication_date')
    def _compute_age(self):
        for book in self:
            if book.publication_date:
                today = date.today()
                book.age = today.year - book.publication_date.year
            else:
                book.age = 0

    # --- Cảnh báo khi nhập ngày xuất bản sai ---
    @api.onchange('publication_date')
    def _onchange_publication_date(self):
        today = date.today()
        if self.publication_date and self.publication_date > today:
            return {
                'warning': {
                    'title': 'Cảnh báo: Ngày không hợp lệ',
                    'message': 'Bạn đã chọn một ngày xuất bản trong tương lai. Sách này chưa được xuất bản à?'
                }
            }

    # ================================
    #   AUTO RESIZE ẢNH
    # ================================
    def _resize_image_base64(self, image_base64, max_width=900, quality=85):
        """Resize ảnh khi upload để giảm dung lượng và fit màn hình."""
        if not image_base64:
            return image_base64

        if Image is None:
            _logger.warning("Pillow not installed. Cannot resize image.")
            return image_base64

        # Convert base64 -> bytes
        if isinstance(image_base64, str):
            image_bytes = base64.b64decode(image_base64)
        else:
            image_bytes = image_base64

        try:
            img = Image.open(io.BytesIO(image_bytes))
        except Exception as e:
            _logger.error("Cannot open image: %s", e)
            return image_base64

        # Nếu ảnh nhỏ hơn max_width thì giữ nguyên
        if img.width <= max_width:
            return image_base64

        # Tính kích thước mới theo tỷ lệ
        ratio = max_width / float(img.width)
        new_height = int(img.height * ratio)
        resized = img.resize((max_width, new_height), Image.LANCZOS)

        # Convert lại thành JPEG để giảm dung lượng
        buffer = io.BytesIO()
        resized.convert("RGB").save(buffer, format='JPEG', quality=quality)

        # Encode lại base64
        return base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Ghi đè create
    @api.model
    def create(self, vals):
        if vals.get('cover_image'):
            vals['cover_image'] = self._resize_image_base64(vals['cover_image'])
        return super().create(vals)

    # Ghi đè write
    def write(self, vals):
        if vals.get('cover_image'):
            vals['cover_image'] = self._resize_image_base64(vals['cover_image'])
        return super().write(vals)

from odoo import api, fields, models
from odoo.exceptions import ValidationError # thêm thư viện này
class libraryBookReview(models.Model):
    _name = 'library.book.review'
    _description = 'Library Book Review'

    book_id = fields.Many2one(
        comodel_name='library.book', # Model cha (từ model 'my_library')
        string='Sách',
        required=True,
    )

    reviewer_id = fields.Many2one(
        comodel_name='res.partner', #Model Contacts gốc của Odoo
        string='Người đánh giá',
        required=True,
    )

    rating = fields.Selection(
        [
            ('1', '1 Sao'),
            ('2', '2 Sao'),
            ('3', '3 Sao'),
            ('4', '4 Sao'),
            ('5', '5 Sao'),
        ],
        string='Điểm (Sao)',
        required=True,
    )

    comment = fields.Text(string='Bình luận')
    # --- CODE MỚI CỦA NHIỆM VỤ 4 (State field) ---
    state = fields.Selection(
        [
            ('draft', 'Nháp'),
            ('submitted', 'Đã gửi'),
            ('approved', 'Đã duyệt'),
            ('rejected', 'Bị từ chối'),
        ],
        string='Trạng thái',
        default='draft',  # Mặc định luôn là 'Nháp'
        required=True,
    )

    # --- CODE MỚI CỦA NHIỆM VỤ 4 (Hàm cho nút bấm) ---

    # Hàm cho nút "Gửi"
    def action_submit(self):
        # 'self' là bản ghi Đánh giá hiện tại
        # self.write() dùng để cập nhật giá trị
        self.write({'state': 'submitted'})

    # Hàm cho nút "Duyệt"
    def action_approve(self):
        self.write({'state': 'approved'})

    # Hàm cho nút "Từ chối"
    def action_reject(self):
        self.write({'state': 'rejected'})

    # (Hàm _check_rating_comment của Nhiệm vụ 2 vẫn ở đây)

    @api.constrains('rating', 'comment')
    def _check_rating_comment(self):
        # Hàm này sẽ chạy KHI BẤM LƯU (SAVE)
        for review in self:
            # Chuyển 'rating' (dạng text '1', '2'...) thành SỐ (Integer)
            # Dùng int() để so sánh
            if int(review.rating) < 3 and not review.comment:
                # Nếu điểm < 3 SAO VÀ không có bình luận
                # Ném ra lỗi pop-up màu đỏ, CHẶN không cho lưu
                raise ValidationError("Vui lòng cho biết lý do (Bình luận) tại sao bạn đánh giá thấp (dưới 3 sao).")

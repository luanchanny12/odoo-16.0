from odoo import models, fields, api
from datetime import date
from odoo.exceptions import AccessError


class Student(models.Model):
    _name = 'x.student'
    _description = 'Sinh viên'
    _rec_name = 'name'

    # =====================
    # BASIC INFO
    # =====================
    name = fields.Char(
        string='Tên sinh viên',
        required=True
    )

    student_code = fields.Char(
        string='Mã sinh viên',
        required=True,
        copy=False,
        index=True
    )

    birth_date = fields.Date(
        string='Ngày sinh'
    )

    gender = fields.Selection(
        [
            ('male', 'Nam'),
            ('female', 'Nữ'),
            ('other', 'Khác')
        ],
        string='Giới tính',
        default='other'
    )

    email = fields.Char(
        string='Email',
        required=True
    )

    phone = fields.Char(
        string='Số điện thoại'
    )

    # TASK SAU: chuyển sang model major
    major = fields.Char(
        string='Ngành học',
        required=True
    )

    # =====================
    # STATUS
    # =====================
    state = fields.Selection(
        [
            ('studying', 'Đang học'),
            ('paused', 'Tạm nghỉ'),
            ('graduated', 'Tốt nghiệp')
        ],
        string='Trạng thái',
        default='studying'
    )

    # =====================
    # SYSTEM
    # =====================
    age = fields.Integer(
        string='Tuổi',
        compute='_compute_age',
        store=True
    )

    user_id = fields.Many2one(
        'res.users',
        string='Tài khoản đăng nhập',
        readonly=True,
        help="Tài khoản website của sinh viên (nếu có)"
    )

    # =====================
    # CONSTRAINTS
    # =====================
    _sql_constraints = [
        (
            'student_code_unique',
            'unique(student_code)',
            'Mã sinh viên đã tồn tại!'
        ),
        (
            'email_unique',
            'unique(email)',
            'Email đã tồn tại!'
        )
    ]

    # =====================
    # COMPUTE
    # =====================
    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                    (today.month, today.day) <
                    (rec.birth_date.month, rec.birth_date.day)
                )
            else:
                rec.age = 0

    # =====================
    # BUSINESS ACTIONS
    # =====================
    def action_pause(self):
        """
        Chỉ ADMIN mới được cho sinh viên tạm nghỉ
        """
        if not self.env.user.has_group('base.group_system'):
            raise AccessError("Bạn không có quyền thực hiện thao tác này.")

        for rec in self:
            rec.state = 'paused'

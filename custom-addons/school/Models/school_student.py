from odoo import api, fields, models, _
from datetime import date


class SchoolStudent(models.Model):
    # Sửa lại _name cho đúng chuẩn Odoo
    _name = 'school.student'
    _description = 'Student Information'
    # Thêm chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Student Name', required=True, tracking=True)
    student_code = fields.Char(string='Student ID', required=True, copy=False)
    image = fields.Binary(string='Image')
    birth_date = fields.Date(string='Date of Birth')

    # Trường compute (tự động tính toán) tuổi
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')

    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')

    # Trường quan hệ: Mỗi học sinh thuộc về MỘT lớp học
    class_id = fields.Many2one('school.class', string='Class')

    # Ràng buộc SQL: Đảm bảo Student ID là duy nhất
    _sql_constraints = [
        ('student_code_uniq', 'unique(student_code)', 'Student ID must be unique!')
    ]

    @api.depends('birth_date')
    def _compute_age(self):
        """Tính tuổi dựa trên ngày sinh"""
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = today.year - record.birth_date.year - \
                             ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
            else:
                record.age = 0
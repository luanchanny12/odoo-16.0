from odoo import fields, models

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char(string='Teacher Name', required=True)
    teacher_code = fields.Char(string='Teacher ID', required=True, copy=False)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    subject = fields.Char(string='Subject Taught')

    # Trường quan hệ: Mỗi giáo viên chủ nhiệm NHIỀU lớp
    class_ids = fields.One2many('school.class', 'homeroom_teacher_id', string='Homeroom Classes')

    _sql_constraints = [
        ('teacher_code_uniq', 'unique(teacher_code)', 'Teacher ID must be unique!')
    ]
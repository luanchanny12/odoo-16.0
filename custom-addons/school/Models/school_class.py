from odoo import fields, models


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)

    # Trường quan hệ: Mỗi lớp có MỘT giáo viên chủ nhiệm
    homeroom_teacher_id = fields.Many2one('school.teacher', string='Homeroom Teacher')

    # Trường quan hệ: Mỗi lớp có NHIỀU học sinh
    student_ids = fields.One2many('school.student', 'class_id', string='Students')
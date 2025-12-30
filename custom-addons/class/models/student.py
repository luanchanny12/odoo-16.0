from odoo import models, fields, api

class TrainingStudent(models.Model):
    _name = 'training.student'
    _description = 'Student'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    score = fields.Float(string='Score')
    @api.model
    def create_student(self, name, age, score):
        return self.create({
            'name': name,
            'age': age,
            'score': score,
        })

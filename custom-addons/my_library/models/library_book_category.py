from odoo import fields, models

class LibraryBookCategory(models.Model):
    _name = 'library.book_category'
    _description = 'Library Book Category'

    name = fields.Char(string='Thể loại', required=True)

    book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name='category_id',
        string='danh sách',
    )
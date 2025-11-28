from odoo import fields,models

class LibraryPublisher(models.Model):
    _name = 'library.publisher'
    _description = 'Library Publisher'

    name=fields.Char(string='Nhà xuất bản',required=True)
    website=fields.Char(string='website')


    book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name='publisher_id',
        string='danh sách',
    )
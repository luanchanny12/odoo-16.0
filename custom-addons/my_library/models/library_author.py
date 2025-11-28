# -*- coding: utf-8 -*-
from odoo import models,fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char('tên tác giả', required=True)
    biography = fields.Text(string='Tiểu sử')

    book_ids = fields.One2many(
        comodel_name='library.book', # liên kết tới model 'library.book'
        inverse_name='author_id',      #dựa trên trường 'author_id' của Model 'library.book'
        string='sách đã viết'
    )
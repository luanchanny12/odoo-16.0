# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class LibraryWebsite(http.Controller):

    # Route xem chi tiết sách
    @http.route('/book/<int:book_id>', type='http', auth='public', website=True)
    def book_detail(self, book_id, **kw):
        book = request.env['library.book'].sudo().browse(book_id)
        if not book.exists():
            return request.not_found()
        return request.render('my_library.book_detail_template', {'book': book})

    # Route mượn sách
    @http.route('/thu-vien/muon/<int:book_id>', type='http', auth='public', website=True)
    def borrow_book(self, book_id, **kw):
        book = request.env['library.book'].sudo().browse(book_id)
        if not book.exists():
            return request.not_found()
        # Ở đây bạn có thể thêm logic mượn sách
        return request.redirect('/')

    # Route yêu thích sách
    @http.route('/thu-vien/yeu-thich/<int:book_id>', type='http', auth='public', website=True)
    def favorite_book(self, book_id, **kw):
        book = request.env['library.book'].sudo().browse(book_id)
        if not book.exists():
            return request.not_found()
        # Ở đây bạn có thể thêm logic yêu thích sách
        return request.redirect('/')

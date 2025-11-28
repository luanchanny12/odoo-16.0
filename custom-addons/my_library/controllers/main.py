# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class LibraryWebsite(http.Controller):

    # --------------------------
    # 1. XEM CHI TIẾT SÁCH
    # --------------------------
    @http.route('/book/<int:book_id>', type='http', auth='public', website=True)
    def book_detail(self, book_id, **kw):
        book = request.env['library.book'].sudo().browse(book_id)
        if not book.exists():
            return request.not_found()

        return request.render('my_library.book_detail_template', {
            'book': book,
        })

    # --------------------------
    # 2. GỬI ĐÁNH GIÁ SÁCH
    # --------------------------
    @http.route('/thu-vien/danh-gia/gui',
                type='http', auth='public', website=True,
                methods=['POST'], csrf=False)
    def submit_review(self, **post):

        book_id = post.get('book_id')
        rating = post.get('rating')
        comment = post.get('comment')

        if book_id and rating:
            reviewer = request.env.user.partner_id

            request.env['library.book.review'].sudo().create({
                'book_id': int(book_id),
                'reviewer_id': reviewer.id,
                'rating': str(rating),  # ⭐ FIX QUAN TRỌNG NHẤT
                'comment': comment,
                'state': 'submitted'
            })

        return request.redirect('/book/%s' % book_id)  # ⭐ FIX THỨ HAI

    # --------------------------
    # 3. GIẢ LẬP MƯỢN SÁCH
    # --------------------------
    @http.route('/thu-vien/muon/<int:book_id>', type='http', auth='public', website=True)
    def borrow_book(self, book_id, **kw):
        return request.redirect('/book/%s' % book_id)

    # --------------------------
    # 4. GIẢ LẬP YÊU THÍCH SÁCH
    # --------------------------
    @http.route('/thu-vien/yeu-thich/<int:book_id>', type='http', auth='public', website=True)
    def favorite_book(self, book_id, **kw):
        return request.redirect('/book/%s' % book_id)

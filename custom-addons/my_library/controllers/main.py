# -*- coding: utf-8 -*-
from odoo import http, fields
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

        # Lấy flash message nếu có
        flash_message = request.session.pop('my_flash', False)

        return request.render('my_library.book_detail_template', {
            'book': book,
            'flash_message': flash_message,
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
            if reviewer:
                request.env['library.book.review'].sudo().create({
                    'book_id': int(book_id),
                    'reviewer_id': reviewer.id,
                    'rating': str(rating),
                    'comment': comment,
                    'state': 'submitted'
                })
        return request.redirect('/book/%s' % book_id)

    # --------------------------
    # 3. MƯỢN SÁCH (TẠO PHIẾU + FLASH MESSAGE)
    # --------------------------
    @http.route('/thu-vien/muon/<int:book_id>', type='http', auth='public', website=True)
    def borrow_book(self, book_id, **kw):
        book = request.env['library.book'].sudo().browse(book_id)
        if not book.exists():
            return request.not_found()

        borrower = request.env.user.partner_id
        if not borrower:
            # Chưa đăng nhập → chuyển tới login
            return request.redirect('/web/login?redirect=/thu-vien/muon/%s' % book_id)

        # Tạo phiếu mượn
        request.env['library.borrow'].sudo().create({
            'book_id': book.id,
            'borrower_id': borrower.id,
            'state': 'draft',
            'borrow_date': fields.Date.today()
        })

        # Thêm flash message
        request.session['my_flash'] = 'Phiếu mượn sách đã được tạo!'

        return request.redirect('/book/%s' % book_id)

    # --------------------------
    # 4. YÊU THÍCH SÁCH
    # --------------------------
    @http.route('/thu-vien/yeu-thich/<int:book_id>', type='http', auth='public', website=True)
    def favorite_book(self, book_id, **kw):
        # Hiện tại chỉ redirect, có thể bổ sung logic thêm sau
        return request.redirect('/book/%s' % book_id)

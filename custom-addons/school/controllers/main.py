# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SchoolController(http.Controller):

    @http.route('/school/hello', auth='public', website=True)
    def hello(self, **kw):
        """Đây là một controller đơn giản trả về một trang web."""
        # Bạn có thể lấy dữ liệu từ database, ví dụ đếm số học sinh
        student_count = request.env['school.student'].search_count([])

        # Trả về HTML
        return (
            "<h1>Hello from School Management!</h1>"
            f"<p>We currently have {student_count} students registered.</p>"
        )
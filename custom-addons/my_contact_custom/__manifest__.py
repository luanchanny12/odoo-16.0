# -*- coding: utf-8 -*-
{
    'name': "My Contact Customization",
    'summary': "Thêm cấp độ khách hàng vào model Đối tác",
    'description': "Bài tập 5: Kế thừa (Inheritance)",
    'author': "Nguyễn Thanh Luân",
    'category': 'Uncategorized',
    'version': '1.0',

    # --- PHẦN QUAN TRỌNG NHẤT ---
    # Module này 'phụ thuộc' vào module 'contacts' gốc của Odoo.
    # Odoo sẽ đảm bảo 'contacts' được nạp TRƯỚC khi nạp module này.
    'depends': ['contacts'],  # (Bạn cũng có thể dùng 'base' nếu chỉ sửa 'res.partner')

    'data': [
        # KHÔNG CÓ file security, vì chúng ta dùng model có sẵn
        'views/res_partner_views.xml',  # Chỉ cần nạp file view
    ],
    'installable': True,
}
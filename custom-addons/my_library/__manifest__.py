# -*- coding: utf-8 -*-
{
    'name': 'My Library',
    'summary': "Quản lý sách trong thư viện cá nhân",
    'description': """
        Module cơ bản để thực hành Odoo:
        - Quản lý sách, Tác giả, Thể loại, NXB
        - Quản lý Mượn/Trả sách
        - Báo cáo PDF
        - Website Thư viện
    """,
    'author': 'Nguyễn Thanh Luân',
    'website': 'https://www.nual12th.com',
    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base', 'website'],

    'data': [
        # Security
        'security/library_security.xml',
        'security/ir.model.access.csv',

        # Data
        'data/library_cron.xml',
        'data/library_server_actions.xml',

        # Views
        'views/library_book_views.xml',
        'views/library_author_views.xml',
        'views/library_book_category_views.xml',
        'views/library_publisher_views.xml',
        'views/library_borrow_views.xml',

        # Website templates
        'views/book_detail_template.xml',
        'views/library_book_website_template.xml',

        # Reports
        'reports/library_borrow_report.xml',

        # Wizards
        'wizard/library_return_wizard_views.xml',
    ],

    'assets': {
        'website.assets_frontend': [
            'my_library/static/src/css/library.css',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

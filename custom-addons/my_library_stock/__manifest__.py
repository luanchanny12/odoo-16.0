# -*- coding: utf-8 -*-
{
    'name': "Library Stock",
    'summary': "Quản lý nhập xuất tồn kho sách",
    'author': "Nguyễn Thanh Luân",
    'version': '1.0',
    'depends': ['base', 'my_library'], # Phụ thuộc vào module Sách

    'data': [
        'security/ir.model.access.csv',
        'views/library_stock_move_views.xml',
        'views/library_book_views_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
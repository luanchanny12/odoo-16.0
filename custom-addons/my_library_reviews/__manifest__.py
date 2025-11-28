{
    'name': "Book Reviews",
    'version': "1.0",
    'summary': "Đánh giá sách hay sách dở",
    'author': "Nguyễn Thanh Luân",
    'category': "Uncategorized",
    'depends': ["base", "my_library", "contacts"],
    'data': [
        'security/ir.model.access.csv',
        'views/review_views.xml',
        'views/library_book_views_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
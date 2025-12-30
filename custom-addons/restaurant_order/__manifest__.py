{
    'name': 'Order fast food',
    'version': '1.0',
    'summary': 'Ứng dụng order đồ ăn nhanh',
    'sequence': 10,

    'depends': [
        'base',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/menu_item_view.xml',
        'views/order_line_view.xml',
        'views/order_view.xml',
    ],

    'category': 'Uncategorized',
    'author': 'luanchanny',
    'website': 'http://www.luanchanny.com',
    'lincese': 'LGPL-3',
    'description': """
    App đặt đồ ăn, đồ uống nhanh
    """,

    'installable': True,
    'auto_install': False,
    'application': True,
}
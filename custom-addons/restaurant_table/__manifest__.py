from odoo.api import depends

{
    'name': 'Đặt bàn ăn',
    'version': '1.0',
    'summary': 'Ứng dụng đặt bàn ăn',
    'sequence': 20,

    'depends': [
        'base',
        'contacts',
    ],

    'data' : [
        'security/ir.model.access.csv',

        'views/table_management_view.xml',
    ],

    'category': 'Uncategorized',
    'author': 'luanchanny',
    'website': 'https://www.luanchanny.com',
    'lincese': '',
    'description': """
    Đặt chỗ ngồi cho bàn ăn
    """,

    'installable': True,
    'auto_install': False,
    'application': True,
}
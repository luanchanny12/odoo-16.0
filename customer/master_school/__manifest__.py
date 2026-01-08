{
    'name': 'master-school',
    'version': '1.0',
    'summary': 'trường đại học master school',
    'author': 'Nguyễn Thanh Luân',
    'website': 'https://www.nual12th.com',
    'category': 'Education',

    'depends': [
        'base',
'website',
    ],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/student_menu.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
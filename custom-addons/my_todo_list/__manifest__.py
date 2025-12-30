# -*- coding: utf-8 -*-
{
    'name': "My To-do List",
    'summary': "Module thực hành về Computed Fields và Onchange",
    'description': "Quản lý các công việc cần làm (To-do Task)",
    'author': "Nguyễn Thanh Luân",
    'category': 'Uncategorized',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
    ],
    'application': True,
    'installable': True,
}

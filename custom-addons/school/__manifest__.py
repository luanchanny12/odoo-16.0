{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Management',
    'author': 'ahihi',
    'description': '''
        Quan ly truong hoc
    ''',
    'website': 'http://www.ahihihi.com',
    'depends': ['base', 'mail'],
    'data': [
        # THÊM CÁC DÒNG NÀY:
        'security/ir.model.access.csv',
        'views/school_student_views.xml',
        'views/school_class_views.xml',
        'views/school_teacher_views.xml',
        'views/school_menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    # Thêm 'assets' nếu controller của bạn dùng file CSS/JS riêng
    'assets': {},
}
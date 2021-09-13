{
    'name': 'Second Module',
    'version': '1.0',
    'summary': 'Learn odoo inherit',
    'description': 'Learn odoo inherit',
    'category': 'Other',
    'author': 'mr. Long',
    'depends': [
        'first_module',
    ],
    'data': [
        'views/customer_view.xml',
        'views/employee_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

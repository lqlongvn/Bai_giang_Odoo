{
    'name': 'Second Module',
    'version': '1.0',
    'summary': 'Learn odoo inherit',
    'description': 'Learn odoo inherit',
    'category': 'Other',
    'author': 'mr. Long',
    'depends': [
        'base',
        'first_module',
    ],
    'data': [
        'views/customer_view.xml',
        'views/employee_view.xml',
        'views/res_partner_view.xml',
        'security/security.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

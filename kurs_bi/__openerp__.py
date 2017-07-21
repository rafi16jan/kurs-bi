# -*- coding: utf-8 -*-
{
    'name': "Kurs BI",

    'summary': """
        Kurs BI
    """,

    'description': """
    """,

    'author': "Farrell Rafi",
    'website': "http://odooabc.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/kurs.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

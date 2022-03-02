# -*- coding: utf-8 -*-
{
    'name': "APF-SGE",

    'summary': """
        Ejercicio opcional de desarrollo de modulo ODOO.
        """,

    'description': """
        Este módulo es un desarrollo opcional para el modulo SGE del ciclo formativo 2º DAM.
    """,

    'author': "Alberto Pérez Fructuoso",
    'website': "https://github.com/alateka",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # (Diferencia entre módulo y aplicación - Una aplicación es un conjunto de módulos)
    # En el caso que queramos desarrollar una aplicación en vez de un módulo,
    # se pondría la siguiente clave a True.
    'application': True
}

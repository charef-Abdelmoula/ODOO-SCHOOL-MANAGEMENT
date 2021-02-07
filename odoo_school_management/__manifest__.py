# -*- coding: utf-8 -*-
{
    'name': "Odoo School Management",

    'summary': """
    Odoo module:School Management
        """,

    'description': """
        This module will cover all school management process
    """,

    'author': "InfoScoping",
    'website': "http://www.infoscoping.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/school_subject_view.xml',
        'views/school_classroom_view.xml',
        'views/school_session_view.xml',
        'views/school_teacher_view.xml',
        'views/school_student_view.xml',
        'views/school_transfer_request_view.xml',
        'data/activities.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

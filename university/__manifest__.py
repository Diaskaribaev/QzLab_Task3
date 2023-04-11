# -*- coding: utf-8 -*-
{
    'name': "university",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','website','portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/menu.xml',
        'views/organization_view.xml',
        'views/student_view.xml',
        'views/speciality_view.xml',
    ],

}

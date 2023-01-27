# -*- coding:utf-8 -*-
{
    'name': "TPO",
    'author': "Sanket Brahmbhatt(sabr)",
    'summary': "Build a training and placement opeartion",
    'version': '1.0',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'view/action_all_file.xml',
        'view/student_student.xml',
        'view/tpo_propert_view.xml',
        'view/details_company.xml',
        'view/res_user_view.xml',
        'view/technical_skills_views.xml',
        'view/apply_to_College_view.xml',
        'view/report.xml',
        'view/report_pdf_student.xml',
        'view/tpo_property_menu.xml',
        ],
    'demo': [
        'demo/student_student_demo.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}

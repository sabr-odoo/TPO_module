# -*- coding:utf-8 -*- 
{
    'name' : "TPO",
    'author' : "Sanket Brahmbhatt(sabr)",
    'summary' : "Build a training and placement opeartion",
    'version' : '1.0' ,
    'depends' : ['mail'],
    'data' : [
       'view/tpo_propert_view.xml',
        'view/student_student.xml',
        'view/details_company.xml',
        'view/res_user_view.xml',
        'view/technical_skills_views.xml',
        'view/apply_to_College_view.xml',
        'view/tpo_property_menu.xml',
        'security/ir.model.access.csv',
     ],
    'application' : True,
    'installable': True,
    'license': 'LGPL-3',
    # 'demo': [
    #    'demo/demo_student_student.xml',
    # ],
}
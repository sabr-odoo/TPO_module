# -*- coding:utf-8 -*- 
{
    'name' : "Company",
    'author' : "Sanket Brahmbhatt(sabr)",
    'summary' : "Build a Application for Further student",
    'version' : '1.0' ,
    'depends' : ['mail'], 
    'data' : [
        'views/higher_student_view.xml',
        # 'views/student_student_view.xml',
        'views/further_student_menu.xml',
        'security/ir.model.access.csv',
     ],
    'application' : True,
    'installable': True,
    'license': 'LGPL-3',
   
}

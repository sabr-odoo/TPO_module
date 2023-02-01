from odoo import http


class Student(http.Controller):
    @http.route('/exam', auth='public')
    def student(self, **kw):
        Student_list = http.request.env['student.student']
        return http.request.render('TPO.student', {
            'students': Student_list.search([])
        })
    
    @http.route('/exam/<model("student.student"):student_data>/', auth='public', website=True)
    def student_data(self, student_data):
        return http.request.render('TPO.student_data_link',{
            'student_data':student_data
        })
# -*- coding : utf-8 -*-

from odoo import http


class TPO(http.Controller):
    @http.route('/TPO', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['tpo.name']
        return http.request.render('TPO.index', {
            'teachers': Teachers.search([])
        })

    # @http.route('/TPO/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)

    
    @http.route('/TPO/<model("tpo.name"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('TPO.student_student_id_data',{
            'teacher':teacher
        })
   

    # @http.route('/real_estate', auth='public')
    # def index(self, **kw):
    #     return http.request.render('real_estate.index' ,{
    #         'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
    #     })

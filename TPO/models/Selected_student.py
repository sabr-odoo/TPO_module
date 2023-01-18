# -*- coding:utf-8 -*-

from odoo import models, fields


class SelectedStudent(models.Model):
    _name = "selected.student"
    _description = "Selected Student Here"
    # _inherits = { 
    #              'student.student':'student_student_id',
    #              'details.student':'details_student_id'
    #             }
    
    
    # student_student_id=fields.Many2one('student.student')
    # details_student_id=fields.Many2one('details.student') 
    
    abc = fields.Char(String="Name")
    maker = fields.Char(string='Maker')

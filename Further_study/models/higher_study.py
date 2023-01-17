# -*- coding:utf-8 -*-  
 
from odoo import models,api,fields

class HigherStudy(models.Model):
    _name= 'higher.study'
    _description = "higher Student" 
    
    name = fields.Char(string="Name")
    # higher_studentids = fields.One2many('student.student','Student_id')
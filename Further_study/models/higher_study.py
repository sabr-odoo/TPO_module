# -*- coding:utf-8 -*-

from odoo import models, api, fields


class HigherStudy(models.Model):
    _name = 'higher.study'
    _description = "higher Student"
    _inherit = "student.student"

    name = fields.Char(string="Name")
    # country_id = fields.Many2one(
    #     'res.country', string='Country', required=True)
    # higher_studentids = fields.One2many('student.student','Student_id')
    career = fields.Char()
    teacher_name = fields.Char()
    
    
    
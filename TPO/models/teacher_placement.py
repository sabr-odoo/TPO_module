# -*- coding:utf-8 -*-

from odoo import models,fields,api

class sa(models.Model):
    _name="teacher.placement"
    _description="Placement information about teacher"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char()
    department_teacher= fields.Selection(
          selection=[('mca','MCA'),('information_technology', 'Information Technology'),('computer','Computer'),('mechanical', 'Mechanical')]   
          )
    student_nameids =fields.One2many('student.student','teacher_placement_id',string="stduent name")  
    offeres_ids = fields.One2many("student.student","teacher_placement_id",string="Offer IDs")
    student_count = fields.Integer('student count',compute="_compute_student_count")
    # company_ids = fields.One2many('details.company','deta_company')
    # company_count = fields.Integer('Company Count',compute= "_compute_company_count")

    @api.depends('offeres_ids','student_count')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.offeres_ids) 

    # @api.depends('company_ids','company_count')
    # def _compute_student_count(self):
    #     for record in self:
    #         record.company_count = len(record.company_ids) 
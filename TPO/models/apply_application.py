# -*- coding:utf-8 -*-

from  odoo import models,fields

class applyApplication(models.Model):
    _name="apply.application"
    _description="student can apply selected company"

    name=fields.Many2one('details.company')
    s_name=fields.Many2one('student.student')
    s_id=fields.Many2one('student.student')
    te_name=fields.Many2one('teacher.placement')
    add_some=fields.Text()
    select_apply=fields.Selection(
          selection=[('software_developer','Software Developer'),('business_analyst', 'Business Analyst'),('sales_intern','Sales Intern')]   
          )    
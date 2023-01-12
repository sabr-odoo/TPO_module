#-*- coding:utf-8 -*-

from odoo import models,fields 

class resumeStudent(models.Model):
    _name="resume.student"
    _description="Student of resume form"
    _inherit = ["mail.thread", "mail.activity.mixin"]
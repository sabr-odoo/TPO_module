# -*- coding:utf-8 -*-

from odoo import models,fields 

class studentPlacement(models.Model):
    _name="student.placement"
    _description="Placement information about student"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char()
    
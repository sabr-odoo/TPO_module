# -*- coding:utf-8 -*-

from odoo import models,fields 

class studentPlacement(models.Model):
    _name="student.placement"
    _description="Placement information about student"

    name = fields.Char()
    
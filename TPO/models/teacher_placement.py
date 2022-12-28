# -*- coding:utf-8 -*-

from odoo import models,fields  

class sa(models.Model):
    _name="teacher.placement"
    _description="Placement information about teacher"

    name = fields.Char()
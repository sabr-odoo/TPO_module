# -*- coding:utf:8 -*-
 
from odoo import models,fields,api 

class ResUser(models.Model):
    _inherit = "res.users"
    
    username_ids = fields.One2many('student.student','institution_name_id')

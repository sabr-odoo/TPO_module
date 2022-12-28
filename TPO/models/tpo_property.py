# -*- coding:utf-8 -*- 

from odoo import models,fields 

class tpoProperty(models.Model):
    _name="tpo.property"
    _description="Training and Placement Department" 

    name = fields.Char()
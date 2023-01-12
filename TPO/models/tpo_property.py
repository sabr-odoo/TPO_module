# -*- coding:utf-8 -*- 

from odoo import models,fields 

class tpoProperty(models.Model):
    _name="tpo.property"
    _description="Training and Placement Department"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char()
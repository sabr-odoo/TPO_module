# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError


class StudentStudent(models.Model):
    _inherit = "student.student"

    name = fields.Char()
    

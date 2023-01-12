# -*- coding:utf:8 -*-

from odoo import models, fields


class TechnicalSkills(models.Model):
    _name = "technical.skills"
    _description = "technical skills for student direct choice  module"
    _order = "name desc"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True)
    com_languageid = fields.Char('details.company')
    color = fields.Integer(string="color")
    color_2 = fields.Char(string="color 2")

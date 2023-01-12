# -*- coding:utf-8 -*-

from odoo import models, fields, api


class detailsCompany(models.Model):
    _name = "details.company"
    _description = "hey"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char()
    description = fields.Text()
    deapartment = fields.Selection(
        selection=[('mca', 'MCA'), ('information_technology', 'Information Technology'),
                   ('computer', 'Computer'), ('mechanical', 'Mechanical')]
    )
    country_id = fields.Many2one(
        'res.country', string='Country', required=True)
    education = fields.Char()
    stipend = fields.Integer()
    website = fields.Char()
    working_mode = fields.Selection(
        selection=[('hybrid', 'Hybrid'), ('Work_from_home', 'Work From Home'), ('work_from_office', 'Work From Office')], default="work_from_office "
    )
    bond = fields.Selection(
        selection=[('1year', '1year'), ('1.5year',
                                        '1.5year'), ('2year', '2 Year')]
    )
    package = fields.Integer()
    experience = fields.Integer()
    address = fields.Text()
    position = fields.Char()
    langauge = fields.Many2many('technical.skills')
    process = fields.Char()
    date_joining = fields.Date()
    deta_company = fields.Many2one('teacher.placement')
    student_select = fields.One2many(
        'apply.application', 'c_name_id', string="Student List")

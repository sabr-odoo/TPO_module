# -*- coding:utf-8 -*-

from odoo import models, fields, api


class StudentStudent(models.Model):
    _name = "student.student"
    _description = "Student of application form"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char()
    Student_id = fields.Many2one('teacher.placement', string="Student ID")
    DOB = fields.Date()
    age = fields.Integer()
    number = fields.Char()
    email = fields.Char()
    address = fields.Char()
    city = fields.Char()
    dist = fields.Char()
    state = fields.Char()
    pincode = fields.Integer()
    ssc = fields.Integer()
    hsc = fields.Integer()
    cgpa = fields.Integer(string="CGPA", compute="_compute_CGPA_count")
    n_backlog = fields.Integer()
    branch = fields.Selection(
        selection=[('mca', 'MCA'), ('information_technology', 'Information Technology'),
                   ('computer', 'Computer'), ('mechanical', 'Mechanical')]
    )
    state = fields.Selection(
        selection=[('new', 'New'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default="new"
    )
    Career_option = fields.Selection(
        selection=[('placement', 'Placement'), ('higher_education', 'Higher Education'),
                   ('family_business', 'Family Business'), ('others', 'Others')]
    )
    passing_year = fields.Selection(
        selection=[('pass_2023', '2023'), ('2024', '2024'),
                   ('2025', '2025'), ('2026', '2026')]
    )
    teacher_placement_id = fields.Many2one("teacher.placement")
    
    company_placement_id = fields.Many2one(
        "details.company", string="Company Name")
    # Resume fields
    description = fields.Text()
    onesem = fields.Integer()
    secondsem = fields.Integer()
    thirdsem = fields.Integer()
    foursem = fields.Integer()
    fivesem = fields.Integer()
    sixsem = fields.Integer()
    objective = fields.Text()
    linkedin = fields.Char()
    github = fields.Char()
    skill = fields.Text()
    technical_skill = fields.Many2many('technical.skills')
    intership = fields.Text()
    project = fields.Text()
    apply_company = fields.One2many('apply.application', 's_name_id')

    @api.depends('onesem', 'secondsem', 'thirdsem', 'foursem', 'fivesem', 'sixsem')
    def _compute_CGPA_count(self):
        for record in self:
            num = record.onesem + record.secondsem + record.thirdsem + \
                record.foursem + record.fivesem + record.sixsem
            record.cgpa = num / 6

    # @api.depends('apply_company')
    # def _compute_career_student(self):
    #   for record in self:
    #     if record.Career_option == 'placement':
    #         return record.apply_company

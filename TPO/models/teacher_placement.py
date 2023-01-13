# -*- coding:utf-8 -*-

from odoo import models, fields, api


class sa(models.Model):
    _name = "teacher.placement"
    _description = "Placement information about teacher"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char()
    department_teacher = fields.Selection(
        selection=[('mca', 'MCA'), ('information_technology', 'Information Technology'),
                   ('computer', 'Computer'), ('mechanical', 'Mechanical')])
    student_nameids = fields.One2many(
        'student.student', 'teacher_placement_id', string="stduent name")
    offeres_ids = fields.One2many(
        "student.student", "teacher_placement_id", string="Offer IDs")
    student_count = fields.Integer(
        'student count', compute="_compute_student_count")
    from_date = fields.Datetime(string='Start', required=True)
    subject_name = fields.Selection(
        selection=[('compound_interest', 'Compound Interest'), ('inequality', 'Inequality'),
                   ('arithmetic_aptitude', 'Arithmetic Aptitude'), ('verbal_ability', 'Verbal Ability')])

    @api.depends('offeres_ids', 'student_count')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.offeres_ids)

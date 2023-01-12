# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class applyApplication(models.Model):
    _name = "apply.application"
    _description = "student can apply selected company"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    c_name_id = fields.Many2one('details.company')
    s_name_id = fields.Many2one('student.student')
    te_name_id = fields.Many2one('teacher.placement')
    add_some = fields.Text()
    select_apply = fields.Selection(
        selection=[('software_developer', 'Software Developer'),
                   ('business_analyst', 'Business Analyst'), ('sales_intern', 'Sales Intern')]
    )
    status = fields.Selection(
        selection=[('selected', 'SELECTED'), ('not_selected', 'NOT SELECTED')])
    apply_appid = fields.Many2one('student.student')

    @api.depends('status')
    def action_selected(self):
      for record in self:
            record.status = 'selected' 
            return True


    @api.depends('status')
    def action_not_selected(self):
       for record in self:
            record.status = 'not_selected' 
       return True
# @api.depends("status")
# def action_accept(self):
#     for record in self:
#         if record.status == "accepted":
#             raise ValidationError(('The default Unit of Measure and the purchased Unit of Measure must be in the same category.'))
# def action_refuse(self):
#     for record in self:
#         if record.status == "refused":
#             return True

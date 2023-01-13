# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError


class applyApplication(models.Model):
    _name = "apply.application"
    _description = "student can apply selected company"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    c_name_id = fields.Many2one('details.company')
    s_name_id = fields.Many2one('student.student' )
    te_name_id = fields.Many2one('teacher.placement')
    add_some = fields.Text()
    select_apply = fields.Selection(
        selection=[('software_developer', 'Software Developer'),
                   ('business_analyst', 'Business Analyst'), ('sales_intern', 'Sales Intern')]
    )
    status = fields.Selection(
        selection=[('selected', 'SELECTED'), ('not_selected', 'NOT SELECTED'), ('on_process', 'On Process')])
    # ,compute="_compute_header_status"
    apply_appid = fields.Many2one('student.student')
    # name=fields.Many2one(related='s_name_id.apply_name')
    
    # @api.depends('status','s_name_id.state')
    # def _compute_header_status(self):
    #     for record in self:
    #         if record.status == 'selected':
    #             raise UserError("cancel Properties cannot be sold")
    #         record.s_name_id.state = 'selected'
            
    
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
   
    @api.depends('status')
    def action_process(self):
       for record in self:
            record.status = 'on_process'
            return True

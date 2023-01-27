# # -*- coding:utf:8 -*-

# from odoo import models, fields, api


# class Report(models.Model):
#     _name = "report.account_batch_payment.print_batch_payment"
#     _template = 'account_batch_payment.print_batch_payment'
#     _inherit = "student.student"
#     _description = "Generate Pdf file"


#     name=fields.Char()
# # @api.model
# # def _get_report_values(self, docids, data=None):
# #     report_name = 'stduent.stduent.print.pdf'
# #     report = self.env['ir.actions.report']._get_report_from_name(
# #         report_name)
# #     return {
# #         'doc_ids': docids,
# #         'doc_model': report.model,
# #         'docs': self.env[report.model].browse(docids),
# #         'pages': self.get_pages,
# #     }


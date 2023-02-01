from odoo import models, fields, api

class TpoName(models.Model):
    _name = 'tpo.name'

    name = fields.Char()
    text = fields.Html()
    age = fields.Integer()
    number = fields.Char()
    email = fields.Char()
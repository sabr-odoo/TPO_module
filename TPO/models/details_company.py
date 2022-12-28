# -*- coding:utf-8 -*- 

from odoo import models,fields

class detailsCompany(models.Model):
    _name="details.company"
    _description="hey"

    name=fields.Char()
    deapartment =fields.Selection(
          selection=[('mca','MCA'),('information_technology', 'Information Technology'),('computer','Computer'),('mechanical', 'Mechanical')]   
          )
    education=fields.Char()
    stipend=fields.Integer()
    website=fields.Char()
    


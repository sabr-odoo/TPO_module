#-*- coding:utf-8 -*-

from odoo import models,fields  

class applictionStudent(models.Model):
    _name="application.student"
    _description="Student of application form" 

    name = fields.Char()
    Student_id=fields.Char(string="Student ID")
    DOB=fields.Date()
    age=fields.Integer()
    number=fields.Char()
    email= fields.Char()
    address= fields.Char()
    city =fields.Char()
    dist= fields.Char()
    state=fields.Char()
    pincode = fields.Integer()
    ssc=fields.Integer()
    hsc=fields.Integer()
    cgpa=fields.Integer()
    n_backlog=fields.Integer()   
    branch = fields.Char() 
    Career_option =fields.Selection(
          selection=[('placement','Placement'),('higher_education', 'Higher Education'),('family_business','Family Business'),('others', 'Others')]   
          )
    passing_year =fields.Selection(
          selection=[('2023','2023'),('2024', '2024'),('2025','2025'),('2026', '2026')]   
          )      


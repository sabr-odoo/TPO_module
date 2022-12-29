#-*- coding:utf-8 -*-

from odoo import models,fields  

class StudentStudent(models.Model):
    _name="student.student"
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
    state =fields.Selection(
          selection=[('new','New'),('confirm', 'Confirm'),('cancel','Cancel')],default="new"   
          )
    Career_option =fields.Selection(
          selection=[('placement','Placement'),('higher_education', 'Higher Education'),('family_business','Family Business'),('others', 'Others')]   
          )
    passing_year =fields.Selection(
          selection=[('pass_2023','2023'),('2024', '2024'),('2025','2025'),('2026', '2026')]   
          )  
    teacher_placement_id=fields.Many2one("teacher.placement")  
    company_placement_id=fields.Many2one("details.company",string="Company Name")
    #Resume fields
    description=fields.Text()
    onesem=fields.Integer()
    secondsem=fields.Integer()
    thirdsem=fields.Integer()
    foursem=fields.Integer()
    fivesem=fields.Integer()
    sixsem=fields.Integer()
    objective=fields.Text()
    linkedin=fields.Char()
    github=fields.Char()
    skill=fields.Text()
    technical_skill=fields.Text()
    intership=fields.Text()
    project=fields.Text()

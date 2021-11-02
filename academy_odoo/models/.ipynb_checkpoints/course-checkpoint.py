# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Descrption')
    
    level = fields.Selection(string='level',
                            selection=[('beginner','Beginner'), 
                                       ('intermediate', 'Intermediate'),
                                       ('advanced','Advanced')],
                             copy=False)
    active = fields.Boolean(string='Active', deafult=True)
# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentBase(models.Model):
    _name = 'student.base'
    _description = 'Description module for data file student_base in Odoo'

    name = fields.Char(string='Name')
    lastname = fields.Char(string='Last name')
    birth_date = fields.Date(string='Birth date')
    age = fields.Integer(string='Age')
    matricule = fields.Char(string='Matricule')
    photo = fields.Image(string='Image')



# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Description module for data file student_class in Odoo'

    name = fields.Char(string='Name')
    number = fields.Integer(String='Student number')
    stage = fields.Char(string='Stage')



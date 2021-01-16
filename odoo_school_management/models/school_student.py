# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string="Name", required=1)  # student name is required
    birth_date = fields.Date(string="Birthday")
    age = fields.Float(string="Age")
    gender = fields.Selection([
        ('man', 'Man'),
        ('woman', 'Woman'),
    ], string="Gender")
    number = fields.Integer(string="Number")
    address = fields.Text(string="Address")

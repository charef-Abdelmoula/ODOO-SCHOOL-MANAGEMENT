# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolClassroom(models.Model):
    _name = 'school.classroom'
    _description = 'School Classroom'

    name = fields.Char(string="Name")
    tables_number = fields.Integer(string="Tables Number")

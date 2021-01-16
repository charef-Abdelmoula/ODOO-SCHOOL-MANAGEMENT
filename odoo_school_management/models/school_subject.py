# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    """ _name :this name of the table going to be stored in Postgresql DB as 
    school_subject.
    _description :a brief description of your model.
    """
    name = fields.Char(string="Name")
    teacher_id = fields.Many2one('school.teacher', string="Teacher")

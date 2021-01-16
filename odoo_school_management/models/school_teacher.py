# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char(string="Name",required=1)
    age = fields.Float(string="Age")
    gender = fields.Selection([
        ('man', 'Man'),
        ('woman', 'Woman'),
    ], string="Gender")
    experience = fields.Float(string="Experience")
    address = fields.Text(string="Address")
    subject_ids = fields.One2many('school.subject', 'teacher_id', string="Subjects")

    """
    for the last field subject_ids:a teacher can teach multiple in our example.
    as we explained for One2many field we need to have a relation on the other
     model school.subject (teacher_id)
    """

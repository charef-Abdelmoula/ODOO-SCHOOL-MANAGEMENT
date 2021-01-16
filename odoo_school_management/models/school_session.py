# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolSession(models.Model):
    _name = 'school.session'
    _description = 'School Session'

    name = fields.Char(string="Name")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    duration = fields.Float(string="Duration")
    subject_id = fields.Many2one('school.subject', string="Subject")
    teacher_id = fields.Many2one('school.teacher', string="Teacher")
    classroom_id = fields.Many2one('school.classroom', string="Classroom")
    description = fields.Text("Description")


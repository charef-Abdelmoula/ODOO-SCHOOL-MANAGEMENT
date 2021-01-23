# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolTransferRequest(models.Model):
    _name = 'school.transfer.request'
    _description = 'Student transfer Request'

    name = fields.Char(string="Transfer Number", required=1)
    student_id = fields.Many2one('school.student', string="Student", required=1)
    reason = fields.Text(string="Transfer Reason", required=1)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('validated', 'Validated'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], "State", default='draft')

    def submit_request(self):
        self.write({'state': 'submitted'})

    def validate_request(self):
        self.write({'state': 'validated'})

    def accept_request(self):
        self.write({'state': 'accepted'})

    def reject_request(self):
        self.write({'state': 'rejected'})

    def reset_request_to_draft(self):
        self.write({'state': 'draft'})

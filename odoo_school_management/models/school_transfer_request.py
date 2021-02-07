# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class SchoolTransferRequest(models.Model):
    _name = 'school.transfer.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
        """Create an activity for the actual user who has validated this transfer """
        note = (
                   'This Transfer is validated, it should be approved/accepted before  %s') % (
                           fields.Date().today() + relativedelta(days=3))

        # note :the message of the activity
        # we have used relativedelta library so that we can have the date after tree days

        self.activity_schedule(
            'odoo_school_management.mail_act_transfer_decision', fields.Date().today() + relativedelta(days=3),
            note=note,
            user_id=self.env.user.id)
        """
        activity_schedule takes as parameters:
                1-the xml id of the activity type which we have defined in activities.xml file under data directory.
                2-date due of the activity.
                3-the message tro show.
                4-the user who will be assigned this activity.
            """

    def accept_request(self):
        self.write({'state': 'accepted'})
        """
        activity_feedback :Shows a feedback for user that this activity is made
        activity_unlink   : delete the activity
        """
        self.activity_feedback(
            ['odoo_school_management.mail_act_transfer_decision'])
        # self.activity_unlink(
        #     ['odoo_school_management.mail_act_transfer_decision'])

    def reject_request(self):
        self.write({'state': 'rejected'})
        self.activity_feedback(
            ['odoo_school_management.mail_act_transfer_decision'])
        # self.activity_unlink(
        #     ['odoo_school_management.mail_act_transfer_decision'])

    def reset_request_to_draft(self):
        self.write({'state': 'draft'})

from odoo import models, fields
from odoo.tools import date_utils


class AttendanceReport(models.Model):
    _inherit = 'hr.attendance'

    today = fields.Datetime.now()

    def action_send(self):
        report_list = []
        report_list.clear()
        today = fields.date.today()
        yesterday = date_utils.subtract(today, days=1)
        x = self.env['hr.attendance'].search([('check_in', '<=', today), ('check_in', '>', yesterday)])
        for i in x:
            report = {
                'check_in': i.check_in,
                'name': i.employee_id.name
            }
            report_list.append(report)
        # print(report_list)
        admin_email = self.env['ir.model.access'].search([('name', '=', 'hr.attendance.overtime.user')]).group_id.users.email
        mail_values = {
            'data': report_list,
            'admin_mail': admin_email
        }
        mail_template = self.env.ref('attendance_report.attendance_email_template')
        mail_template.with_context(mail_values).send_mail(self.id, force_send=True)

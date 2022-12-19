{
    'name': 'Attendance Report',
    'version': '15.0.1.0.0',
    'sequence': 100,
    'depends': ['base',
                'hr_attendance',
                'mail'
                ],
    'data': [
        'views/mail.xml',
        'data/cron_action.xml',
    ],
    'license': 'LGPL-3',
}

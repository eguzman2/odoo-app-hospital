{
    'name': 'Vertical Hospital',
    'summary': 'Patients & Treatments',
    'sequence': 10,
    'description': """
        Patients & Treatments
        -Manage patients & Treatments.
        -Generate PDF report
        -API to share patients data
    """,
    'category': 'Specific Industry Applications',
    'version': '15.0.1.0.0',
    'depends': ['mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menuitem.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_treatment_views.xml',
        'report/print_hospital_patients.xml',
        'views/hospital_report.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

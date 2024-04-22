from odoo import api, models, _


class HospitalPatientsReport(models.AbstractModel):
    _name = 'report.vertical_hospital.print_hospital_patients'
    _description = 'Hospital Patients Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        data = dict(data or {})
        return {
            'doc_ids': docids,
            'docs': self.env['hospital.patient'].browse(docids),
            'doc_model': 'hospital.patient',
            'data': data
        }

from odoo import api, _, fields, models


class HospitalTreatment(models.Model):
    _name = "hospital.treatment"
    _description = "Treatment"

    name = fields.Char('name', required=True)
    code = fields.Char('Treatment code')
    doctor = fields.Char('Treating Doctor')

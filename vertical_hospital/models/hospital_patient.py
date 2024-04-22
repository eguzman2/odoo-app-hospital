from odoo import api, _, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Char('Sequence', required=True)
    name = fields.Char('Name and last name', required=True)
    dni = fields.Integer('DNI', track_visibility='onchange')
    done_treatment_ids = fields.Many2many('hospital.treatment', 'patient_treatment_rel', 'patient_id', 'treatment_id', string='Done treatments')
    discharged_datetime = fields.Datetime('Discharged date and time')
    updated_datetime = fields.Datetime('Updated date and time')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('discharged', 'Discharged'),
        ('removed', 'Removed')
    ], "state", default="draft", track_visibility='onchange', required=True)


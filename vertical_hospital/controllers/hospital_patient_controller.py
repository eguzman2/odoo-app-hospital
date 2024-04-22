import json

from odoo.http import request, route, Response
from odoo import api, http, _
from werkzeug.exceptions import NotFound


class HospitalController(http.Controller):

    @http.route('/odoo-domain/pacientes/consulta/<string:sequence>', methods=['GET'], type='http', auth='none')
    def get_patient(self, sequence, **kw):
        patient_id = request.env['hospital.patient'].sudo().search([('sequence', '=', sequence)])
        if not patient_id:
            raise NotFound()
        return self._response_patient_json(patient_id)

    @api.model
    def _response_patient_json(self, patient_id):
        return Response(json.dumps({
            "seq": patient_id.sequence,
            "name": patient_id.name,
            "dni": patient_id.dni,
            "state": patient_id.state
        }), content_type='application/json;charset=utf-8', status=200)

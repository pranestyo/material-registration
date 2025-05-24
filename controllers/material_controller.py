
from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/api/materials', type='json', auth='user')
    def get_materials(self, **kwargs):
        domain = []
        if 'type' in kwargs:
            domain.append(('type', '=', kwargs['type']))
        materials = request.env['material.material'].search_read(domain)
        return materials

    @http.route('/api/materials/create', type='json', auth='user')
    def create_material(self, **kwargs):
        required_fields = ['code', 'name', 'type', 'buy_price', 'supplier_id']
        if not all(field in kwargs for field in required_fields):
            return {'error': 'Missing fields'}

        material = request.env['material.material'].create(kwargs)
        return material.read()[0]

    @http.route('/api/materials/update/<int:id>', type='json', auth='user')
    def update_material(self, id, **kwargs):
        material = request.env['material.material'].browse(id)
        if material.exists():
            material.write(kwargs)
            return {'success': True}
        return {'error': 'Material not found'}

    @http.route('/api/materials/delete/<int:id>', type='json', auth='user')
    def delete_material(self, id):
        material = request.env['material.material'].browse(id)
        if material.exists():
            material.unlink()
            return {'success': True}
        return {'error': 'Material not found'}


from odoo.tests.common import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self):
        super().setUp()
        self.partner = self.env['res.partner'].create({
            'name': 'Test Supplier',
            'supplier_rank': 1,
        })

    def test_create_material(self):
        material = self.env['material.material'].create({
            'code': 'MAT001',
            'name': 'Cotton Material',
            'type': 'cotton',
            'buy_price': 150,
            'supplier_id': self.partner.id
        })
        self.assertEqual(material.name, 'Cotton Material')

    def test_buy_price_validation(self):
        with self.assertRaises(Exception):
            self.env['material.material'].create({
                'code': 'MAT002',
                'name': 'Cheap Material',
                'type': 'jeans',
                'buy_price': 50,
                'supplier_id': self.partner.id
            })

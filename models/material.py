
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.material'
    _description = 'Material'

    code = fields.Char(string='Material Code', required=True)
    name = fields.Char(string='Material Name', required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('res.partner', string='Related Supplier', domain="[('supplier_rank', '>', 0)]", required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for rec in self:
            if rec.buy_price < 100:
                raise ValidationError('Buy price must be >= 100.')

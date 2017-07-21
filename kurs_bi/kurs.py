from scrap import currencies, kurs
from odoo import models, fields, api
class KursWizard(models.Model):
    _name = 'kurs.bi.wizard'

    currency = fields.Selection(currencies, string="Currency", required=True)
    kurs_tengah = fields.Float(string="Kurs Tengah", compute='_kurs', store=True, readonly=True)
    kurs_jual = fields.Float(string="Kurs Jual", compute='_kurs', store=True, readonly=True)
    kurs_beli = fields.Float(string="Kurs Beli", compute='_kurs', store=True, readonly=True)

    @api.one
    @api.depends('currency')
    def _kurs(self):
      if self.currency:
         currency = kurs.get(self.currency)
         if currency:
            self.kurs_jual = currency['kurs_jual']
            self.kurs_beli = currency['kurs_beli']
            self.kurs_tengah = (self.kurs_jual + self.kurs_beli) / 2

    @api.multi
    def update(self):
        currency = kurs.get(self.currency)
        currency_id = self.env['res.currency'].sudo().search([('name', '=', self.currency)], limit=1)
        if currency_id:
           self.env['res.currency.rate'].sudo().create({'currency_id': currency_id.id, 'rate': 1 / (self.kurs_tengah / currency['nilai'])})

# This file is part of the sale_invoice_grouping_by_address module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Invoice']


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'
    shipment_address = fields.Many2One('party.address', 'Shipment Address',
        domain=[('party', '=', Eval('party'))], states={
            'readonly': ~Eval('state').in_(['draft', 'validated']),
            })

    def on_change_party(self):
        super(Invoice, self).on_change_party()

        if hasattr(self, 'shipment_party'):
            delivery_address = None
            if self.party and not self.shipment_party:
                delivery_address = self.party.address_get(type='delivery')
            if self.shipment_party:
                delivery_address = self.shipment_party.address_get(type='delivery')
            self.shipment_address = delivery_address

    def _credit(self, **values):
        credit = super(Invoice, self)._credit(**values)
        credit.shipment_address = (self.shipment_address
            and self.shipment_address.id or None)
        return credit

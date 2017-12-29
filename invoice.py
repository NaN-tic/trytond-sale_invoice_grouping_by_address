# This file is part of the sale_invoice_grouping_by_address module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Invoice']
__metaclass__ = PoolMeta


class Invoice():
    __name__ = 'account.invoice'
    shipment_address = fields.Many2One('party.address', 'Shipment Address',
        domain=['OR', [('party', '=', Eval('party')),
                    ('party', '=', Eval('shipment_party'))],],
        states={'readonly': ~Eval('state').in_(['draft', 'validated']),
        },
        depends=['party', 'state'])

    @fields.depends('party')
    def on_change_party(self):
        super(Invoice, self).on_change_party()

        self.shipment_address = None
        if self.party:
            delivery_address = self.party.address_get(type='delivery')
            if delivery_address:
                self.shipment_address = delivery_address

    def _credit(self):
        res = super(Invoice, self)._credit()
        res['shipment_address'] = (self.shipment_address
            and self.shipment_address.id or None)
        return res

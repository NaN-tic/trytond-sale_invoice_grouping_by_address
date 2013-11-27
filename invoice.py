#This file is part of the sale_invoice_grouping_by_address module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Invoice']
__metaclass__ = PoolMeta


class Invoice():
    __name__ = 'account.invoice'
    shipment_address = fields.Many2One('party.address', 'Shipment Address',
        domain=[('party', '=', Eval('party'))], states={
            'readonly': ~Eval('state').in_(['draft', 'validated']),
            },
        depends=['party', 'state'])

    def on_change_party(self):
        res = super(Invoice, self).on_change_party()
        res['shipment_address'] = None
        res['shipment_address.rec_name'] = None
        if self.party:
            delivery_address = self.party.address_get(type='delivery')
            if delivery_address:
                res['shipment_address'] = delivery_address.id
                res['shipment_address.rec_name'] = delivery_address.rec_name
        return res

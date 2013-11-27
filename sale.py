#This file is part of the sale_invoice_grouping_by_address module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    @property
    def _invoice_grouping_fields(self):
        res = super(Sale, self)._invoice_grouping_fields
        if self.shipment_address:
            if (self.shipment_address.party.sale_invoice_grouping_method ==
                    'shipment_address'):
                res = [x for x in res if x != 'invoice_address']
                res.append('shipment_address')
                res = tuple(res)
        return res

    def _get_grouped_invoice_domain(self, invoice):
        invoice_domain = super(Sale, self)._get_grouped_invoice_domain(invoice)
        if self.shipment_address:
            if (self.shipment_address.party.sale_invoice_grouping_method ==
                    'shipment_address'):
                invoice_domain[
                    invoice_domain.index(('shipment_address', '=', None))
                    ] = ('shipment_address', '=', self.shipment_address)
        return invoice_domain

    def _get_invoice_sale(self, invoice_type):
        invoice = super(Sale, self)._get_invoice_sale(invoice_type)
        if not hasattr(invoice, 'shipment_address') and self.shipment_address:
            invoice.shipment_address = self.shipment_address
        return invoice

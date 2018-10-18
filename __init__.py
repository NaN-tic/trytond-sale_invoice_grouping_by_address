# This file is part of the sale_invoice_grouping_by_address module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import invoice
from . import sale
from . import party


def register():
    Pool.register(
        invoice.Invoice,
        sale.Sale,
        party.Party,
        module='sale_invoice_grouping_by_address', type_='model')

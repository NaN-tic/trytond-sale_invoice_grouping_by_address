# This file is part of the sale_invoice_grouping_by_address module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Party']


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    @classmethod
    def __setup__(cls):
        super(Party, cls).__setup__()
        if (('shipment_address', 'By shipment address') not in
                cls.sale_invoice_grouping_method._field.selection):
            cls.sale_invoice_grouping_method._field.selection.append(
                    ('shipment_address', 'By shipment address'),
                    )

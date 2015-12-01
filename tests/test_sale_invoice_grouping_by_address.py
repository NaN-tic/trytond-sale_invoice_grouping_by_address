# This file is part of the sale_invoice_grouping_by_address module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleInvoiceGroupingByAddressTestCase(ModuleTestCase):
    'Test Sale Invoice Grouping By Address module'
    module = 'sale_invoice_grouping_by_address'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleInvoiceGroupingByAddressTestCase))
    return suite
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This file is part of the sale_invoice_grouping_by_address module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class SaleInvoiceGroupingByAddressTestCase(unittest.TestCase):
    'Test Sale Invoice Grouping By Address module'

    def setUp(self):
        trytond.tests.test_tryton.install_module(
            'sale_invoice_grouping_by_address')

    def test0005views(self):
        'Test views'
        test_view('sale_invoice_grouping_by_address')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleInvoiceGroupingByAddressTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

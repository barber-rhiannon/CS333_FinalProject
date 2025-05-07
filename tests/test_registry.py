# Author: Rhiannon Barber
# Date: May 6
# CS 333: FINAL PROJECT --

import unittest
from converter.registry import CurrencyRegistry
from converter.currency import CurrencyError

class TestCurrencyRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = CurrencyRegistry()

    def test_add_and_get_currency(self):
        self.registry.add_currency("GBP", 1.3)
        gbp = self.registry.get_currency("GBP")
        self.assertEqual(gbp.rate_to_usd, 1.3)

    def test_update_currency(self):
        self.registry.add_currency("AUD", 0.75)
        self.registry.update_currency("AUD", 0.77)
        self.assertEqual(self.registry.get_currency("AUD").rate_to_usd, 0.77)

    def test_remove_currency(self):
        self.registry.add_currency("CAD", 0.8)
        self.registry.remove_currency("CAD")
        with self.assertRaises(CurrencyError):
            self.registry.get_currency("CAD")

    def test_add_duplicate_currency_raises(self):
        self.registry.add_currency("USD", 1.0)
        with self.assertRaises(CurrencyError):
            self.registry.add_currency("USD", 1.0)

    def test_get_nonexistent_currency(self):
        with self.assertRaises(CurrencyError):
            self.registry.get_currency("NON")

    def test_update_nonexistent_currency(self):
        with self.assertRaises(CurrencyError):
            self.registry.update_currency("ZAR", 0.1)

    def test_remove_nonexistent_currency(self):
        with self.assertRaises(CurrencyError):
            self.registry.remove_currency("XYZ")

    def test_case_sensitivity_currency_code(self):
        self.registry.add_currency("usd", 1.0)
        with self.assertRaises(CurrencyError):
            self.registry.get_currency("USD")

# Author: Rhiannon Barber
# Date: May 6
# CS 333: FINAL PROJECT

import unittest
from converter.registry import CurrencyRegistry
from converter.converter import CurrencyConverter
from converter.currency import CurrencyError

class TestIntegrationFlow(unittest.TestCase):
    def setUp(self):
        self.registry = CurrencyRegistry()
        self.registry.add_currency("USD", 1.0)
        self.registry.add_currency("EUR", 1.2)
        self.registry.add_currency("JPY", 0.007)
        self.converter = CurrencyConverter(self.registry)

    def test_conversion_after_update(self):
        self.registry.update_currency("EUR", 1.5)
        result = self.converter.convert(100, "USD", "EUR")
        self.assertAlmostEqual(result, 66.67, places=2)

    def test_conversion_then_rate_change(self):
        initial = self.converter.convert(100, "USD", "EUR")
        self.registry.update_currency("EUR", 1.0)
        updated = self.converter.convert(100, "USD", "EUR")
        self.assertNotEqual(initial, updated)

    def test_conversion_after_currency_removed(self):
        self.registry.remove_currency("EUR")
        with self.assertRaises(CurrencyError):
            self.converter.convert(100, "USD", "EUR")

    def test_add_then_convert(self):
        self.registry.add_currency("INR", 0.012)
        result = self.converter.convert(100, "USD", "INR")
        self.assertEqual(result, round(100 / 0.012, 2))

    def test_usd_to_usd_integration(self):
        result = self.converter.convert(123.45, "USD", "USD")
        self.assertEqual(result, 123.45)

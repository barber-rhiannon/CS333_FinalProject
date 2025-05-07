import unittest
from converter.registry import CurrencyRegistry
from converter.converter import CurrencyConverter
from converter.currency import CurrencyError

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.registry = CurrencyRegistry()
        self.registry.add_currency("USD", 1.0)
        self.registry.add_currency("EUR", 1.2)
        self.registry.add_currency("JPY", 0.007)
        self.converter = CurrencyConverter(self.registry)

    def test_usd_to_eur(self):
        result = self.converter.convert(100, "USD", "EUR")
        self.assertAlmostEqual(result, 83.33, places=2)

    def test_eur_to_jpy(self):
        result = self.converter.convert(50, "EUR", "JPY")
        self.assertTrue(result > 8000)

    def test_invalid_currency(self):
        with self.assertRaises(CurrencyError):
            self.converter.convert(100, "USD", "XXX")

    def test_negative_amount(self):
        with self.assertRaises(CurrencyError):
            self.converter.convert(-10, "EUR", "USD")

    def test_convert_zero_amount(self):
        result = self.converter.convert(0, "USD", "EUR")
        self.assertEqual(result, 0)

    def test_convert_same_currency(self):
        result = self.converter.convert(50, "USD", "USD")
        self.assertEqual(result, 50)

    def test_large_value_conversion(self):
        result = self.converter.convert(1_000_000, "EUR", "JPY")
        self.assertTrue(result > 100_000_000)

    def test_float_precision(self):
        result = self.converter.convert(33.33, "USD", "EUR")
        self.assertIsInstance(result, float)

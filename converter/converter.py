# Author: Rhiannon Barber
# Date: May 6
# CS 333: FINAL PROJECT


from .registry import CurrencyRegistry
from .currency import CurrencyError

class CurrencyConverter:
    def __init__(self, registry: CurrencyRegistry):
        self.registry = registry

    def convert(self, amount: float, from_code: str, to_code: str) -> float:
        if amount < 0:
            raise CurrencyError("Amount must be non-negative.")

        from_currency = self.registry.get_currency(from_code)
        to_currency = self.registry.get_currency(to_code)

        amount_in_usd = amount * from_currency.rate_to_usd
        converted = amount_in_usd / to_currency.rate_to_usd

        return round(converted, 2)

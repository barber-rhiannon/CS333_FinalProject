from .currency import Currency, CurrencyError

class CurrencyRegistry:
    def __init__(self):
        self._currencies = {}

    def add_currency(self, code: str, rate_to_usd: float):
        if code in self._currencies:
            raise CurrencyError(f"Currency '{code}' already exists.")
        self._currencies[code] = Currency(code, rate_to_usd)

    def update_currency(self, code: str, new_rate: float):
        if code not in self._currencies:
            raise CurrencyError(f"Currency '{code}' not found.")
        self._currencies[code].rate_to_usd = new_rate

    def remove_currency(self, code: str):
        if code not in self._currencies:
            raise CurrencyError(f"Currency '{code}' not found.")
        del self._currencies[code]

    def get_currency(self, code: str) -> Currency:
        if code not in self._currencies:
            raise CurrencyError(f"Currency '{code}' not found.")
        return self._currencies[code]

# Author: Rhiannon Barber
# Date: May 6
# CS 333: FINAL PROJECT

from dataclasses import dataclass

@dataclass
class Currency:
    code: str
    rate_to_usd: float

class CurrencyError(Exception):
    pass

from enum import Enum


# Understands the exchange rate between currencies as of April 3, 2023.
class Currency(Enum):
    USD = 1
    TWD = 30.4800
    CAD = 1.3435
    CNY = 6.8776
    JPY = 132.3500
    KRW = 1316.3800
    GBP = 1.2403
    EUR = 1.0891


def exchange_to(original_crrency, amount, new_currency):
    return amount / original_crrency.value * new_currency.value

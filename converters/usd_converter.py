# Универсальный конвертер USD в любую валюту.

from converters.currency_converter import CurrencyConverter

class UsdConverter(CurrencyConverter):
    def __init__(self, rates: Dict[str, float], target_currency: str):
        self.rates = rates
        self.target_currency = target_currency

    def convert(self, amount: float) -> float:
        return amount * self.rates.get(self.target_currency, 0.0)
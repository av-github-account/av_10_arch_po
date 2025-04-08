from converters import UsdConverter
from converters.currency_rate_service import CurrencyRateService

def main():
    amount = float(input("Введите значение в USD: \n"))
    service = CurrencyRateService()
    rates = service.get_rates()

    converters = {
        'RUB': UsdConverter(rates, 'RUB'),
        'EUR': UsdConverter(rates, 'EUR'),
        'GBP': UsdConverter(rates, 'GBP'),
        'CNY': UsdConverter(rates, 'CNY'),
    }

    for currency, converter in converters.items():
        print(f"{amount} USD to {currency}: {converter.convert(amount):.2f}")

if __name__ == "__main__":
    main()
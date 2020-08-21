class CountryCurrency(object):
    def __init__(self, country: str, currency: str, currency_code: str):
        self.country = country
        self.currency = currency
        self.currency_code = currency_code

    def __str__(self) -> str:
        return 'CurrencyModel(country: {}, currency: {}, currency_code: {})'.format(
            self.country,
            self.currency,
            self.currency_code
        )

    def __repr__(self):
        return 'CurrencyModel({}, {}, {})'.format(
            self.country,
            self.currency,
            self.currency_code
        )

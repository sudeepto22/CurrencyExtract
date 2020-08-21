class Currency(object):
    def __init__(self, currency_code: str, value: float):
        self.currency_code = currency_code
        self.value = value

    def __str__(self) -> str:
        return 'CurrencyModel(currency_code: {}, value: {})'.format(
            self.currency_code,
            self.value
        )

    def __repr__(self):
        return 'CurrencyModel({}, {})'.format(
            self.currency_code,
            self.value
        )

from enum import Enum


class DBConfig(Enum):
    HOST: str = '<HOST>'
    USER: str = '<USERNAME>'
    PASSWORD: str = '<PASSWORD>'

    DATABASE: str = 'currency_extract'

    TABLE_CURRENCY: str = 'currency_tbl'
    TABLE_CURRENCY_HISTORY: str = 'currency_history_tbl'
    TABLE_COUNTRY_CURRENCY: str = 'country_currency_tbl'

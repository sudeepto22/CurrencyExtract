from enum import Enum


class DBConfig(Enum):
    HOST: str = 'localhost'
    USER: str = 'sudeepto'
    PASSWORD: str = 'Sudeepto22$'

    DATABASE: str = 'currency_extract'

    TABLE_CURRENCY: str = 'currency_tbl'
    TABLE_CURRENCY_HISTORY: str = 'currency_history_tbl'
    TABLE_COUNTRY_CURRENCY: str = 'country_currency_tbl'

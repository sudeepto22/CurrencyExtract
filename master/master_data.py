from typing import List, Any

import pandas as pd

from model.country_currency_model import CountryCurrency


class MasterData(object):
    def __init__(self):
        self.df_country_currency: pd.DataFrame = pd.read_csv('assets/currency_country_mapping.csv')

    def get_data(self) -> List[CountryCurrency]:
        country_currency_list: Any = self.df_country_currency.values.tolist()
        data: List[CountryCurrency] = list()
        for country_currency in country_currency_list:
            data.append(CountryCurrency(
                country=country_currency[0],
                currency=country_currency[1],
                currency_code=country_currency[2]
            ))
        return data

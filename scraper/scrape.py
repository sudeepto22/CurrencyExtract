from typing import List, Any

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from config.api_config import APIConfig
from model.currency_model import Currency


class CurrencyScrape(object):
    def __init__(self):
        self.df_country_currency: pd.DataFrame = pd.read_csv('assets/currency_country_mapping.csv')
        self.currencies: list = self.df_country_currency['currency_code'].unique()

    def scrape(self) -> list:
        """
        Start the scraping activity for all currency_codes
        Return a list of currency_code and INR value of such currency code

        :return: currency_value: list
        """
        currency_value: list = list()
        for currency in tqdm(self.currencies):
            currency: str = currency.replace('\n', "")
            if currency == 'INR':
                currency_value.append({
                    'currency_code': currency,
                    'value': 1
                })
                continue
            url: str = APIConfig.URL.value.format(currency)

            res = requests.get(url=url)
            soup: BeautifulSoup = BeautifulSoup(res.text, features='html.parser')

            classes: list = APIConfig.DIV_CLASSES.value

            data: list = soup.findAll('div', {'class': classes[0]})
            if data:
                data: str = data[-1].text
                currency_value.append({
                    'currency_code': currency,
                    'value': data.split()[0]
                })
            else:
                data: list = soup.findAll("div", {"class": classes[1]})
                if data:
                    data: str = data[1].text
                    currency_value.append({
                        'currency_code': currency,
                        'value': data.split()[0]
                    })

        return currency_value

    def get_data(self) -> List[Currency]:
        """
        Execute the scrape method to get the data for all currency_codes
        Once we get the data, convert it to DataFrame
        Create a list of Currency Object and return it

        :return: data: List[Currency]
        """
        currency_value: list = self.scrape()
        df_currency_value: pd.DataFrame = pd.DataFrame(currency_value)
        currency_list: Any = df_currency_value.values.tolist()
        data: List[Currency] = list()
        for currency in currency_list:
            data.append(Currency(
                currency_code=currency[0],
                value=currency[1]
            ))
        return data

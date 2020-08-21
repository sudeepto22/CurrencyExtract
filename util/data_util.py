from typing import List

from model.country_currency_model import CountryCurrency
from model.currency_model import Currency


class DataUtil(object):
    @staticmethod
    def list_to_string_currency(data: List[Currency]) -> str:
        """
        Convert list of currency into SQL compatible string

        :param data: List[Currency]
        :return: str
        """
        temp_list: list = list()
        for d in data:
            temp_str = '("{}", {})'.format(
                d.currency_code,
                d.value
            )
            temp_list.append(temp_str)
        return ','.join(temp_list)

    @staticmethod
    def list_to_string_country_currency(data: List[CountryCurrency]) -> str:
        """
        Convert list of currency into SQL compatible string

        :param data: List[Currency]
        :return: str
        """
        temp_list: list = list()
        for d in data:
            temp_str = '("{}", "{}", "{}")'.format(
                d.country,
                d.currency,
                d.currency_code
            )
            temp_list.append(temp_str)
        return ','.join(temp_list)

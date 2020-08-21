from typing import List

import mysql.connector

from config.db_config import DBConfig
from model.country_currency_model import CountryCurrency
from model.currency_model import Currency
from util.data_util import DataUtil


class DBHelper(object):
    def __init__(self):
        self.database_connection = mysql.connector.connect(
            host=DBConfig.HOST.value,
            user=DBConfig.USER.value,
            password=DBConfig.PASSWORD.value
        )

    def insert(self, data: List[Currency]):
        """
        Transform the data so that it is SQL query compatible
        REPLACE the data in CURRENCY table
        INSERT the data in CURRENCY_HISTORY table

        :param data: List[Currency]
        :return: None
        """
        cursor = self.database_connection.cursor()
        modes: dict = {
            'REPLACE': DBConfig.TABLE_CURRENCY.value,
            'INSERT': DBConfig.TABLE_CURRENCY_HISTORY.value
        }
        for mode, table in modes.items():
            query = '{} INTO {}.{} (currency_code, value) VALUES {}'.format(
                mode,
                DBConfig.DATABASE.value,
                table,
                DataUtil.list_to_string_currency(data=data)
            )
            cursor.execute(query)

        self.database_connection.commit()

    def insert_country_currency(self, data: List[CountryCurrency]):
        """
        Transform the data so that it is SQL query compatible
        REPLACE the data in CURRENCY table
        INSERT the data in CURRENCY_HISTORY table

        :param data: List[Currency]
        :return: None
        """
        cursor = self.database_connection.cursor()
        query = 'REPLACE INTO {}.{} (country, currency, currency_code) VALUES {}'.format(
            DBConfig.DATABASE.value,
            DBConfig.TABLE_COUNTRY_CURRENCY.value,
            DataUtil.list_to_string_country_currency(data=data)
        )
        cursor.execute(query)

        self.database_connection.commit()

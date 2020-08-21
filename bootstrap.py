from db_util.db_helper import DBHelper
from master.master_data import MasterData
from scraper.scrape import CurrencyScrape


def execute():
    currency_scrape = CurrencyScrape()
    data = currency_scrape.get_data()

    db_helper = DBHelper()
    db_helper.insert(data=data)


def execute_master():
    master_data = MasterData()
    data = master_data.get_data()

    db_helper = DBHelper()
    db_helper.insert_country_currency(data=data)


if __name__ == '__main__':
    execute()

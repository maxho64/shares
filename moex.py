import json

import requests

from TradesParser import TradesParser
from TransactionsParser import TransactionsParser

API_ENDPOINT = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities.json'

MARKET_DATA_KEY = "marketdata"
MARKET_DATA_COLUMNS_INFO_KEY = "columns"
MARKET_DATA_DATA_INFO_KEY = "data"

r = requests.get(API_ENDPOINT)

market = json.loads(r.content.decode())

marketColumns = market[MARKET_DATA_KEY][MARKET_DATA_COLUMNS_INFO_KEY]
marketData = market[MARKET_DATA_KEY][MARKET_DATA_DATA_INFO_KEY]


def reshapeMarketShares(data, columns):
    market_shares = list()

    for share in data:
        new_share = dict()
        for i, column in enumerate(columns):
            new_share[column] = share[i]
        market_shares.append(new_share)

    return market_shares


market_shares = reshapeMarketShares(marketData, marketColumns)

for market_share in market_shares:
    if market_share['SECID'] == "MOEX":
        pass

parser = TradesParser("trades.xls")
parser.parse()
trades = parser.get_data()

parser = TransactionsParser("transactions.xls")
parser.parse()
dividends = parser.get_data()


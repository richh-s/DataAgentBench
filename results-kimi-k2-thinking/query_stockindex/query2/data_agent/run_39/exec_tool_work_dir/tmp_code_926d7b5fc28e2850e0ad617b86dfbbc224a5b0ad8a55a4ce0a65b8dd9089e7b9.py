code = """import json

# Storage keys from previous calls
meta_data = [{"Exchange": "New York Stock Exchange", "Currency": "USD"}, {"Exchange": "NASDAQ", "Currency": "USD"}, {"Exchange": "Hong Kong Stock Exchange", "Currency": "HKD"}, {"Exchange": "Shanghai Stock Exchange", "Currency": "CNY"}, {"Exchange": "Tokyo Stock Exchange", "Currency": "JPY"}, {"Exchange": "Euronext", "Currency": "EUR"}, {"Exchange": "Shenzhen Stock Exchange", "Currency": "CNY"}, {"Exchange": "Toronto Stock Exchange", "Currency": "CAD"}, {"Exchange": "National Stock Exchange of India", "Currency": "INR"}, {"Exchange": "Frankfurt Stock Exchange", "Currency": "EUR"}, {"Exchange": "Korea Exchange", "Currency": "KRW"}, {"Exchange": "SIX Swiss Exchange", "Currency": "CHF"}, {"Exchange": "Taiwan Stock Exchange", "Currency": "TWD"}, {"Exchange": "Johannesburg Stock Exchange", "Currency": "ZAR"}]

indices_list = [{"Index": "000001.SS"}, {"Index": "399001.SZ"}, {"Index": "GDAXI"}, {"Index": "GSPTSE"}, {"Index": "HSI"}, {"Index": "IXIC"}, {"Index": "J203.JO"}, {"Index": "N100"}, {"Index": "N225"}, {"Index": "NSEI"}, {"Index": "NYA"}, {"Index": "SSMI"}, {"Index": "TWII"}]

# Map exchanges to their likely indices based on common knowledge
exchange_to_indices = {
    "New York Stock Exchange": ["NYA"],  # NYSE Composite
    "NASDAQ": ["IXIC"],  # NASDAQ Composite
    "Toronto Stock Exchange": ["GSPTSE"],  # S&P/TSX Composite
}

# Identify North American exchanges
north_american_exchanges = [
    "New York Stock Exchange",
    "NASDAQ", 
    "Toronto Stock Exchange"
]

print("__RESULT__:")
print(json.dumps({
    "north_american_exchanges": north_american_exchanges,
    "exchange_to_indices": exchange_to_indices
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)

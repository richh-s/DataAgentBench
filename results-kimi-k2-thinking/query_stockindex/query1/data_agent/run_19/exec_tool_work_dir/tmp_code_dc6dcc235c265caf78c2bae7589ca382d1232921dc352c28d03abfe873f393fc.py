code = """# Load the exchange info and prepare mapping from exchanges to indices
exchange_info = [
    {"Exchange": "New York Stock Exchange", "Currency": "USD"},
    {"Exchange": "NASDAQ", "Currency": "USD"},
    {"Exchange": "Hong Kong Stock Exchange", "Currency": "HKD"},
    {"Exchange": "Shanghai Stock Exchange", "Currency": "CNY"},
    {"Exchange": "Tokyo Stock Exchange", "Currency": "JPY"},
    {"Exchange": "Euronext", "Currency": "EUR"},
    {"Exchange": "Shenzhen Stock Exchange", "Currency": "CNY"},
    {"Exchange": "Toronto Stock Exchange", "Currency": "CAD"},
    {"Exchange": "National Stock Exchange of India", "Currency": "INR"},
    {"Exchange": "Frankfurt Stock Exchange", "Currency": "EUR"},
    {"Exchange": "Korea Exchange", "Currency": "KRW"},
    {"Exchange": "SIX Swiss Exchange", "Currency": "CHF"},
    {"Exchange": "Taiwan Stock Exchange", "Currency": "TWD"},
    {"Exchange": "Johannesburg Stock Exchange", "Currency": "ZAR"}
]

# Map exchanges to their major index symbols based on the hint
exchange_to_index = {
    "Hong Kong Stock Exchange": "HSI",
    "Shanghai Stock Exchange": "000001.SS",
    "Tokyo Stock Exchange": "N225",
    "Shenzhen Stock Exchange": "399001.SZ",
    "National Stock Exchange of India": "NSEI",
    "Taiwan Stock Exchange": "TWII"
}

# Filter for Asia region exchanges
asia_exchanges = [
    "Hong Kong Stock Exchange",      # HSI
    "Shanghai Stock Exchange",      # 000001.SS
    "Tokyo Stock Exchange",         # N225
    "Shenzhen Stock Exchange",      # 399001.SZ
    "National Stock Exchange of India",  # NSEI
    "Taiwan Stock Exchange"         # TWII
]

asia_indices = [exchange_to_index[exch] for exch in asia_exchanges]
print("__RESULT__:")
print(str(asia_indices))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)

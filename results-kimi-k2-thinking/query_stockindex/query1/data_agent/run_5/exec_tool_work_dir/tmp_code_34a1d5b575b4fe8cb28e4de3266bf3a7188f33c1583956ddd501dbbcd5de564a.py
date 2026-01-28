code = """# Access the index info data
index_info = locals()['var_functions.query_db:5']

# Access distinct index symbols
index_symbols = locals()['var_functions.query_db:9']

# Identify Asia-based exchanges based on geographic knowledge
asia_exchanges = [
    "Tokyo Stock Exchange",
    "Hong Kong Stock Exchange", 
    "Shanghai Stock Exchange",
    "Shenzhen Stock Exchange",
    "National Stock Exchange of India",
    "Korea Exchange",
    "Taiwan Stock Exchange"
]

# Manually map exchanges to their primary index symbols
exchange_to_index = {
    "Tokyo Stock Exchange": "N225",
    "Hong Kong Stock Exchange": "HSI",
    "Shanghai Stock Exchange": "000001.SS",
    "Shenzhen Stock Exchange": "399001.SZ",
    "National Stock Exchange of India": "NSEI",
    "Korea Exchange": "KS11",  # This might be KOSPI 200 or similar
    "Taiwan Stock Exchange": "TWII"
}

# Filter for indices that exist in our dataset
available_indices = [idx['Index'] for idx in index_symbols]
asia_indices_filtered = {exchange: symbol for exchange, symbol in exchange_to_index.items() 
                        if symbol in available_indices or symbol.replace('.JO', '.JO') in available_indices}

# Print the mapping
result = []
for exchange, symbol in exchange_to_index.items():
    status = "Available" if (symbol in available_indices or symbol.replace('.JO', '.JO') in available_indices) else "Not in dataset"
    result.append({"exchange": exchange, "index_symbol": symbol, "status": status})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}]}

exec(code, env_args)

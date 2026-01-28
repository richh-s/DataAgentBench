code = """import json

# Create Exchange to Index mapping based on geographic knowledge
exchange_to_index = {
    'Tokyo Stock Exchange': 'N225',  # Nikkei 225
    'Hong Kong Stock Exchange': 'HSI',  # Hang Seng Index
    'Shanghai Stock Exchange': '000001.SS',  # SSE Composite Index
    'Shenzhen Stock Exchange': '399001.SZ',  # SZSE Component Index
    'National Stock Exchange of India': 'NSEI',  # NIFTY 50
    'Korea Exchange': '^KS11',  # KOSPI Composite
    'Taiwan Stock Exchange': 'TWII',  # Taiwan Weighted Index
    'Johannesburg Stock Exchange': 'J203.JO'  # JSE Top 40
}

# Asia region exchanges
asia_exchanges = [
    'Tokyo Stock Exchange',
    'Hong Kong Stock Exchange', 
    'Shanghai Stock Exchange',
    'Shenzhen Stock Exchange',
    'National Stock Exchange of India',
    'Korea Exchange',
    'Taiwan Stock Exchange'
]

# Get Asia indices
asia_indices = [exchange_to_index[exch] for exch in asia_exchanges]

print('__RESULT__:')
print(json.dumps({'asia_indices': asia_indices}))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

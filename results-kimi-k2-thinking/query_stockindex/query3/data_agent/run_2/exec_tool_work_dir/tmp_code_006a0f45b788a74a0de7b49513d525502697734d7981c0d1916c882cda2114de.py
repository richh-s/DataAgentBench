code = """# Mapping index symbols to exchanges and countries
index_mapping = {
    '000001.SS': {'Exchange': 'Shanghai Stock Exchange', 'Country': 'China'},
    '399001.SZ': {'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China'},
    'GDAXI': {'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany'},
    'GSPTSE': {'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada'},
    'HSI': {'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong'},
    'IXIC': {'Exchange': 'NASDAQ', 'Country': 'United States'},
    'J203.JO': {'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa'},
    'N100': {'Exchange': 'Euronext', 'Country': 'Netherlands/Belgium/France'},
    'N225': {'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan'},
    'NSEI': {'Exchange': 'National Stock Exchange of India', 'Country': 'India'},
    'NYA': {'Exchange': 'New York Stock Exchange', 'Country': 'United States'},
    'SSMI': {'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland'},
    'TWII': {'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan'}
}

print('__RESULT__:')
print(list(index_mapping.keys()))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

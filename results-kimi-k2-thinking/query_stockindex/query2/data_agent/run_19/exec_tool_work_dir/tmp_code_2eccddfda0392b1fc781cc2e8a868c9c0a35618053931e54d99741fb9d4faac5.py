code = """import json

# Access the stored results
exchange_data = locals()['var_functions.query_db:2']
index_data = locals()['var_functions.query_db:6']

# Extract exchanges and indices
exchanges = [item['Exchange'] for item in exchange_data]
indices = [item['Index'] for item in index_data]

# Map North American exchanges to their indices
north_american_map = {
    'New York Stock Exchange': 'NYA',
    'NASDAQ': 'IXIC',
    'Toronto Stock Exchange': 'GSPTSE'
}

result = []
for exchange, index in north_american_map.items():
    if exchange in exchanges and index in indices:
        result.append({'exchange': exchange, 'index': index})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min(Date)': '2018-01-05 00:00:00', 'max(Date)': '2018-12-21 00:00:00', 'total_days': '84'}, {'Index': '399001.SZ', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-25 00:00:00', 'total_days': '76'}, {'Index': 'GDAXI', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '98'}, {'Index': 'GSPTSE', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '86'}, {'Index': 'HSI', 'min(Date)': '2018-01-05 00:00:00', 'max(Date)': '2018-12-21 00:00:00', 'total_days': '85'}, {'Index': 'IXIC', 'min(Date)': '2018-01-02 00:00:00', 'max(Date)': '2018-12-13 00:00:00', 'total_days': '75'}, {'Index': 'J203.JO', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-28 00:00:00', 'total_days': '81'}, {'Index': 'N100', 'min(Date)': '2018-01-12 00:00:00', 'max(Date)': '2018-12-07 00:00:00', 'total_days': '67'}, {'Index': 'N225', 'min(Date)': '2018-01-11 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '74'}, {'Index': 'NSEI', 'min(Date)': '2018-01-08 00:00:00', 'max(Date)': '2018-12-27 00:00:00', 'total_days': '78'}, {'Index': 'NYA', 'min(Date)': '2018-01-09 00:00:00', 'max(Date)': '2018-12-20 00:00:00', 'total_days': '78'}, {'Index': 'SSMI', 'min(Date)': '2018-01-04 00:00:00', 'max(Date)': '2018-12-28 00:00:00', 'total_days': '93'}, {'Index': 'TWII', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-24 00:00:00', 'total_days': '78'}]}

exec(code, env_args)

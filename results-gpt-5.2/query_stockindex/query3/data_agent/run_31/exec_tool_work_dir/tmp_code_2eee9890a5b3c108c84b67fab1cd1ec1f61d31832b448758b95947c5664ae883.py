code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_XUB9Rr8yWwjXVxVBulsJ5oGy)
# fill missing country mappings
fill = {
    'IXIC':'United States',
    '^IXIC':'United States',
    'NSEI':'India',
    '^NSEI':'India',
    'GDAXI':'Germany',
    '^GDAXI':'Germany',
    'TWII':'Taiwan',
    '^TWII':'Taiwan'
}
top5['Country'] = top5.apply(lambda r: fill.get(r['Index'], r['Country']), axis=1)

print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_QOBVxFcpoxbXBm4Ylg6ascjW': 'file_storage/call_QOBVxFcpoxbXBm4Ylg6ascjW.json', 'var_call_hHa6C9Szwj2YXan7RZNOSlz5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_XUB9Rr8yWwjXVxVBulsJ5oGy': [{'Index': 'IXIC', 'Country': None, 'total_return_multiple': 4.822, 'months_invested': 257, 'last_date': '2021-05-27'}, {'Index': 'NSEI', 'Country': None, 'total_return_multiple': 2.3609, 'months_invested': 165, 'last_date': '2021-05-31'}, {'Index': 'GDAXI', 'Country': None, 'total_return_multiple': 2.3475, 'months_invested': 257, 'last_date': '2021-05-31'}, {'Index': '399001.SZ', 'Country': 'China', 'total_return_multiple': 2.3445, 'months_invested': 258, 'last_date': '2021-06-02'}, {'Index': 'TWII', 'Country': None, 'total_return_multiple': 2.2374, 'months_invested': 257, 'last_date': '2021-05-26'}]}

exec(code, env_args)

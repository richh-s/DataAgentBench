code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_UgLBXNKQMN22CS7NBz7ONuMp)

# map index symbols to exchange/country (inferred)
map_idx = {
    'IXIC': {'Exchange':'NASDAQ', 'Country':'United States'},
    'NYA': {'Exchange':'New York Stock Exchange', 'Country':'United States'},
    'GDAXI': {'Exchange':'Frankfurt Stock Exchange', 'Country':'Germany'},
    '399001.SZ': {'Exchange':'Shenzhen Stock Exchange', 'Country':'China'},
    '000001.SS': {'Exchange':'Shanghai Stock Exchange', 'Country':'China'},
    'N225': {'Exchange':'Tokyo Stock Exchange', 'Country':'Japan'},
    'HSI': {'Exchange':'Hong Kong Stock Exchange', 'Country':'Hong Kong'},
    'GSPTSE': {'Exchange':'Toronto Stock Exchange', 'Country':'Canada'},
    'NSEI': {'Exchange':'National Stock Exchange of India', 'Country':'India'},
    'SSMI': {'Exchange':'SIX Swiss Exchange', 'Country':'Switzerland'},
    'TWII': {'Exchange':'Taiwan Stock Exchange', 'Country':'Taiwan'},
    'N100': {'Exchange':'Euronext', 'Country':'Europe (Euronext)'},
    'J203.JO': {'Exchange':'Johannesburg Stock Exchange', 'Country':'South Africa'},
}

meta = []
for idx in top5['Index']:
    m = map_idx.get(idx, {'Exchange':None,'Country':None})
    meta.append(m)
meta_df = pd.DataFrame(meta)

out = pd.concat([top5[['Index','overall_return_multiple']], meta_df], axis=1)
out['overall_return_multiple'] = out['overall_return_multiple'].astype(float)
out = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_IQw038LXdeVI95KVq3Mdzg2F': ['index_info'], 'var_call_aYQMZRH4VMisJJFJwPksBzAv': ['index_trade'], 'var_call_zxM3mfHEjBOGwDFynqF5e7Lg': [{'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}], 'var_call_KwRVe1RvsF0ea8b5VZVKCHUL': 'file_storage/call_KwRVe1RvsF0ea8b5VZVKCHUL.json', 'var_call_UgLBXNKQMN22CS7NBz7ONuMp': [{'Index': 'IXIC', 'overall_return_multiple': 4.831290448090858, 'months_invested': 257, 'last_date': '2021-05-28 00:00:00'}, {'Index': 'GDAXI', 'overall_return_multiple': 2.3600544673131734, 'months_invested': 257, 'last_date': '2021-05-25 00:00:00'}, {'Index': '399001.SZ', 'overall_return_multiple': 2.3566160880793254, 'months_invested': 257, 'last_date': '2021-05-27 00:00:00'}, {'Index': 'NSEI', 'overall_return_multiple': 2.332756497988608, 'months_invested': 165, 'last_date': '2021-05-28 00:00:00'}, {'Index': 'TWII', 'overall_return_multiple': 2.2983279471195175, 'months_invested': 257, 'last_date': '2021-05-31 00:00:00'}], 'var_call_lVkuerJFi6jqmvigm7RWyzBk': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

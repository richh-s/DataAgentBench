code = """import json
recs = var_call_MxJyHIi9khWWrlxUAh1kkDY3
# fix mapping for symbols without caret in dataset
country_map = {
    'GSPC':'United States','IXIC':'United States','DJI':'United States',
    'N225':'Japan','HSI':'Hong Kong','000001.SS':'China','399001.SZ':'China',
    'FTSE':'United Kingdom','FCHI':'France','GDAXI':'Germany','NSEI':'India',
    'KS11':'South Korea','TWII':'Taiwan','SSMI':'Switzerland','GSPTSE':'Canada',
    'JSETOP40':'South Africa'
}
for r in recs:
    r['country'] = country_map.get(r['Index'], r.get('country','Unknown'))
print('__RESULT__:')
print(json.dumps(recs))"""

env_args = {'var_call_I60HY7iEWg5C8iUAkTJuHhmz': 'file_storage/call_I60HY7iEWg5C8iUAkTJuHhmz.json', 'var_call_RfXZ44Ml6S46DzPqRZJj9z4w': ['index_info'], 'var_call_w68rsQ8bbkkg0yQouK3SHSbw': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_MxJyHIi9khWWrlxUAh1kkDY3': [{'Index': 'IXIC', 'country': 'Unknown', 'months': 257, 'multiple': 4.822046767118095, 'overall_return_pct': 382.20467671180944}, {'Index': 'NSEI', 'country': 'Unknown', 'months': 165, 'multiple': 2.3608849755128487, 'overall_return_pct': 136.08849755128486}, {'Index': 'GDAXI', 'country': 'Unknown', 'months': 257, 'multiple': 2.3474623836455386, 'overall_return_pct': 134.74623836455385}, {'Index': '399001.SZ', 'country': 'China', 'months': 258, 'multiple': 2.344545336356674, 'overall_return_pct': 134.45453363566742}, {'Index': 'TWII', 'country': 'Unknown', 'months': 257, 'multiple': 2.237406175424464, 'overall_return_pct': 123.74061754244639}]}

exec(code, env_args)

code = """import json
res = var_call_VuShfCHNrXP7FpDUPJer7W75
# fix mapping for symbols without caret
index_to_country = {
    'N225': 'Japan',
    'GSPC': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'FCHI': 'France',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'KS11': 'South Korea',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'JN0U.JO': 'South Africa'
}
for r in res:
    r['country'] = index_to_country.get(r['Index'])

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_JVhJ92G9JGSCLoatiN2vgOI7': 'file_storage/call_JVhJ92G9JGSCLoatiN2vgOI7.json', 'var_call_04afrWAiSFqiaaZnCOubWdpU': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_VuShfCHNrXP7FpDUPJer7W75': [{'Index': 'IXIC', 'multiple': 4.816205036184268, 'months': 257, 'country': None}, {'Index': 'NSEI', 'multiple': 2.3564091777426452, 'months': 165, 'country': None}, {'Index': 'GDAXI', 'multiple': 2.3537005565588847, 'months': 257, 'country': None}, {'Index': '399001.SZ', 'multiple': 2.3383811889670953, 'months': 258, 'country': 'China'}, {'Index': 'TWII', 'multiple': 2.2447368452852596, 'months': 257, 'country': None}]}

exec(code, env_args)

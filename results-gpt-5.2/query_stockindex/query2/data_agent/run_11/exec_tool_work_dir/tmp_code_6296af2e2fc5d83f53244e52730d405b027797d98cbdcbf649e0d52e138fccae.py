code = """import json
recs = var_call_q3oufHHUG7b5OHsE29ZIDeYR
out = []
for r in recs:
    up = float(r['up_days'])
    down = float(r['down_days'])
    if up > down:
        out.append(r['Index'])
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8Q9V78C0kXS4401UnB1YOn1s': ['index_info'], 'var_call_aMiAkL1SPTvkQ6gismKWD6Vx': ['index_trade'], 'var_call_3KKxreEFIEJCMxczDm7j3CaI': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_yCml4EyfLi0H5Ya24h0pYYkB': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_q3oufHHUG7b5OHsE29ZIDeYR': [{'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}]}

exec(code, env_args)

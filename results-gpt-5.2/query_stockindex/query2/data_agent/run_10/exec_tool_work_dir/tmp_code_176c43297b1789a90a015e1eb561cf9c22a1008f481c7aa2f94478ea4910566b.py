code = """import json, pandas as pd

df = pd.DataFrame(var_call_Si8byQUVGspB6HGgSDxKYUF5)
# coerce numeric
for c in ['n_days','up_days','down_days']:
    df[c]=pd.to_numeric(df[c])

# North America indices: NYA (NYSE Composite), IXIC (NASDAQ Composite), GSPTSE (S&P/TSX Composite)
na = df[df['Index'].isin(['NYA','IXIC','GSPTSE'])].copy()
na['more_up_than_down'] = na['up_days'] > na['down_days']
res = na[na['more_up_than_down']].sort_values('Index')[['Index','up_days','down_days']]
answer = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_FOOFDveGgAXnQdoKqqKlzsbU': ['index_info'], 'var_call_sKsRMsKyZ6mJadLXHGk7Nl1Q': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_zqqnK7WvWIDd6cnpAPvocip3': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_Si8byQUVGspB6HGgSDxKYUF5': [{'Index': 'J203.JO', 'n_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'IXIC', 'n_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'N225', 'n_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'n_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'n_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'n_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'HSI', 'n_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'n_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'n_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'n_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'NYA', 'n_days': '79', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'N100', 'n_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'n_days': '76', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)

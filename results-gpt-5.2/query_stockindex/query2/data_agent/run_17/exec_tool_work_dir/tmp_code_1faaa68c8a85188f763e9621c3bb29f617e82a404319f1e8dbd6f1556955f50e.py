code = """import json, pandas as pd

df = pd.DataFrame(var_call_xgEe5pxibXhi3GfdKQUXcntC)
# cast numeric strings
for c in ['n_days','up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North America indices mapping inferred from exchange/index list
north_america = {
    'NYA': 'New York Stock Exchange (NYA)',
    'IXIC': 'NASDAQ (IXIC)',
    'GSPTSE': 'Toronto Stock Exchange (GSPTSE)'
}

df_na = df[df['Index'].isin(north_america.keys())].copy()
df_na['name'] = df_na['Index'].map(north_america)

over_up = df_na[df_na['up_days'] > df_na['down_days']].sort_values('Index')
answer_list = over_up['Index'].tolist()

print('__RESULT__:')
print(json.dumps({'indices': answer_list, 'details': over_up[['Index','up_days','down_days']].to_dict(orient='records')}))"""

env_args = {'var_call_W6r76h3UVWOtXRktYqKEVuDT': ['index_info'], 'var_call_CnX7EC0PEjGgZQOMte21vDUZ': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_n9NTEsyTip0OyLG4XYNCKSFM': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_xgEe5pxibXhi3GfdKQUXcntC': [{'Index': 'J203.JO', 'n_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'n_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'n_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'n_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'n_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'n_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'n_days': '79', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'HSI', 'n_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'n_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'n_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'n_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'n_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'n_days': '76', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)

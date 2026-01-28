code = """import json, pandas as pd

df = pd.DataFrame(var_call_rMx5xR9grezG7Z0EiIS1u80W)
# coerce numeric strings
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North America indices based on known mapping:
# NYA (NYSE Composite, US), IXIC (NASDAQ Composite, US), GSPTSE (S&P/TSX Composite, Canada)
na = df[df['Index'].isin(['NYA','IXIC','GSPTSE'])].copy()
na_more_up = na[na['up_days'] > na['down_days']].sort_values('Index')
answer = na_more_up[['Index','up_days','down_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_p2M0bLWn4kpV6P7xk0Igr71j': ['index_info'], 'var_call_1MDHjgs2qZuvHlwaUI7QEREH': ['index_trade'], 'var_call_3ZRfwsbv3T5dZkdhqYW9I30F': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_4H1Z2BTxeHN4KcTCBNTkJ5sf': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_rMx5xR9grezG7Z0EiIS1u80W': [{'Index': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'HSI', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)

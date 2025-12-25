code = """import pandas as pd
import json

with open(locals()['var_function-call-12337040612068561019'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

debug_info = {}
for index_name, group in df.groupby('Index'):
    up_days = group[group['Close'] > group['Open']].shape[0]
    down_days = group[group['Close'] < group['Open']].shape[0]
    debug_info[index_name] = {'up': up_days, 'down': down_days}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-7458028202963988006': ['index_info'], 'var_function-call-7458028202963985611': ['index_trade'], 'var_function-call-14921271989771260256': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-14921271989771262141': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-3554815193617154133': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-12337040612068561019': 'file_storage/function-call-12337040612068561019.json', 'var_function-call-17069154687632134843': ['IXIC']}

exec(code, env_args)

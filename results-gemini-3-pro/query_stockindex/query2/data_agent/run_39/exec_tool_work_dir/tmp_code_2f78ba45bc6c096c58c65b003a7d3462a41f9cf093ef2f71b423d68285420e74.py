code = """import pandas as pd
import json

file_path = locals()['var_function-call-6810584387871759174']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
df_2018 = df[df['Date'].dt.year == 2018].copy()

results = {}
for index_name in ['NYA', 'IXIC', 'GSPTSE']:
    group = df_2018[df_2018['Index'] == index_name]
    up_days = (group['Close'] > group['Open']).sum()
    down_days = (group['Close'] < group['Open']).sum()
    results[index_name] = {'up': int(up_days), 'down': int(down_days)}

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17150134842231265257': ['index_info'], 'var_function-call-17150134842231266666': ['index_trade'], 'var_function-call-3028719031646075140': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8844816984964247701': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-10767464470127093905': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'Close': '2568.300049'}], 'var_function-call-16541636625392433100': [{'Date': 'September 30, 2020 at 12:00 AM'}], 'var_function-call-6810584387871759174': 'file_storage/function-call-6810584387871759174.json', 'var_function-call-9729114095832180303': ['IXIC']}

exec(code, env_args)

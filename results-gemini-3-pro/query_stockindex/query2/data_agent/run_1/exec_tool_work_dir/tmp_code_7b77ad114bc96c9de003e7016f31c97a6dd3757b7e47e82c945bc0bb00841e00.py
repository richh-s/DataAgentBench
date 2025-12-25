code = """import pandas as pd
import json

with open(locals()['var_function-call-13009816149152470627'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])

df_2018 = df[df['Date'].dt.year == 2018].copy()
df_2018['is_up'] = df_2018['Close'] > df_2018['Open']
df_2018['is_down'] = df_2018['Close'] < df_2018['Open']

results = df_2018.groupby('Index')[['is_up', 'is_down']].sum()

print("__RESULT__:")
print(results.to_json())"""

env_args = {'var_function-call-3184075637316832398': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-5622635207725991': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_function-call-14994659038385282803': [{'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}], 'var_function-call-9229395500212327445': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-13009816149152470627': 'file_storage/function-call-13009816149152470627.json', 'var_function-call-15915541419561396846': ['IXIC']}

exec(code, env_args)

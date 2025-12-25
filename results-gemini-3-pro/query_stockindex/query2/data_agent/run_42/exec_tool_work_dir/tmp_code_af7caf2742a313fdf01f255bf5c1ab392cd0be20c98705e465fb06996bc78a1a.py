code = """import json
import pandas as pd

file_path = locals()['var_function-call-5146420228312629501']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df_2018 = df[df['Date'].dt.year == 2018].copy()

df_2018['Open'] = pd.to_numeric(df_2018['Open'], errors='coerce')
df_2018['Close'] = pd.to_numeric(df_2018['Close'], errors='coerce')
df_2018 = df_2018.dropna(subset=['Open', 'Close'])

results = {}
indices = ['IXIC', 'NYA', 'GSPTSE']

for idx in indices:
    sub = df_2018[df_2018['Index'] == idx]
    up_days = sum(sub['Close'] > sub['Open'])
    down_days = sum(sub['Close'] < sub['Open'])
    results[idx] = {'up': up_days, 'down': down_days}

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2746366283723555284': ['index_info'], 'var_function-call-502872477713395494': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-12417923733498193425': ['index_trade'], 'var_function-call-9752965283835245653': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-6861699087213518783': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-10485866844994124588': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-4792080475545075852': [{'Date': 'September 30, 2020 at 12:00 AM'}, {'Date': 'September 30, 2020 at 12:00 AM'}, {'Date': 'September 30, 2020 at 12:00 AM'}, {'Date': 'September 30, 2020 at 12:00 AM'}, {'Date': 'September 30, 2019 at 12:00 AM'}], 'var_function-call-14924311414119862158': [{'Date': '05 Feb 1971, 00:00'}, {'Date': '08 Feb 1971, 00:00'}, {'Date': '1971-02-09 00:00:00'}, {'Date': '1971-02-10 00:00:00'}, {'Date': '11 Feb 1971, 00:00'}], 'var_function-call-15016669656925824078': [{'count_star()': '37163'}], 'var_function-call-5146420228312629501': 'file_storage/function-call-5146420228312629501.json', 'var_function-call-13233269419662497698': ['IXIC']}

exec(code, env_args)

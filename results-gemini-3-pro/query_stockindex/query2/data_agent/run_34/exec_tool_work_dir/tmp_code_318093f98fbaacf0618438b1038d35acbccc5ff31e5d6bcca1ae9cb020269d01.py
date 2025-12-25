code = """import pandas as pd
import json

file_path = locals()['var_function-call-18083602444097427597']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df[df['Date'].dt.year == 2018]

df['Up'] = (df['Close'] > df['Open']).astype(int)
df['Down'] = (df['Close'] < df['Open']).astype(int)

result = df.groupby('Index')[['Up', 'Down']].sum()
print("__RESULT__:")
print(result.to_json())"""

env_args = {'var_function-call-14525901499582339742': ['index_info'], 'var_function-call-14525901499582338717': ['index_trade'], 'var_function-call-8337424923021630348': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-1188953710041648481': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-2445592690623118384': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-18296696890722009446': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-14864950931914302467': [{'Index': 'NYA', 'Date': 'December 31, 1965 at 12:00 AM'}, {'Index': 'NYA', 'Date': '03 Jan 1966, 00:00'}, {'Index': 'NYA', 'Date': '1966-01-04 00:00:00'}, {'Index': 'NYA', 'Date': '05 Jan 1966, 00:00'}, {'Index': 'NYA', 'Date': 'January 06, 1966 at 12:00 AM'}], 'var_function-call-18083602444097427597': 'file_storage/function-call-18083602444097427597.json', 'var_function-call-6294163895348241362': ['IXIC'], 'var_function-call-310937981663079004': {'GSPTSE': 251, 'IXIC': 251, 'NYA': 251}}

exec(code, env_args)

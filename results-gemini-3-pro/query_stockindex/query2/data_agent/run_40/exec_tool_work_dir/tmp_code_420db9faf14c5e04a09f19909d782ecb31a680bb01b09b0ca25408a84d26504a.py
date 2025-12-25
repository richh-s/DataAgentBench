code = """import json
import pandas as pd
import numpy as np

file_path = locals()['var_function-call-13360150098485586410']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(f"Total rows loaded: {len(df)}")

df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

print(f"NaN Open: {df['Open'].isna().sum()}")
print(f"NaN Close: {df['Close'].isna().sum()}")

def clean_date(d):
    d = str(d)
    d = d.replace(" at 12:00 AM", "")
    d = d.replace(", 00:00", "")
    d = d.replace(" 00:00:00", "")
    return d.strip()

df['Date_Clean'] = df['Date'].apply(clean_date)
df['Date_Parsed'] = pd.to_datetime(df['Date_Clean'], errors='coerce')

print(f"NaT Dates: {df['Date_Parsed'].isna().sum()}")
if df['Date_Parsed'].isna().sum() > 0:
    print("Sample NaT dates (original):")
    print(df[df['Date_Parsed'].isna()]['Date'].head().tolist())

df_2018 = df[df['Date_Parsed'].dt.year == 2018].copy()
print(f"Rows in 2018: {len(df_2018)}")

# Check for rows where Open/Close is valid
df_valid = df_2018.dropna(subset=['Open', 'Close'])
print(f"Rows with valid prices in 2018: {len(df_valid)}")

df_valid['Up'] = df_valid['Close'] > df_valid['Open']
df_valid['Down'] = df_valid['Close'] < df_valid['Open']

grouped = df_valid.groupby('Index')[['Up', 'Down']].sum()
print(grouped)

print("__RESULT__:")
print(json.dumps(grouped.to_dict(orient='index')))"""

env_args = {'var_function-call-132721909087634207': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-15951985826592087202': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_function-call-16019284196565972503': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}], 'var_function-call-11069777017572883723': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-13360150098485586410': 'file_storage/function-call-13360150098485586410.json', 'var_function-call-4683547043867167606': ['NYA'], 'var_function-call-9317354994147307522': [{'Index': 'IXIC', 'Date': '05 Feb 1971, 00:00'}, {'Index': 'IXIC', 'Date': '08 Feb 1971, 00:00'}, {'Index': 'IXIC', 'Date': '1971-02-09 00:00:00'}, {'Index': 'IXIC', 'Date': '1971-02-10 00:00:00'}, {'Index': 'IXIC', 'Date': '11 Feb 1971, 00:00'}], 'var_function-call-11416388678025506240': ['NYA'], 'var_function-call-8918035088124978561': {'GSPTSE': {'Up': 34, 'Down': 48}, 'IXIC': {'Up': 36, 'Down': 49}, 'NYA': {'Up': 39, 'Down': 27}}}

exec(code, env_args)

code = """import json
import pandas as pd

file_path = locals()['var_function-call-13360150098485586410']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def clean_date(d):
    d = str(d)
    d = d.replace(" at 12:00 AM", "")
    d = d.replace(", 00:00", "")
    d = d.replace(" 00:00:00", "")
    return d.strip()

df['Date_Clean'] = df['Date'].apply(clean_date)
df['Date_Parsed'] = pd.to_datetime(df['Date_Clean'], errors='coerce')

df_2018 = df[df['Date_Parsed'].dt.year == 2018].copy()

# Ensure numeric
df_2018['Open'] = pd.to_numeric(df_2018['Open'], errors='coerce')
df_2018['Close'] = pd.to_numeric(df_2018['Close'], errors='coerce')
df_2018 = df_2018.dropna(subset=['Open', 'Close'])

df_2018['Up'] = df_2018['Close'] > df_2018['Open']
df_2018['Down'] = df_2018['Close'] < df_2018['Open']

grouped = df_2018.groupby('Index')[['Up', 'Down']].sum()
result_indices = grouped[grouped['Up'] > grouped['Down']].index.tolist()

debug_info = {
    "total_rows_loaded": len(df),
    "rows_2018": len(df_2018),
    "counts": grouped.to_dict(orient='index'),
    "result": result_indices
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-132721909087634207': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-15951985826592087202': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_function-call-16019284196565972503': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}], 'var_function-call-11069777017572883723': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-13360150098485586410': 'file_storage/function-call-13360150098485586410.json', 'var_function-call-4683547043867167606': ['NYA'], 'var_function-call-9317354994147307522': [{'Index': 'IXIC', 'Date': '05 Feb 1971, 00:00'}, {'Index': 'IXIC', 'Date': '08 Feb 1971, 00:00'}, {'Index': 'IXIC', 'Date': '1971-02-09 00:00:00'}, {'Index': 'IXIC', 'Date': '1971-02-10 00:00:00'}, {'Index': 'IXIC', 'Date': '11 Feb 1971, 00:00'}], 'var_function-call-11416388678025506240': ['NYA'], 'var_function-call-8918035088124978561': {'GSPTSE': {'Up': 34, 'Down': 48}, 'IXIC': {'Up': 36, 'Down': 49}, 'NYA': {'Up': 39, 'Down': 27}}, 'var_function-call-9412470027718849701': {'GSPTSE': {'Up': 34, 'Down': 48}, 'IXIC': {'Up': 36, 'Down': 49}, 'NYA': {'Up': 39, 'Down': 27}}, 'var_function-call-1415239274386070846': [{'Date': 'December 31, 1965 at 12:00 AM'}, {'Date': '03 Jan 1966, 00:00'}, {'Date': '1966-01-04 00:00:00'}, {'Date': '05 Jan 1966, 00:00'}, {'Date': 'January 06, 1966 at 12:00 AM'}, {'Date': '1966-01-07 00:00:00'}, {'Date': '1966-01-10 00:00:00'}, {'Date': 'January 11, 1966 at 12:00 AM'}, {'Date': '12 Jan 1966, 00:00'}, {'Date': 'January 13, 1966 at 12:00 AM'}, {'Date': 'January 14, 1966 at 12:00 AM'}, {'Date': 'January 17, 1966 at 12:00 AM'}, {'Date': '1966-01-18 00:00:00'}, {'Date': 'January 19, 1966 at 12:00 AM'}, {'Date': '20 Jan 1966, 00:00'}, {'Date': 'January 21, 1966 at 12:00 AM'}, {'Date': '1966-01-24 00:00:00'}, {'Date': '1966-01-25 00:00:00'}, {'Date': '26 Jan 1966, 00:00'}, {'Date': 'January 27, 1966 at 12:00 AM'}]}

exec(code, env_args)

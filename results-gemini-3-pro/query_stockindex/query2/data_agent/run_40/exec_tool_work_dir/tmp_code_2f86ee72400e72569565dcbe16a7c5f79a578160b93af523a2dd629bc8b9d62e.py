code = """import json
import pandas as pd
import sys

file_path = locals()['var_function-call-13360150098485586410']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Test dateutil
try:
    from dateutil import parser
    has_dateutil = True
except ImportError:
    has_dateutil = False

debug_info = {}
debug_info['has_dateutil'] = has_dateutil

def clean_date(d):
    d = str(d)
    d = d.replace(" at 12:00 AM", "")
    d = d.replace(", 00:00", "")
    d = d.replace(" 00:00:00", "")
    return d.strip()

df['Date_Clean'] = df['Date'].apply(clean_date)

# Try parsing with dateutil if available
if has_dateutil:
    def parse_dt(x):
        try:
            return parser.parse(x)
        except:
            return pd.NaT
    df['Date_Parsed'] = df['Date'].apply(parse_dt)
else:
    # Try mixed format
    try:
        df['Date_Parsed'] = pd.to_datetime(df['Date_Clean'], format='mixed', errors='coerce')
    except:
        # Fallback
        df['Date_Parsed'] = pd.to_datetime(df['Date_Clean'], errors='coerce')

df['Year'] = df['Date_Parsed'].dt.year
df_2018 = df[df['Year'] == 2018].copy()

# Recalculate NaT stats
debug_info['NaT_count'] = int(df['Date_Parsed'].isna().sum())
debug_info['rows_2018'] = int(len(df_2018))

# Process if we have data
if not df_2018.empty:
    df_2018['Open'] = pd.to_numeric(df_2018['Open'], errors='coerce')
    df_2018['Close'] = pd.to_numeric(df_2018['Close'], errors='coerce')
    df_2018['Up'] = df_2018['Close'] > df_2018['Open']
    df_2018['Down'] = df_2018['Close'] < df_2018['Open']
    grouped = df_2018.groupby('Index')[['Up', 'Down']].sum()
    debug_info['counts'] = grouped.to_dict(orient='index')
    
    result_indices = grouped[grouped['Up'] > grouped['Down']].index.tolist()
    debug_info['result'] = result_indices

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-132721909087634207': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-15951985826592087202': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_function-call-16019284196565972503': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}], 'var_function-call-11069777017572883723': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-13360150098485586410': 'file_storage/function-call-13360150098485586410.json', 'var_function-call-4683547043867167606': ['NYA'], 'var_function-call-9317354994147307522': [{'Index': 'IXIC', 'Date': '05 Feb 1971, 00:00'}, {'Index': 'IXIC', 'Date': '08 Feb 1971, 00:00'}, {'Index': 'IXIC', 'Date': '1971-02-09 00:00:00'}, {'Index': 'IXIC', 'Date': '1971-02-10 00:00:00'}, {'Index': 'IXIC', 'Date': '11 Feb 1971, 00:00'}], 'var_function-call-11416388678025506240': ['NYA'], 'var_function-call-8918035088124978561': {'GSPTSE': {'Up': 34, 'Down': 48}, 'IXIC': {'Up': 36, 'Down': 49}, 'NYA': {'Up': 39, 'Down': 27}}, 'var_function-call-9412470027718849701': {'GSPTSE': {'Up': 34, 'Down': 48}, 'IXIC': {'Up': 36, 'Down': 49}, 'NYA': {'Up': 39, 'Down': 27}}, 'var_function-call-1415239274386070846': [{'Date': 'December 31, 1965 at 12:00 AM'}, {'Date': '03 Jan 1966, 00:00'}, {'Date': '1966-01-04 00:00:00'}, {'Date': '05 Jan 1966, 00:00'}, {'Date': 'January 06, 1966 at 12:00 AM'}, {'Date': '1966-01-07 00:00:00'}, {'Date': '1966-01-10 00:00:00'}, {'Date': 'January 11, 1966 at 12:00 AM'}, {'Date': '12 Jan 1966, 00:00'}, {'Date': 'January 13, 1966 at 12:00 AM'}, {'Date': 'January 14, 1966 at 12:00 AM'}, {'Date': 'January 17, 1966 at 12:00 AM'}, {'Date': '1966-01-18 00:00:00'}, {'Date': 'January 19, 1966 at 12:00 AM'}, {'Date': '20 Jan 1966, 00:00'}, {'Date': 'January 21, 1966 at 12:00 AM'}, {'Date': '1966-01-24 00:00:00'}, {'Date': '1966-01-25 00:00:00'}, {'Date': '26 Jan 1966, 00:00'}, {'Date': 'January 27, 1966 at 12:00 AM'}], 'var_function-call-8420978581612418654': {'total_rows_loaded': 753, 'rows_2018': 233, 'counts': {'GSPTSE': {'Up': 34, 'Down': 48}, 'IXIC': {'Up': 36, 'Down': 49}, 'NYA': {'Up': 39, 'Down': 27}}, 'result': ['NYA']}, 'var_function-call-11685535736278381957': {'total': 753, 'year_2018': 233, 'NaT_count': 520, 'not_2018_sample': ['04 Jan 2018, 00:00', '05 Jan 2018, 00:00', '2018-01-09 00:00:00', '10 Jan 2018, 00:00', '11 Jan 2018, 00:00'], 'NaT_sample': ['04 Jan 2018, 00:00', '05 Jan 2018, 00:00', '2018-01-09 00:00:00', '10 Jan 2018, 00:00', '11 Jan 2018, 00:00']}}

exec(code, env_args)

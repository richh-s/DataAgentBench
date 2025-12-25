code = """import json
import pandas as pd
import dateutil.parser

# Load data
with open(locals()['var_function-call-10561230580302364662'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Helper to parse dates
def parse_date(d):
    try:
        return pd.to_datetime(d)
    except:
        try:
            return dateutil.parser.parse(d)
        except:
            return pd.NaT

df['Date_Parsed'] = pd.to_datetime(df['Date'], errors='coerce')

# Check if we have enough 2018 data
df_2018 = df[df['Date_Parsed'].dt.year == 2018].copy()

# Ensure numeric columns
cols = ['Open', 'Close']
for c in cols:
    df_2018[c] = pd.to_numeric(df_2018[c], errors='coerce')

# Calculate Up/Down
df_2018['Up'] = df_2018['Close'] > df_2018['Open']
df_2018['Down'] = df_2018['Close'] < df_2018['Open']

# Aggregate
result = df_2018.groupby('Index')[['Up', 'Down']].sum()

print("__RESULT__:")
print(result.to_json())"""

env_args = {'var_function-call-8468999768472924223': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8468999768472924450': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-15268200763498426462': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}], 'var_function-call-11567062012809635610': [{'Date': '05 Feb 1971, 00:00'}, {'Date': '08 Feb 1971, 00:00'}, {'Date': '1971-02-09 00:00:00'}, {'Date': '1971-02-10 00:00:00'}, {'Date': '11 Feb 1971, 00:00'}], 'var_function-call-14509001577574359370': [{'count_star()': '37163'}], 'var_function-call-10561230580302364662': 'file_storage/function-call-10561230580302364662.json'}

exec(code, env_args)

code = """import json, pandas as pd
import os

path = var_call_A4meYbsYk5hIeseSlueYdF5X
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# parse Date as datetime with day-first and flexible format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# filter from 2020-01-01
mask = df['Date'] >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# convert numeric columns
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# drop rows with missing needed values
df = df.dropna(subset=['Open','High','Low'])

# compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

result = df.groupby('Index')['vol'].mean().sort_values(ascending=False)

out = result.reset_index().to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5ik1rBEdZCl1mg61Qkn4Vcz7': ['index_info'], 'var_call_yl3eSwKFGzZdJQtS38mjNiz5': ['index_trade'], 'var_call_BlQjBbGrjBWP79OPvsEZtCoA': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_call_A4meYbsYk5hIeseSlueYdF5X': 'file_storage/call_A4meYbsYk5hIeseSlueYdF5X.json'}

exec(code, env_args)

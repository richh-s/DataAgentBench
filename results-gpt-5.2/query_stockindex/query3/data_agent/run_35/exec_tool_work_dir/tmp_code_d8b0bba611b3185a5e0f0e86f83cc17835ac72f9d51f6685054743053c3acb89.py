code = """import json, pandas as pd
from datetime import datetime

path = var_call_NCn27vrRETPgRTdWTyTds7w8
with open(path, 'r') as f:
    rows = json.load(f)

def parse_date(s):
    fmts = [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%d %b %Y, %H:%M',
        '%B %d, %Y at %I:%M %p',
        '%b %d, %Y at %I:%M %p',
    ]
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            pass
    return pd.NaT

df = pd.DataFrame(rows)
df['dt'] = df['Date'].map(parse_date)
df = df.dropna(subset=['dt'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])
df = df[df['dt'] >= pd.Timestamp('2000-01-01')]

# monthly last close
idx_groups = df.sort_values('dt').groupby(['Index', pd.Grouper(key='dt', freq='MS')], sort=False)
monthly = idx_groups['CloseUSD'].last().reset_index().rename(columns={'dt':'month','CloseUSD':'close_usd'})

# build cashflow: invest 1 unit each month at month close => units = 1/price
monthly['units'] = 1.0 / monthly['close_usd']

# for each index compute total units invested and final value at last month
res = []
for idx, g in monthly.groupby('Index'):
    g = g.sort_values('month')
    total_units = g['units'].sum()
    final_price = g['close_usd'].iloc[-1]
    final_value = total_units * final_price
    months = len(g)
    invested = months * 1.0
    multiple = final_value / invested
    res.append({'Index': idx, 'MonthsAvailable': months, 'Invested': invested, 'FinalValue': final_value, 'ReturnMultiple': multiple})

out = pd.DataFrame(res).sort_values('ReturnMultiple', ascending=False).head(5)
print('__RESULT__:')
print(out.to_json(orient='records'))"""

env_args = {'var_call_1oDxJjpBDh0FKEVZMMEQl2Mo': ['index_info'], 'var_call_0TRAH6EA7OhvVx9PgRtUmyHO': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_PYWVyhefplIODCHHDPhUaLuv': 'file_storage/call_PYWVyhefplIODCHHDPhUaLuv.json', 'var_call_nBk5CM0aVrJwGLqG7dFRFsi3': {'parsed_ok': 50, 'examples': [{'raw': '31 Dec 1986, 00:00', 'parsed': '1986-12-31'}, {'raw': 'January 02, 1987 at 12:00 AM', 'parsed': '1987-01-02'}, {'raw': '1987-01-05 00:00:00', 'parsed': '1987-01-05'}, {'raw': '06 Jan 1987, 00:00', 'parsed': '1987-01-06'}, {'raw': '07 Jan 1987, 00:00', 'parsed': '1987-01-07'}, {'raw': '1987-01-08 00:00:00', 'parsed': '1987-01-08'}, {'raw': '1987-01-09 00:00:00', 'parsed': '1987-01-09'}, {'raw': '1987-01-12 00:00:00', 'parsed': '1987-01-12'}, {'raw': '1987-01-13 00:00:00', 'parsed': '1987-01-13'}, {'raw': '1987-01-14 00:00:00', 'parsed': '1987-01-14'}]}, 'var_call_NCn27vrRETPgRTdWTyTds7w8': 'file_storage/call_NCn27vrRETPgRTdWTyTds7w8.json'}

exec(code, env_args)

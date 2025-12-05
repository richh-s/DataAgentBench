code = """import json, pandas as pd
from datetime import datetime

# Load large trade data from file
path = var_call_OoANpUO5RshrKMF25q7fMh9K
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date
def parse_date(s):
    for fmt in ["%d %b %Y, %H:%M", "%B %d, %Y at %I:%M %p"]:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter from 2000-01-01
start = datetime(2000,1,1)
df = df[df['Date_parsed']>=start]

# Assume monthly investment on the last trading day of each month
amount = 100  # arbitrary; ranking is scale-invariant

results = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date_parsed')
    # monthly resample: pick last row per year-month
    g['ym'] = g['Date_parsed'].dt.to_period('M')
    last_per_month = g.sort_values('Date_parsed').groupby('ym').tail(1)
    if last_per_month.empty:
        continue
    # contributions: invest "amount" at each month-end price
    prices = last_per_month['Adj Close'].astype(float).values
    units = amount / prices
    total_units = units.sum()
    total_invested = amount * len(prices)
    # value at last available price
    final_price = prices[-1]
    final_value = total_units * final_price
    results.append({'Index': idx, 'total_invested': float(total_invested), 'final_value': float(final_value), 'multiple': float(final_value/total_invested)})

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('multiple', ascending=False).head(5)

result = res_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZNlbLe306v59bWiCHe2G5hSc': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_OoANpUO5RshrKMF25q7fMh9K': 'file_storage/call_OoANpUO5RshrKMF25q7fMh9K.json'}

exec(code, env_args)

code = """import json, pandas as pd
from datetime import datetime

# Load full trade data from file
file_path = var_call_YOa9oGsdktpGZRCeeknUAEnh
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date formats and filter from 2000-01-01
def parse_date(x):
    for fmt in ['%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p', '%d %b %Y', '%Y-%m-%d']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date'] = df['Date'].apply(parse_date)

df = df[df['Date'] >= datetime(2000,1,1)]

# Ensure numeric
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Create year-month for monthly DCA contributions (assume invest once per month at last trading day)
df['ym'] = df['Date'].dt.to_period('M')

results = []

for idx, grp in df.groupby('Index'):
    grp = grp.sort_values('Date')
    # keep from first full month >=2000 that has data
    # simulate $1 invested each month at that month's last trading day adj close
    monthly = grp.groupby('ym').tail(1)
    if len(monthly) < 12:  # require at least 1 year of data
        continue
    prices = monthly['Adj Close'].values
    # units bought each month with $1
    units = 1.0 / prices
    total_units = units.sum()
    final_price = prices[-1]
    final_value = total_units * final_price
    total_invested = len(prices) * 1.0
    # return multiple
    multiple = final_value / total_invested
    results.append({'Index': idx, 'months': int(len(prices)), 'multiple': float(multiple)})

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('multiple', ascending=False).head(5)

result = res_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_B4GUqPUJRfZaRDcr1OFBVkF4': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_YOa9oGsdktpGZRCeeknUAEnh': 'file_storage/call_YOa9oGsdktpGZRCeeknUAEnh.json'}

exec(code, env_args)

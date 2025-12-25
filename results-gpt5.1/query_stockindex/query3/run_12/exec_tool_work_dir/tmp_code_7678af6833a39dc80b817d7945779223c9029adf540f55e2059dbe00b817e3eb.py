code = """import pandas as pd, json
from datetime import datetime

file_path = var_call_0mZxLTsdAkGjO51DoBGGRUnO
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date formats and filter from 2000-01-01
def parse_date(x):
    for fmt in ['%d %b %Y, %H:%M', '%d %b %Y, %H:%M:%S', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date_parsed'])
start = datetime(2000,1,1)
df = df[df['Date_parsed']>=start]

# Ensure Adj Close is float
df['Adj Close'] = df['Adj Close'].astype(float)

# Create a year-month column
df['YearMonth'] = df['Date_parsed'].dt.to_period('M')

# Assume regular monthly investments on the last available trading day of each month
idx = df.sort_values(['Index','Date_parsed']).groupby(['Index','YearMonth'])['Date_parsed'].idxmax()
monthly = df.loc[idx].copy()

# For each index, simulate investing 1 unit of currency every month (constant dollar amount)
# Units bought each month = 1 / price; total units * last price gives final value.
monthly['units'] = 1.0 / monthly['Adj Close']

latest_dates = df.groupby('Index')['Date_parsed'].max().reset_index().rename(columns={'Date_parsed':'LastDate'})
latest_prices = df.sort_values('Date_parsed').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'LastPrice'})
latest = pd.merge(latest_dates, latest_prices, on='Index')

units_agg = monthly.groupby('Index')['units'].sum().reset_index()
result = pd.merge(units_agg, latest, on='Index')
result['final_value'] = result['units'] * result['LastPrice']

# Also compute total invested months for information
months_count = monthly.groupby('Index')['YearMonth'].nunique().reset_index().rename(columns={'YearMonth':'n_months'})
result = pd.merge(result, months_count, on='Index')
result = result[result['n_months']>0]

# Get top 5 indices by final_value
top5 = result.sort_values('final_value', ascending=False).head(5)

out = top5[['Index','final_value','n_months']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_2qrGkpGXu7SAVfVqDSsZ3yDe': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_0mZxLTsdAkGjO51DoBGGRUnO': 'file_storage/call_0mZxLTsdAkGjO51DoBGGRUnO.json'}

exec(code, env_args)

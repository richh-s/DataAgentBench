code = """import json, pandas as pd
from datetime import datetime

# Load full large result
path = var_call_FW2FDesprMj4gSEpkuU3PQaN
with open(path, 'r') as f:
    data = json.load(f)

# Put into DataFrame
df = pd.DataFrame(data)

# Normalize date formats and filter from 2000-01-01
def parse_date(x):
    for fmt in ['%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.to_datetime(x, errors='coerce')

df['Date'] = df['Date'].apply(parse_date)
df = df[df['Date'] >= datetime(2000,1,1)]

# Ensure numeric
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Monthly DCA: assume invest 1 unit of cash at last trading day of each month per index
# For each index and year-month, take last date's price; compute total units accumulated; final value = units * last price

df['ym'] = df['Date'].dt.to_period('M')

results = []
for idx, g in df.groupby('Index'):
    gm = g.sort_values('Date').groupby('ym').tail(1)
    if gm.empty:
        continue
    units = (1.0 / gm['Adj Close']).sum()
    final_price = g.loc[g['Date'].idxmax(), 'Adj Close']
    final_value = units * final_price
    results.append({'Index': idx, 'final_value': final_value})

res_df = pd.DataFrame(results).sort_values('final_value', ascending=False).head(5)

result = res_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ebzMhyd7UdE8ljMJyw7uKJ3X': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}], 'var_call_FW2FDesprMj4gSEpkuU3PQaN': 'file_storage/call_FW2FDesprMj4gSEpkuU3PQaN.json'}

exec(code, env_args)

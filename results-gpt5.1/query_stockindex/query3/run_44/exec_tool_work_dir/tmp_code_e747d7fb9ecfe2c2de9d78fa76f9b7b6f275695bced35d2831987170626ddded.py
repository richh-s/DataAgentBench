code = """import json, pandas as pd
from datetime import datetime

path = var_call_9c6sa2QWf6yKBzViPSPB7yyZ
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

df['Date'] = df['Date'].dt.to_period('M').dt.to_timestamp()
df['Adj Close'] = df['Adj Close'].astype(float)

monthly = df.sort_values(['Index','Date']).groupby(['Index','Date']).tail(1)

results = []
for idx, grp in monthly.groupby('Index'):
    grp = grp.sort_values('Date')
    grp = grp[grp['Date'] >= pd.Timestamp('2000-01-31')]
    if grp.empty:
        continue
    start_price = grp.iloc[0]['Adj Close']
    norm = grp['Adj Close'] / start_price
    total_units = norm.sum()
    final_price = grp.iloc[-1]['Adj Close']
    final_value = total_units * final_price
    total_invest = len(grp)
    multiple = final_value / total_invest
    results.append({'Index': idx, 'multiple': multiple})

top5 = sorted(results, key=lambda x: x['multiple'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_9c6sa2QWf6yKBzViPSPB7yyZ': 'file_storage/call_9c6sa2QWf6yKBzViPSPB7yyZ.json', 'var_call_p4wUJx9WV9mnScBZwcZH7jkm': ['index_info']}

exec(code, env_args)

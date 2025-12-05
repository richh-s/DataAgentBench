code = """import json, pandas as pd
from datetime import datetime

path = var_call_8PNQtPplfpQjz8QolRpznJoo
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure Date is string then parse
df['Date'] = pd.to_datetime(df['Date'].astype(str), errors='coerce').dt.to_period('M')

monthly = df.groupby(['Index','Date'])['Adj Close'].last().reset_index()

monthly['Adj Close'] = monthly['Adj Close'].astype(float)

C = 100
monthly['units'] = C / monthly['Adj Close']

monthly.sort_values(['Index','Date'], inplace=True)

results = []
for idx, grp in monthly.groupby('Index'):
    grp = grp.dropna(subset=['Adj Close'])
    if grp.empty:
        continue
    units = grp['units'].sum()
    last_price = grp['Adj Close'].iloc[-1]
    total_contrib = C * len(grp)
    final_value = units * last_price
    total_return = (final_value / total_contrib) - 1
    results.append({'Index': idx, 'total_return': total_return})

res_df = pd.DataFrame(results).sort_values('total_return', ascending=False).head(5)

result = res_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8PNQtPplfpQjz8QolRpznJoo': 'file_storage/call_8PNQtPplfpQjz8QolRpznJoo.json', 'var_call_BoYXlgUnElOYocETpmzBoxKm': ['index_info']}

exec(code, env_args)

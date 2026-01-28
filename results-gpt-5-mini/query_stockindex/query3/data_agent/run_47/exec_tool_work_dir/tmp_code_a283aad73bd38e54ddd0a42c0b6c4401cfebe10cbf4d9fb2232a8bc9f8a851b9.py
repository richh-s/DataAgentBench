code = """import json
import pandas as pd
from datetime import datetime

# Load data from storage variables
# var_call_Mi0qdYN0BpVQl7cja7UNtaAe contains file path to large JSON
with open(var_call_Mi0qdYN0BpVQl7cja7UNtaAe, 'r') as f:
    data = json.load(f)

# index info available in var_call_qp0DEN9fhAjckt8EjOeFYXdP
index_info = var_call_qp0DEN9fhAjckt8EjOeFYXdP

df = pd.DataFrame(data)
# Convert types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])

# Filter from 2000-01-01
start_date = pd.to_datetime('2000-01-01')
df = df[df['Date'] >= start_date].copy()

# Determine monthly first trading day per index
# Create year-month period
df['YearMonth'] = df['Date'].dt.to_period('M')

results = []
monthly_contribution = 1.0

for idx, group in df.groupby('Index'):
    g = group.sort_values('Date')
    # For each YearMonth, take the first trading day
    monthly = g.groupby('YearMonth').first().reset_index()
    # Only consider months where Date >= start_date
    monthly = monthly[monthly['Date'] >= start_date]
    months = len(monthly)
    if months == 0:
        continue
    shares = (monthly_contribution / monthly['CloseUSD']).sum()
    last_price = g.iloc[-1]['CloseUSD']
    final_value = shares * last_price
    total_invested = months * monthly_contribution
    return_factor = None
    if total_invested > 0:
        return_factor = final_value / total_invested
    results.append({
        'Index': idx,
        'months': months,
        'total_invested': round(float(total_invested), 6),
        'final_value': round(float(final_value), 6),
        'return_factor': round(float(return_factor), 6),
        'last_date': g.iloc[-1]['Date'].strftime('%Y-%m-%d')
    })

res_df = pd.DataFrame(results)
# Remove any infinite or NaN
res_df = res_df[res_df['return_factor'].notna() & res_df['return_factor'] != float('inf')]

# Get top 10 to inspect if needed
top5 = res_df.sort_values('return_factor', ascending=False).head(5)
output = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_g0h6mRxm2lCzdwaun3y0hEPB': ['index_trade'], 'var_call_Mi0qdYN0BpVQl7cja7UNtaAe': 'file_storage/call_Mi0qdYN0BpVQl7cja7UNtaAe.json', 'var_call_o2aQmVbVBNOdULA6hy7eruXJ': ['index_info'], 'var_call_qp0DEN9fhAjckt8EjOeFYXdP': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

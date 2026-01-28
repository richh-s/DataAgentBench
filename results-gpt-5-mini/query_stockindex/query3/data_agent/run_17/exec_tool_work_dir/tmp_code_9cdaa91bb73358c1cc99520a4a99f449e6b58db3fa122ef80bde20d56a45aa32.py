code = """import json
import pandas as pd
from datetime import datetime

# Load the full index_trade query result from the storage variable
path = var_call_9Cqge3Z3p39dI4jIyEyMvFXX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Convert types
df['Date'] = pd.to_datetime(df['Date'])
# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter from 2000-01-01 inclusive
start_date = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start_date].copy()

# Investment parameters
monthly_amount = 1.0  # dollars per month

results = []
for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').copy()
    if g.empty:
        continue
    # Group by year-month and take first available trading day in each month
    g['year_month'] = g['Date'].dt.to_period('M')
    monthly = g.groupby('year_month').first().reset_index()
    # Only consider months where CloseUSD is available and > 0
    monthly = monthly[monthly['CloseUSD'].notna() & (monthly['CloseUSD'] > 0)]
    months_count = len(monthly)
    if months_count == 0:
        continue
    # Shares bought each month
    monthly['shares'] = monthly['CloseUSD'].apply(lambda p: monthly_amount / p)
    total_shares = monthly['shares'].sum()
    # Final price is the last available CloseUSD in the full series
    last_price = g.loc[g['Date'].idxmax(), 'CloseUSD']
    # Compute final value and return multiple
    final_value = total_shares * last_price
    total_invested = months_count * monthly_amount
    return_multiple = final_value / total_invested if total_invested > 0 else None
    results.append({
        'Index': idx,
        'months_invested': int(months_count),
        'total_invested': total_invested,
        'final_value': final_value,
        'return_multiple': return_multiple
    })

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('return_multiple', ascending=False).reset_index(drop=True)

# Manual mapping of indices to countries
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'J203.JO': 'South Africa',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands'
}

# Take top 5
top5 = res_df.head(5).copy()
output = []
for _, row in top5.iterrows():
    idx = row['Index']
    country = country_map.get(idx, 'Unknown')
    output.append({
        'Index': idx,
        'Country': country,
        'ReturnMultiple': round(float(row['return_multiple']), 4),
        'TotalMonthsInvested': int(row['months_invested'])
    })

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_sMCAwN2P7AfXmnOEewi7X0ek': ['index_trade'], 'var_call_ggsJ59AMp7QS94oOxnlZ06vP': ['index_info'], 'var_call_W8ridIt8gV8vjwzKqiAEoPMW': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_9Cqge3Z3p39dI4jIyEyMvFXX': 'file_storage/call_9Cqge3Z3p39dI4jIyEyMvFXX.json'}

exec(code, env_args)

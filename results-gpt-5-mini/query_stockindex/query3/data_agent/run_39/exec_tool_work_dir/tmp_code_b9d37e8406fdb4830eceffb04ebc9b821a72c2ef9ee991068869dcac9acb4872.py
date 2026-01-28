code = """import pandas as pd
import json

# Load the query result from storage. The variable name is provided by the tool call key.
# var_call_eRsfphHKMIH6GXeE23JR33d7 contains the path to the JSON file with the full result.
records_path = var_call_eRsfphHKMIH6GXeE23JR33d7

df = pd.read_json(records_path)
# Ensure correct types
df['Date'] = pd.to_datetime(df['Date'])
# CloseUSD may be string, convert to float
df['CloseUSD'] = df['CloseUSD'].astype(float)

# Prepare YearMonth period
df['YearMonth'] = df['Date'].dt.to_period('M')

results = []
for idx, group in df.groupby('Index'):
    g = group.sort_values('Date')
    # For each month, pick first trading day
    monthly = g.loc[g.groupby('YearMonth')['Date'].idxmin()]
    monthly = monthly.sort_values('Date')
    # Investment amount per month (USD)
    amt = 1.0
    # Only consider months from 2000-01 onward (query already filtered)
    num_months = len(monthly)
    if num_months == 0:
        continue
    # Total shares accumulated
    shares = (amt / monthly['CloseUSD']).sum()
    # Final price is last available CloseUSD for that index
    final_price = g['CloseUSD'].iloc[-1]
    final_value = shares * final_price
    total_contrib = num_months * amt
    # Return multiplier (final value divided by total invested)
    if total_contrib > 0:
        multiplier = final_value / total_contrib
    else:
        multiplier = None
    results.append({
        'Index': idx,
        'months_invested': int(num_months),
        'final_value_usd': float(final_value),
        'total_contributed_usd': float(total_contrib),
        'return_multiplier': float(multiplier)
    })

res_df = pd.DataFrame(results)
# Sort by return multiplier descending
res_df = res_df.sort_values('return_multiplier', ascending=False).reset_index(drop=True)

# Map indices to countries (manual mapping based on common index symbols)
country_map = {
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'N100': 'Netherlands',
    '399001.SZ': 'China'
}

# Take top 5
top5 = res_df.head(5).copy()
# Add country
top5['country'] = top5['Index'].map(country_map).fillna('Unknown')

# Prepare output list of dicts
output = []
for _, row in top5.iterrows():
    output.append({
        'Index': row['Index'],
        'Country': row['country'],
        'Return Multiplier': round(row['return_multiplier'], 4),
        'Final Value USD': round(row['final_value_usd'], 2),
        'Total Contributed USD': round(row['total_contributed_usd'], 2),
        'Months Invested': int(row['months_invested'])
    })

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_7u3YVMVix8LBnpVqybcbuOVg': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_eRsfphHKMIH6GXeE23JR33d7': 'file_storage/call_eRsfphHKMIH6GXeE23JR33d7.json'}

exec(code, env_args)

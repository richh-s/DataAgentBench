code = """import pandas as pd
import json

# Load data from previous query stored in a file path variable
# var_call_xroc9GzWsDwRLVhqphmVSuCG contains the file path
fp = var_call_xroc9GzWsDwRLVhqphmVSuCG

df = pd.read_json(fp)
# Ensure correct dtypes
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to float
# Some values may be strings; coerce
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter from 2000-01-01 onwards
df = df[df['Date'] >= pd.to_datetime('2000-01-01')].copy()

# Prepare mapping from index symbol to country (inferred by domain knowledge)
index_to_country = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands',
    '399001.SZ': 'China',
    'NYA': 'United States'
}

results = []

for idx, g in df.groupby('Index'):
    g = g.sort_values('Date').copy()
    # Year-month period
    g['YearMonth'] = g['Date'].dt.to_period('M')
    # For each month pick earliest trading day
    first_of_month = g.groupby('YearMonth').first().reset_index()
    # Only consider months from 2000-01 to last available month
    # Count months invested
    months_invested = len(first_of_month)
    if months_invested == 0:
        continue
    # Invest $1 each month at CloseUSD on that first trading day
    # Shares bought per month = 1 / CloseUSD (if CloseUSD > 0)
    first_of_month = first_of_month[first_of_month['CloseUSD'] > 0]
    first_of_month['shares'] = 1.0 / first_of_month['CloseUSD']
    total_shares = first_of_month['shares'].sum()
    # Final close USD = last available CloseUSD in g
    last_close = g['CloseUSD'].iloc[-1]
    final_value = total_shares * last_close
    total_invested = months_invested * 1.0
    return_multiple = final_value / total_invested if total_invested != 0 else None
    return_percent = (final_value - total_invested) / total_invested * 100 if total_invested != 0 else None

    results.append({
        'Index': idx,
        'MonthsInvested': months_invested,
        'TotalInvestedUSD': round(total_invested, 2),
        'FinalValueUSD': round(float(final_value), 2),
        'ReturnMultiple': round(float(return_multiple), 4),
        'ReturnPercent': round(float(return_percent), 2),
        'Country': index_to_country.get(idx, 'Unknown')
    })

# Sort by ReturnMultiple desc and take top 5
results_sorted = sorted(results, key=lambda x: x['ReturnMultiple'], reverse=True)
top5 = results_sorted[:5]

# Prepare JSON string
out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_hOuC4fyceaWQmatOMiztSyGT': ['index_trade'], 'var_call_vLhktk2pijxaV2ogUtBLNXb9': ['index_info'], 'var_call_WoFRJtNBfzEz0LJOGXQPrQlw': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_call_xroc9GzWsDwRLVhqphmVSuCG': 'file_storage/call_xroc9GzWsDwRLVhqphmVSuCG.json'}

exec(code, env_args)

code = """import pandas as pd
import json

# Load data from storage variables
# var_call_vMsuaof3Ao9NsGJzU5cz6cUD is a file path to the full JSON result
path = var_call_vMsuaof3Ao9NsGJzU5cz6cUD

df = pd.read_json(path)
# Ensure correct dtypes
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Group indices
results = []

# country mapping for known indices
country_map = {
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Euronext (Europe)',
    '399001.SZ': 'China'
}

# Parameters for DCA
contribution = 1.0  # $1 per month
start_period = pd.Timestamp('2000-01-01')

for idx, g in df.groupby('Index'):
    g = g.sort_values('Date').reset_index(drop=True)
    # only consider data from 2000-01-01
    g = g[g['Date'] >= start_period]
    if g.empty:
        continue
    # Determine first trading day of each month present in g
    g['year_month'] = g['Date'].dt.to_period('M')
    first_of_month = g.groupby('year_month').first().reset_index()
    # contributions count
    contrib_count = len(first_of_month)
    # Sum shares bought each month
    # skip any month where CloseUSD is null or zero
    valid = first_of_month[first_of_month['CloseUSD'].notna() & (first_of_month['CloseUSD']>0)]
    if valid.empty:
        continue
    shares_bought = (contribution / valid['CloseUSD']).sum()
    total_invested = contribution * contrib_count
    # final value based on last available CloseUSD in the dataset for that index
    last_close = g['CloseUSD'].iloc[-1]
    final_value = shares_bought * last_close
    # return multiple
    return_multiple = final_value / total_invested if total_invested>0 else None
    return_pct = (return_multiple - 1.0) * 100.0 if return_multiple is not None else None

    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'Contributions': int(contrib_count),
        'TotalInvestedUSD': round(total_invested, 2),
        'FinalValueUSD': round(float(final_value), 2),
        'ReturnMultiple': round(float(return_multiple), 4) if return_multiple is not None else None,
        'ReturnPercent': round(float(return_pct), 2) if return_pct is not None else None
    })

# Sort by ReturnMultiple descending and take top 5
results_sorted = sorted(results, key=lambda x: (x['ReturnMultiple'] is not None, x['ReturnMultiple']), reverse=True)
top5 = results_sorted[:5]

output = json.dumps(top5)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_gAABjuy4I9RDF5riTfANOEke': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_Mph7lKKjVmRP6LiAnf6bH0LH': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_vMsuaof3Ao9NsGJzU5cz6cUD': 'file_storage/call_vMsuaof3Ao9NsGJzU5cz6cUD.json'}

exec(code, env_args)

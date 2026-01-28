code = """import pandas as pd
import json

# Load the stored JSON result file path
fp = var_call_9N5L1GPH6lnWJXDKBCllT1pb
# Read JSON
df = pd.read_json(fp)
# Parse dates with pandas
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# Clean CloseUSD
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Drop rows with missing
df = df.dropna(subset=['Date_parsed', 'CloseUSD'])
# Filter from 2000-01-01 inclusive
df = df[df['Date_parsed'] >= pd.Timestamp('2000-01-01')]
# Year-month period
df['ym'] = df['Date_parsed'].dt.to_period('M')
# For each Index and month, take the first trading day (minimum Date_parsed)
df_sorted = df.sort_values(['Index', 'Date_parsed'])
first_by_month = df_sorted.groupby(['Index', 'ym'], as_index=False).first()

results = []
# Country mapping for indices
country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

for idx, grp in first_by_month.groupby('Index'):
    months = len(grp)
    if months == 0:
        continue
    # total shares bought with $1 per month
    total_shares = (1.0 / grp['CloseUSD']).sum()
    # last available close for index from full df
    last_close = df[df['Index'] == idx].sort_values('Date_parsed').iloc[-1]['CloseUSD']
    final_value = total_shares * last_close
    total_contribution = months * 1.0
    return_factor = final_value / total_contribution if total_contribution > 0 else None
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'Months': months,
        'TotalContributionUSD': round(total_contribution, 2),
        'FinalValueUSD': round(float(final_value), 2),
        'ReturnFactor': round(float(return_factor), 4)
    })

# choose top 5 by FinalValueUSD
results_sorted = sorted(results, key=lambda x: x['FinalValueUSD'], reverse=True)
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_EjbIHnmUmuTqMAEbUCAsXUEa': ['index_trade'], 'var_call_vCmThs2u0JW3ggqX0IvG5ZO4': [{'idx': '000001.SS'}, {'idx': '399001.SZ'}, {'idx': 'GDAXI'}, {'idx': 'GSPTSE'}, {'idx': 'HSI'}, {'idx': 'IXIC'}, {'idx': 'J203.JO'}, {'idx': 'N100'}, {'idx': 'N225'}, {'idx': 'NSEI'}, {'idx': 'NYA'}, {'idx': 'SSMI'}, {'idx': 'TWII'}], 'var_call_5W7VmpiCmILy3QmO05OQ3TAQ': ['index_info'], 'var_call_sBcQDsZq2Ej0X3zC8VdUsEoX': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_9N5L1GPH6lnWJXDKBCllT1pb': 'file_storage/call_9N5L1GPH6lnWJXDKBCllT1pb.json'}

exec(code, env_args)

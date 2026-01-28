code = """import pandas as pd
import json

# Load the large JSON result from the storage variable (file path)
data_path = var_call_9njyeLZAuvGfrWFhY3tceKyT

df = pd.read_json(data_path)
# Ensure proper types
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to float (some values may be strings)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Prepare year-month
df['year_month'] = df['Date'].dt.to_period('M')

# For each index and month, pick the first trading day's CloseUSD
first_of_month = df.sort_values(['Index', 'Date']).groupby(['Index', 'year_month'], as_index=False).first()

# For each index compute monthly DCA with $1 per month
results = []
for idx, g in first_of_month.groupby('Index'):
    g = g.sort_values('year_month')
    # skip if no valid prices
    g = g.dropna(subset=['CloseUSD'])
    if g.empty:
        continue
    contributions = 1.0
    months = len(g)
    # shares bought each month
    shares = (contributions / g['CloseUSD']).sum()
    # last available price in whole dataset for this index (use latest date price)
    last_price_row = df[df['Index'] == idx].sort_values('Date').tail(1)
    if last_price_row.empty or pd.isna(last_price_row.iloc[0]['CloseUSD']):
        continue
    last_price = float(last_price_row.iloc[0]['CloseUSD'])
    final_value = shares * last_price
    total_contribution = contributions * months
    return_factor = final_value / total_contribution if total_contribution>0 else None
    results.append({
        'Index': idx,
        'Months': months,
        'FinalValue': final_value,
        'TotalContribution': total_contribution,
        'ReturnFactor': return_factor
    })

res_df = pd.DataFrame(results)
# If empty, print empty
if res_df.empty:
    out = []
else:
    res_df = res_df.sort_values('FinalValue', ascending=False).reset_index(drop=True)
    top5 = res_df.head(5)
    # Mapping index -> country (based on known mappings)
    mapping = {
        'N225': 'Japan',
        'HSI': 'Hong Kong (China)',
        '000001.SS': 'China (Shanghai)',
        '399001.SZ': 'China (Shenzhen)',
        'TWII': 'Taiwan',
        'GSPTSE': 'Canada',
        'NSEI': 'India',
        'GDAXI': 'Germany',
        'SSMI': 'Switzerland',
        'IXIC': 'United States',
        'NYA': 'United States',
        'J203.JO': 'South Africa',
        'N100': 'Netherlands (Euronext)'
    }
    out = []
    for _, r in top5.iterrows():
        idx = r['Index']
        out.append({
            'Index': idx,
            'Country': mapping.get(idx, 'Unknown'),
            'MonthsInvested': int(r['Months']),
            'TotalContributionUSD': round(float(r['TotalContribution']), 2),
            'FinalPortfolioValueUSD': round(float(r['FinalValue']), 2),
            'ReturnFactor': round(float(r['ReturnFactor']), 4)
        })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_meMT10KbBAzIJwk60L4Makg3': [{'idx': 'J203.JO'}, {'idx': 'N225'}, {'idx': 'GSPTSE'}, {'idx': 'NSEI'}, {'idx': 'GDAXI'}, {'idx': 'IXIC'}, {'idx': 'HSI'}, {'idx': 'NYA'}, {'idx': 'N100'}, {'idx': '399001.SZ'}, {'idx': '000001.SS'}, {'idx': 'SSMI'}, {'idx': 'TWII'}], 'var_call_9njyeLZAuvGfrWFhY3tceKyT': 'file_storage/call_9njyeLZAuvGfrWFhY3tceKyT.json', 'var_call_quiCbck52t78TwAhvQvLm13m': ['index_info'], 'var_call_KE1SzLDL0uPBegckAXSfK4SL': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

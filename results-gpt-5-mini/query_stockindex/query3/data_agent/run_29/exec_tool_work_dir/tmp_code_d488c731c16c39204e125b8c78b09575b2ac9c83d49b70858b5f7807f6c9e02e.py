code = """import pandas as pd
import json

# Load the large query result from the provided storage key variable
# The storage variable name provided by the tool call is var_call_fx337ww1e5I3O2iiPlwP4dDc
path = var_call_fx337ww1e5I3O2iiPlwP4dDc

data = pd.read_json(path)

# Ensure proper types
data['Date'] = pd.to_datetime(data['Date'])
# CloseUSD may be string; convert to float
data['CloseUSD'] = pd.to_numeric(data['CloseUSD'], errors='coerce')

# We'll perform monthly DCA investing of $1 per month starting from 2000-01-01 to each index's last available date.
results = []

for idx, group in data.groupby('Index'):
    g = group.sort_values('Date').reset_index(drop=True)
    # filter dates >= 2000-01-01 (already done in SQL) but ensure
    g = g[g['Date'] >= pd.Timestamp('2000-01-01')]
    if g.empty:
        continue
    # generate list of months from 2000-01 to last date in g
    start = pd.Timestamp('2000-01-01')
    end = g['Date'].max()
    months = pd.date_range(start=start, end=end, freq='MS')
    total_shares = 0.0
    total_invested = 0.0
    monthly_amount = 1.0
    actual_contributions = 0
    for m in months:
        # find first trading day in that month for this index
        month_start = m
        month_end = (m + pd.offsets.MonthEnd(0))
        mask = (g['Date'] >= month_start) & (g['Date'] <= month_end)
        month_rows = g.loc[mask]
        if month_rows.empty:
            continue
        first_row = month_rows.iloc[0]
        price = first_row['CloseUSD']
        if pd.isna(price) or price <= 0:
            continue
        shares_bought = monthly_amount / price
        total_shares += shares_bought
        total_invested += monthly_amount
        actual_contributions += 1
    if actual_contributions == 0:
        continue
    final_price = g.sort_values('Date').iloc[-1]['CloseUSD']
    final_value = total_shares * final_price
    total_return = (final_value - total_invested) / total_invested
    results.append({
        'Index': idx,
        'StartDate': start.strftime('%Y-%m-%d'),
        'EndDate': end.strftime('%Y-%m-%d'),
        'MonthsInvested': actual_contributions,
        'TotalInvestedUSD': round(total_invested,6),
        'FinalValueUSD': round(final_value,6),
        'TotalReturnPct': round(total_return * 100,4),
        'TotalReturnFactor': round(final_value/total_invested,6)
    })

# Create mapping from index symbol to country (inferred from exchange knowledge)
symbol_to_country = {
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands'  # N100 mapped to Euronext (headquartered in Amsterdam)
}

# Merge country info into results
for r in results:
    r['Country'] = symbol_to_country.get(r['Index'], 'Unknown')

# Sort by TotalReturnFactor descending and take top 5
results_sorted = sorted(results, key=lambda x: x['TotalReturnFactor'], reverse=True)
top5 = results_sorted[:5]

# Prepare final output list
output = []
for r in top5:
    output.append({
        'Index': r['Index'],
        'Country': r['Country'],
        'MonthsInvested': r['MonthsInvested'],
        'TotalInvestedUSD': r['TotalInvestedUSD'],
        'FinalValueUSD': r['FinalValueUSD'],
        'TotalReturnPct': r['TotalReturnPct'],
        'TotalReturnFactor': r['TotalReturnFactor']
    })

# Print result following required format
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_u51uaeKw99loSANvEkp3ovDz': ['index_trade'], 'var_call_q0hhhNQ9tq1HUkFaxL3K1f2P': ['index_info'], 'var_call_1ImrSKA42hl3LpMrdc5aFS1B': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_Xjs6fGbZh9VQe78fWlIgjduJ': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_fx337ww1e5I3O2iiPlwP4dDc': 'file_storage/call_fx337ww1e5I3O2iiPlwP4dDc.json'}

exec(code, env_args)

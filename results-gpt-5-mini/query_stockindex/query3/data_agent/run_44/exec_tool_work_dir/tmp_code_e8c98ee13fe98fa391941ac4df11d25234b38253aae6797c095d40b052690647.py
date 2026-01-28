code = """import pandas as pd
import json

# Load the large query result from the provided JSON file path variable
path = var_call_t8Z8BufUseou7bp3s0btvQ3V
# Read JSON list of records
df = pd.read_json(path)

# Ensure correct dtypes
df['CloseUSD'] = df['CloseUSD'].astype(float)
# Parse dates
df['Date'] = pd.to_datetime(df['Date'])

# Determine overall last date in dataset
last_date = df['Date'].max()

# Prepare month starts from 2000-01-01 to last_date
month_starts = pd.date_range(start='2000-01-01', end=last_date, freq='MS')

# Mapping from index symbol to country (inferred)
index_country = {
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

results = []

for idx, grp in df.groupby('Index'):
    grp = grp.sort_values('Date').reset_index(drop=True)
    shares = 0.0
    invest_amount = 1.0  # $1 per month
    invested_months = 0

    # Group by month using Period
    grp['month'] = grp['Date'].dt.to_period('M')

    for ms in month_starts:
        period = ms.to_period('M')
        month_rows = grp[grp['month'] == period]
        if month_rows.empty:
            # no trading days in this month for this index -> skip
            continue
        # pick the first trading day in the month
        buy_row = month_rows.loc[month_rows['Date'].idxmin()]
        price = float(buy_row['CloseUSD'])
        if price <= 0:
            continue
        shares += invest_amount / price
        invested_months += 1

    if invested_months == 0:
        continue

    total_invested = invested_months * invest_amount
    final_price = float(grp['CloseUSD'].iloc[-1])
    final_value = shares * final_price
    total_return = final_value / total_invested

    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'InvestedMonths': invested_months,
        'TotalInvestedUSD': round(total_invested, 2),
        'FinalValueUSD': round(final_value, 2),
        'ReturnMultiple': round(total_return, 4)
    })

# Sort by ReturnMultiple descending and take top 5
top5 = sorted(results, key=lambda x: x['ReturnMultiple'], reverse=True)[:5]

# Print in the required format as a JSON string
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_WmXrJbrRvtU9qhVeXu1FGuBW': ['index_trade'], 'var_call_SJHcblqnOHViFMnmk08ZrMX4': ['index_info'], 'var_call_t8Z8BufUseou7bp3s0btvQ3V': 'file_storage/call_t8Z8BufUseou7bp3s0btvQ3V.json', 'var_call_ve9CScmGxGJvwGBffH6Az3dB': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)

code = """import pandas as pd
import json

# Load the large query result from storage variable
# var_call_gPB08w0rVvPTi4wVY1indoI0 contains the filepath to the JSON file
fp = var_call_gPB08w0rVvPTi4wVY1indoI0

# Read JSON
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)
# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Parse dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter from 2000-01-01 onwards
df = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# If no data after 2000 for an index, it will be excluded
# We'll resample monthly taking last available CloseUSD in each month for each index
results = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    g = g.set_index('Date')
    # take last CloseUSD per month
    monthly = g['CloseUSD'].resample('M').last().dropna()
    if monthly.empty:
        continue
    # simulate monthly $1 investments at each month's price
    contributions = 0
    shares = 0.0
    for price in monthly:
        if price > 0 and not pd.isna(price):
            contributions += 1.0
            shares += 1.0 / price
    if contributions == 0:
        continue
    final_price = monthly.iloc[-1]
    final_value = shares * final_price
    return_ratio = final_value / contributions
    results.append({
        'Index': idx,
        'start': str(monthly.index[0].date()),
        'end': str(monthly.index[-1].date()),
        'months': int(len(monthly)),
        'total_invested': contributions,
        'final_value': final_value,
        'return_ratio': return_ratio
    })

# Sort by return_ratio descending and pick top 5
results_sorted = sorted(results, key=lambda x: x['return_ratio'], reverse=True)
top5 = results_sorted[:5]

# Map indices to countries (best-effort mapping based on common index symbols)
country_map = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong',
    'SSMI': 'Switzerland',
    'N100': 'Europe (Euronext)',
    '000001.SS': 'China',
    'TWII': 'Taiwan',
    '399001.SZ': 'China',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}

for r in top5:
    r['country'] = country_map.get(r['Index'], 'Unknown')
    # format numeric fields
    r['final_value'] = round(r['final_value'], 4)
    r['return_ratio'] = round(r['return_ratio'], 4)

# Prepare JSON-serializable output
out = []
for r in top5:
    out.append({
        'Index': r['Index'],
        'Country': r['country'],
        'Start': r['start'],
        'End': r['end'],
        'MonthsInvested': r['months'],
        'TotalInvestedUSD': r['total_invested'],
        'FinalValueUSD': r['final_value'],
        'ReturnRatio': r['return_ratio']
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d1BhDiC1ePlvcxU4sDL4Yo6I': ['index_trade'], 'var_call_d4FsDh95WWpiS5b542um0KNX': ['index_info'], 'var_call_5G5i4zzHZ0zIqUuZb9zB9b5W': [{'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n_rows': '13947'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n_rows': '13874'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n_rows': '12690'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n_rows': '10526'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n_rows': '8438'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n_rows': '8492'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n_rows': '7671'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n_rows': '5474'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n_rows': '5791'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n_rows': '5869'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n_rows': '5760'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n_rows': '3346'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n_rows': '2346'}], 'var_call_8HDjsNi7QAVLSWd7SMwlDQ40': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_gPB08w0rVvPTi4wVY1indoI0': 'file_storage/call_gPB08w0rVvPTi4wVY1indoI0.json'}

exec(code, env_args)

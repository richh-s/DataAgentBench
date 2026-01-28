code = """import json
import pandas as pd
from dateutil import parser

# Load the large query result from storage path
data_path = var_call_vgTr0V84Zx1CXuBrMFJPUAQJ
# read json
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Clean CloseUSD
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Parse dates robustly

def parse_date(x):
    if pd.isna(x):
        return pd.NaT
    try:
        return pd.to_datetime(x, utc=True)
    except Exception:
        try:
            return pd.to_datetime(parser.parse(x))
        except Exception:
            return pd.NaT

df['Date'] = df['Date'].apply(parse_date)
# Drop rows without date or price
df = df.dropna(subset=['Date','CloseUSD']).copy()
# Remove timezone for simplicity
df['Date'] = df['Date'].dt.tz_convert(None)

# We'll compute DCA investing $1 at the first available trading day on/after the 1st of each month
results = []

for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').reset_index(drop=True)
    # Determine start date: max(first available date, 2000-01-01)
    first_date = g['Date'].iloc[0]
    start = max(first_date, pd.Timestamp('2000-01-01'))
    end = g['Date'].iloc[-1]
    # Generate months from start to end inclusive
    periods = pd.period_range(start=start.to_period('M'), end=end.to_period('M'), freq='M')
    shares = 0.0
    months_invested = 0
    invested = 0.0
    for p in periods:
        month_start = p.to_timestamp()
        # find first trading day on or after month_start
        candidate = g[g['Date'] >= month_start]
        if candidate.empty:
            continue
        buy_row = candidate.iloc[0]
        price = buy_row['CloseUSD']
        if pd.isna(price) or price <= 0:
            continue
        shares += 1.0 / price
        invested += 1.0
        months_invested += 1
    if months_invested == 0:
        continue
    last_price = g['CloseUSD'].iloc[-1]
    final_value = shares * last_price
    return_factor = final_value / invested if invested>0 else None
    results.append({
        'Index': idx,
        'StartDate': start.strftime('%Y-%m-%d'),
        'EndDate': end.strftime('%Y-%m-%d'),
        'MonthsInvested': months_invested,
        'TotalInvested': round(invested,2),
        'FinalValue': round(final_value,4),
        'ReturnFactor': round(return_factor,4)
    })

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('ReturnFactor', ascending=False).reset_index(drop=True)
# Map indices to countries (best-effort mapping)
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands',
    'J203.JO': 'South Africa'
}

# attach country
res_df['Country'] = res_df['Index'].map(country_map).fillna('Unknown')

# take top 5
top5 = res_df.head(5)
# prepare output
out = []
for _, r in top5.iterrows():
    out.append({
        'Index': r['Index'],
        'Country': r['Country'],
        'StartDate': r['StartDate'],
        'EndDate': r['EndDate'],
        'MonthsInvested': int(r['MonthsInvested']),
        'TotalInvestedUSD': r['TotalInvested'],
        'FinalValueUSD': r['FinalValue'],
        'ReturnFactor': r['ReturnFactor']
    })

import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_J7rheE46wo4szXuNitXvtNnK': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}], 'var_call_vgTr0V84Zx1CXuBrMFJPUAQJ': 'file_storage/call_vgTr0V84Zx1CXuBrMFJPUAQJ.json', 'var_call_0K79qAhNhcmPb0QEVP61Pw3C': ['index_info'], 'var_call_n7FLCbF8WsbSNNp9Vb8gjaSt': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

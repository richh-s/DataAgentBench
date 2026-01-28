code = """import json
import pandas as pd
from datetime import datetime

# Load the large query result from the storage variable (file path)
data_path = var_call_S3I3gVPIHeguOqFCJ16VJqby
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Load index info mapping (exchange/currency) though we mainly need country mapping separately
index_info = var_call_n7kO376NQFwJkX0Ph71t6FT4

# Build DataFrame
df = pd.DataFrame(records)
# Normalize column names
df = df.rename(columns={"Index": 'Index', 'Date': 'Date', 'CloseUSD': 'CloseUSD'})

# Parse CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Parse Date using pandas (handles many formats)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with missing dates or prices
df = df.dropna(subset=['Date', 'CloseUSD']).copy()

# Consider investments starting from 2000-01-01
global_start = pd.Timestamp('2000-01-01')

# Mapping index symbol -> country (inferred from common index conventions)
index_country_map = {
    '000001.SS': 'China',        # Shanghai Composite (Shanghai Stock Exchange)
    '399001.SZ': 'China',        # Shenzhen Composite (Shenzhen Stock Exchange)
    'GDAXI': 'Germany',          # DAX (Frankfurt)
    'GSPTSE': 'Canada',          # S&P/TSX (Toronto)
    'HSI': 'Hong Kong',          # Hang Seng (Hong Kong)
    'IXIC': 'United States',     # NASDAQ Composite (USA)
    'J203.JO': 'South Africa',   # Johannesburg
    'N100': 'Netherlands',       # Euronext N100 (pan-Europe) -> mapped to Netherlands
    'N225': 'Japan',             # Nikkei 225 (Tokyo)
    'NSEI': 'India',             # NIFTY 50 (National Stock Exchange of India)
    'NYA': 'United States',      # NYSE Composite
    'SSMI': 'Switzerland',       # SMI (SIX Swiss)
    'TWII': 'Taiwan'             # TAIEX (Taiwan)
}

results = []

# Fixed monthly contribution (amount doesn't change ranking)
contrib = 1.0

for idx, group in df.groupby('Index'):
    grp = group.sort_values('Date').reset_index(drop=True)
    # Investment start is max(global_start, earliest available date)
    start_date = max(global_start, grp['Date'].iloc[0])
    end_date = grp['Date'].iloc[-1]
    if start_date > end_date:
        continue
    # Build month starts from start_date's month start to end_date's month start
    month_starts = pd.date_range(start=start_date.replace(day=1), end=end_date, freq='MS')
    shares_acquired = 0.0
    purchases = 0
    for m in month_starts:
        # find first trading day in the month (Date >= m and < next month start)
        next_m = (m + pd.offsets.MonthBegin(1))
        mask = (grp['Date'] >= m) & (grp['Date'] < next_m)
        month_rows = grp.loc[mask]
        if month_rows.empty:
            # if no trading day in that calendar month (rare), try to find the first trading day after m but before next_m + 7 days
            continue
        price = month_rows.iloc[0]['CloseUSD']
        if pd.isna(price) or price <= 0:
            continue
        shares_acquired += contrib / price
        purchases += 1
    if purchases == 0:
        continue
    total_invested = purchases * contrib
    last_price = grp['CloseUSD'].iloc[-1]
    final_value = shares_acquired * last_price
    return_multiplier = final_value / total_invested
    pct_return = (final_value - total_invested) / total_invested * 100.0
    results.append({
        'Index': idx,
        'Country': index_country_map.get(idx, 'Unknown'),
        'Months': purchases,
        'Total_Invested_USD': round(total_invested, 2),
        'Final_Value_USD': round(final_value, 2),
        'Return_Multiplier': round(return_multiplier, 4),
        'Total_Return_pct': round(pct_return, 2)
    })

# Sort by return multiplier descending and pick top 5
results_sorted = sorted(results, key=lambda x: x['Return_Multiplier'], reverse=True)
top5 = results_sorted[:5]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_4sXUwhUpcIfWDQSzqo4r2lxE': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'rows': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'rows': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'rows': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'rows': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'rows': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'rows': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'rows': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'rows': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'rows': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'rows': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'rows': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'rows': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'rows': '5869'}], 'var_call_S3I3gVPIHeguOqFCJ16VJqby': 'file_storage/call_S3I3gVPIHeguOqFCJ16VJqby.json', 'var_call_C03ykXmWZIowqDiJlnfbVLU8': ['index_info'], 'var_call_n7kO376NQFwJkX0Ph71t6FT4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

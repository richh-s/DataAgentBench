code = """import pandas as pd
import json

# Load the large query result from the provided storage key (file path)
file_path = var_call_GVK2KHR8B6gmgULhC4yN4u67
raw = pd.read_json(file_path)

# Also load index list info (min/max) if needed
idx_ranges = pd.DataFrame(var_call_U3Hj1YsT4koSUklaAYkcz88C)
idx_info = pd.DataFrame(var_call_gpkbTwyBD6Z5KGWaz40V3H4b)

# Clean and parse dates and CloseUSD
raw['Date_parsed'] = pd.to_datetime(raw['Date'], errors='coerce')
raw['CloseUSD'] = pd.to_numeric(raw['CloseUSD'], errors='coerce')
raw = raw.dropna(subset=['Date_parsed','CloseUSD'])
raw = raw.sort_values(['Index','Date_parsed'])

# Define monthly investment simulation starting from 2000-01-01
start_date = pd.Timestamp('2000-01-01')
monthly_amount = 100.0  # invest $100 each month

# Country mapping for known indices (inferred from exchange knowledge)
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

results = []
for idx, grp in raw.groupby('Index'):
    grp = grp.sort_values('Date_parsed').reset_index(drop=True)
    # if latest date before start_date, skip
    if grp['Date_parsed'].max() < start_date:
        continue
    # Generate month starts from 2000-01-01 to last available date
    months = pd.date_range(start=start_date, end=grp['Date_parsed'].max(), freq='MS')
    total_shares = 0.0
    invested_months = 0
    for m in months:
        # find first trading day on or after month start
        cand = grp[grp['Date_parsed'] >= m]
        if cand.empty:
            continue
        price = float(cand.iloc[0]['CloseUSD'])
        if price <= 0 or pd.isna(price):
            continue
        shares = monthly_amount / price
        total_shares += shares
        invested_months += 1
    if invested_months == 0:
        continue
    last_price = float(grp.iloc[-1]['CloseUSD'])
    final_value = total_shares * last_price
    total_invested = invested_months * monthly_amount
    multiple = final_value / total_invested if total_invested>0 else None
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'InvestedMonths': invested_months,
        'TotalInvestedUSD': round(total_invested,2),
        'FinalValueUSD': round(final_value,2),
        'Multiple': round(multiple,4)
    })

# Sort by Multiple descending and pick top 5
results_sorted = sorted(results, key=lambda x: x['Multiple'] if x['Multiple'] is not None else -999, reverse=True)
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_joMFZVAWG25DcOXgr63beEYn': ['index_trade'], 'var_call_fTkFQFHpWDXWu2fxHsjBDC7I': ['index_info'], 'var_call_U3Hj1YsT4koSUklaAYkcz88C': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_call_GVK2KHR8B6gmgULhC4yN4u67': 'file_storage/call_GVK2KHR8B6gmgULhC4yN4u67.json', 'var_call_gpkbTwyBD6Z5KGWaz40V3H4b': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

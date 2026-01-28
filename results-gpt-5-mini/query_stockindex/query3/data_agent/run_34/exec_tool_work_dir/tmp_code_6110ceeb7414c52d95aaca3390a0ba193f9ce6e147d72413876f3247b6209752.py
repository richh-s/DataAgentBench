code = """import pandas as pd
import json

# Load query result from storage
fp = var_call_qfEOMEZmXZ9YfIdDATWSbMJM
with open(fp, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Clean Date strings: remove ' at ...' and ', 00:00'
df['Date_clean'] = df['Date'].astype(str).str.replace(r', 00:00$', '', regex=True).str.replace(r' at .*$', '', regex=True).str.strip()
# Parse dates
df['Date_parsed'] = pd.to_datetime(df['Date_clean'], errors='coerce', infer_datetime_format=True)
# Convert CloseUSD to numeric
df['CloseUSD_num'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Drop rows without valid date or price
df = df.dropna(subset=['Date_parsed', 'CloseUSD_num']).copy()
# Standardize index column
indices = df['Index'].unique().tolist()

results = []

for idx in indices:
    dfi = df[df['Index'] == idx].copy()
    dfi = dfi.sort_values('Date_parsed')
    dfi = dfi.set_index('Date_parsed')
    # Monthly last available close: resample by month end
    monthly = dfi['CloseUSD_num'].resample('M').last()
    # Determine start date: max(first available, 2000-01-01)
    first_avail = monthly.first_valid_index()
    last_avail = monthly.last_valid_index()
    if pd.isna(first_avail) or pd.isna(last_avail):
        continue
    start = max(first_avail, pd.Timestamp('2000-01-01'))
    # Generate monthly period end range from start to last_avail
    month_ends = pd.date_range(start=start, end=last_avail, freq='M')
    monthly = monthly.reindex(month_ends)
    # Drop months with no price
    monthly = monthly.dropna()
    if len(monthly) == 0:
        continue
    # Invest $1 each month at that month's last close
    shares = (1.0 / monthly).sum()
    total_invested = float(len(monthly))
    # Final value use last available close price in full data (most recent trading day)
    last_price = float(dfi['CloseUSD_num'].iloc[-1])
    final_value = shares * last_price
    return_ratio = final_value / total_invested if total_invested>0 else None
    total_return_pct = (final_value - total_invested) / total_invested * 100 if total_invested>0 else None
    results.append({
        'Index': idx,
        'start_month': str(monthly.index[0].date()),
        'last_date': str(dfi.index[-1].date()),
        'months_invested': int(total_invested),
        'total_invested_usd': round(total_invested, 2),
        'final_value_usd': round(final_value, 2),
        'return_ratio': round(return_ratio, 4),
        'total_return_pct': round(total_return_pct, 2)
    })

# Country mapping (best-effort based on index symbols)
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong (China)',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands/Europe',
    'J203.JO': 'South Africa',
    'NSEI': 'India'
}

# Rank by return_ratio
resdf = pd.DataFrame(results)
resdf = resdf.sort_values('return_ratio', ascending=False).reset_index(drop=True)
# Attach country
resdf['country'] = resdf['Index'].map(country_map).fillna('Unknown')

# Select top 5
top5 = resdf.head(5)
# Prepare output list
out = []
for _, row in top5.iterrows():
    out.append({
        'Index': row['Index'],
        'Country': row['country'],
        'MonthsInvested': int(row['months_invested']),
        'TotalInvestedUSD': float(row['total_invested_usd']),
        'FinalValueUSD': float(row['final_value_usd']),
        'ReturnRatio': float(row['return_ratio']),
        'TotalReturnPct': float(row['total_return_pct']),
        'LastDate': row['last_date']
    })

# Print result in required format
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_rZcyRbgHExjOkWbtQsuV6zmn': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'days': '2346'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'days': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'days': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'days': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'days': '8438'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'days': '8492'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'days': '13947'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'days': '12690'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'days': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'days': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'days': '5869'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'days': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'days': '5760'}], 'var_call_qfEOMEZmXZ9YfIdDATWSbMJM': 'file_storage/call_qfEOMEZmXZ9YfIdDATWSbMJM.json'}

exec(code, env_args)

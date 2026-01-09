code = """import pandas as pd, json
import os

def parse_date_col(sr):
    # vectorized parse with multiple attempts
    s = sr.astype(str)
    dt = pd.to_datetime(s, errors='coerce')
    mask = dt.isna()
    if mask.any():
        dt2 = pd.to_datetime(s[mask], format='%d %b %Y, %H:%M', errors='coerce')
        dt.loc[mask] = dt2
    mask = dt.isna()
    if mask.any():
        dt2 = pd.to_datetime(s[mask], format='%B %d, %Y at %I:%M %p', errors='coerce')
        dt.loc[mask] = dt2
    return dt

# Load trades
path = var_call_s7RcaLSJMn9DwF68DGS7pPZi
if isinstance(path, str) and os.path.exists(path):
    df = pd.read_json(path)
else:
    df = pd.DataFrame(var_call_s7RcaLSJMn9DwF68DGS7pPZi)

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['dt'] = parse_date_col(df['Date'])
df = df.dropna(subset=['dt','CloseUSD'])

# Monthly contributions from 2000-01 onward
start = pd.Timestamp('2000-01-01')
df = df[df['dt']>=start]

# For each index and month, use last CloseUSD in that month
# First sort
df = df.sort_values(['Index','dt'])
df['month'] = df['dt'].dt.to_period('M').dt.to_timestamp('M')
monthly_last = df.groupby(['Index','month'], as_index=False)['CloseUSD'].last()

# Determine common end month per index (last available month)
# Simulate investing $1 each month: shares += 1/price
monthly_last['inv'] = 1.0
monthly_last['shares_add'] = monthly_last['inv'] / monthly_last['CloseUSD']
shares = monthly_last.groupby('Index', as_index=False)['shares_add'].sum().rename(columns={'shares_add':'total_shares'})
last_price = monthly_last.sort_values(['Index','month']).groupby('Index', as_index=False).tail(1)[['Index','CloseUSD','month']].rename(columns={'CloseUSD':'last_price','month':'last_month'})
first_month = monthly_last.sort_values(['Index','month']).groupby('Index', as_index=False).head(1)[['Index','month']].rename(columns={'month':'first_month'})
months_ct = monthly_last.groupby('Index', as_index=False).size().rename(columns={'size':'n_months'})

res = shares.merge(last_price, on='Index').merge(first_month, on='Index').merge(months_ct, on='Index')
res['total_invested'] = res['n_months']*1.0
res['final_value'] = res['total_shares']*res['last_price']
res['multiple'] = res['final_value']/res['total_invested']

# Only indices with data starting in 2000-01 (or earlier, but filtered so first month >=2000-01). To ensure "since 2000" we require first_month == 2000-01-31
res = res[res['first_month']<=pd.Timestamp('2000-01-31')]
res = res.sort_values('multiple', ascending=False)

# Map Index to country/exchange using known mapping
country_map = {
    'NYA':'United States',
    'IXIC':'United States',
    'GSPTSE':'Canada',
    'GDAXI':'Germany',
    'N225':'Japan',
    'HSI':'Hong Kong',
    'SSMI':'Switzerland',
    'N100':'Europe (Euronext)',
    '000001.SS':'China',
    '399001.SZ':'China',
    'TWII':'Taiwan',
    'NSEI':'India',
    'J203.JO':'South Africa'
}
res['country'] = res['Index'].map(country_map)

out = res.head(5)[['Index','country','multiple','first_month','last_month','n_months']].copy()
# Convert timestamps to strings
out['first_month']=out['first_month'].dt.strftime('%Y-%m')
out['last_month']=out['last_month'].dt.strftime('%Y-%m')

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_gmGkDg64O3j8lJOAvpfXdVWY': ['index_info'], 'var_call_ttZ8XD7AA6a59qDWswh4Ys4o': ['index_trade'], 'var_call_0dvFLPs7DP7xXns2MMlkVEZ3': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_0cEeuOTbFge9QSne0YkmCCsR': [{'Index': 'NYA', 'min_date_raw': '01 Apr 1969, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'N225', 'min_date_raw': '01 Apr 1971, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'IXIC', 'min_date_raw': '01 Apr 1974, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'GSPTSE', 'min_date_raw': '01 Apr 1981, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'GDAXI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'SSMI', 'min_date_raw': '01 Apr 1996, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': '000001.SS', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'N100', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'NSEI', 'min_date_raw': '01 Apr 2014, 00:00', 'max_date_raw': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'J203.JO', 'min_date_raw': '01 Apr 2016, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '2346'}], 'var_call_junLQpccFiCWlJqeBAptH7Hr': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'CloseUSD': '338.92301274'}], 'var_call_UaCAOfQTqPIQ9uo4VkQWM0rz': {'note': 'ready'}, 'var_call_s7RcaLSJMn9DwF68DGS7pPZi': 'file_storage/call_s7RcaLSJMn9DwF68DGS7pPZi.json'}

exec(code, env_args)

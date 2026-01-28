code = """import json, pandas as pd

# load full trade data
path = var_call_PxHls2I94I6Hju5uaH7vLy2j
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# parse mixed date formats
s = df['Date'].astype(str)
# try multiple parses
p1 = pd.to_datetime(s, errors='coerce', format='%Y-%m-%d %H:%M:%S')
p2 = pd.to_datetime(s, errors='coerce', format='%Y-%m-%d')
p3 = pd.to_datetime(s, errors='coerce', format='%d %b %Y, %H:%M')
p4 = pd.to_datetime(s, errors='coerce', format='%B %d, %Y at %I:%M %p')
dt = p1.fillna(p2).fillna(p3).fillna(p4)
df['dt'] = dt

df = df.dropna(subset=['dt','CloseUSD'])
# filter since 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['dt']>=start]

# monthly DCA: invest 1 unit on first trading day of each month
# shares purchased = 1 / price_on_invest_day
# final value = sum(shares)*last_price
results = []
for idx, g in df.sort_values('dt').groupby('Index'):
    g = g.sort_values('dt')
    g['month'] = g['dt'].dt.to_period('M')
    first = g.groupby('month').head(1)
    if first.empty:
        continue
    # require coverage from 2000-01 to last month? We'll compute with available months since 2000.
    shares = (1.0 / first['CloseUSD']).sum()
    last_price = g.iloc[-1]['CloseUSD']
    final_value = shares * last_price
    total_invested = float(len(first))
    multiple = final_value / total_invested if total_invested>0 else None
    results.append({'Index': idx, 'months_invested': int(total_invested), 'end_date': str(g.iloc[-1]['dt'].date()), 'end_price_usd': float(last_price), 'final_value_per_$1_monthly': float(final_value), 'return_multiple': float(multiple)})

resdf = pd.DataFrame(results).sort_values('return_multiple', ascending=False)

# map index to country based on known major indices/exchanges in dataset
country_map = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    'GDAXI': 'Germany',
    'N100': 'Europe (Euronext)',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}

# top 5
out = resdf.head(5).copy()
out['Country'] = out['Index'].map(country_map)

answer = out[['Index','Country','return_multiple','months_invested','end_date']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_EgpSaGQC2hMP8GcChqOZD9KP': ['index_info'], 'var_call_2hme4jvoA33E8ULSicksplAY': ['index_trade'], 'var_call_moVMnLNhMAhQVerr6pRcnk3i': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_X3TfYmr4CxD4Q1o8Ds8TTMwx': [{'Index': 'N225', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '13874'}, {'Index': 'GSPTSE', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '10526'}, {'Index': 'NSEI', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '3346'}, {'Index': 'GDAXI', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '8438'}, {'Index': 'HSI', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '8492'}, {'Index': 'IXIC', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '12690'}, {'Index': 'NYA', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '13947'}, {'Index': '000001.SS', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '5791'}, {'Index': 'SSMI', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '7671'}, {'Index': 'TWII', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '5869'}, {'Index': 'N100', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '5474'}, {'Index': '399001.SZ', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '5760'}, {'Index': 'J203.JO', 'min_date': 'NaT', 'max_date': 'NaT', 'n_rows': '2346'}], 'var_call_tzJqQkVynO3ZTSsdxu0zNNrl': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_PxHls2I94I6Hju5uaH7vLy2j': 'file_storage/call_PxHls2I94I6Hju5uaH7vLy2j.json'}

exec(code, env_args)

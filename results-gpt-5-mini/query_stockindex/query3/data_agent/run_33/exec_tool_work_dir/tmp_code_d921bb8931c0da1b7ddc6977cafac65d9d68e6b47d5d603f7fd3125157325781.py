code = """import pandas as pd, json
fp = var_call_FxNoPUSnmUnedv8fDu4W9jCA
# load JSON file
df = pd.read_json(fp)
# Ensure columns
df = df[['Index','Date','CloseUSD']]
# Clean CloseUSD to float
def to_float(x):
    try:
        return float(x)
    except:
        return None

df['CloseUSD'] = df['CloseUSD'].apply(to_float)
# Parse dates robustly
dates = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# try cleaning ' at 12:00 AM' patterns
mask_nat = dates.isna()
if mask_nat.any():
    cleaned = df.loc[mask_nat,'Date'].str.replace(' at 12:00 AM','', regex=False)
    parsed = pd.to_datetime(cleaned, errors='coerce', infer_datetime_format=True)
    dates.loc[mask_nat] = parsed
# try other replacements
mask_nat = dates.isna()
if mask_nat.any():
    cleaned = df.loc[mask_nat,'Date'].str.replace(',','', regex=False)
    parsed = pd.to_datetime(cleaned, errors='coerce', infer_datetime_format=True)
    dates.loc[mask_nat] = parsed

df['pdate'] = dates
# drop rows without date or close
df = df.dropna(subset=['pdate','CloseUSD'])
# filter from 2000-01-01
df = df[df['pdate'] >= pd.Timestamp('2000-01-01')].copy()
# compute first trading day of each month per index
df['month'] = df['pdate'].dt.to_period('M')
first_days = df.sort_values(['Index','pdate']).groupby(['Index','month']).first().reset_index()
# compute total shares purchased assuming $1 per month invested at that day's CloseUSD
first_days = first_days[first_days['CloseUSD']>0]
shares = first_days.groupby('Index').apply(lambda g: pd.Series({
    'months': len(g),
    'total_shares': (1.0/g['CloseUSD']).sum(),
    'last_date': g['pdate'].max()
})).reset_index()
# need last available close per index (overall)
last_close = df.sort_values(['Index','pdate']).groupby('Index').last().reset_index()[['Index','pdate','CloseUSD']]
last_close = last_close.rename(columns={'pdate':'last_pdate','CloseUSD':'last_close'})
res = pd.merge(shares, last_close, on='Index', how='left')
res['final_value'] = res['total_shares'] * res['last_close']
res['total_invested'] = res['months'] * 1.0
res['multiple'] = res['final_value'] / res['total_invested']
res = res.sort_values('multiple', ascending=False)
# take top 10 to inspect mapping
top5 = res.head(5).copy()
# map indices to countries using heuristics
mapping = {
    'N225':'Japan', 'HSI':'Hong Kong', '000001.SS':'China', '399001.SZ':'China',
    'GSPC':'United States','^GSPC':'United States','SPX':'United States','DJI':'United States',
    'IXIC':'United States','FTSE':'United Kingdom','FTSE100':'United Kingdom','DAX':'Germany','GDAXI':'Germany',
    'NQ100':'United States','SSEC':'China','SSE':'China','S&P/TSX':'Canada','TSX':'Canada','AORD':'Australia',
    'KOSPI':'South Korea','TWII':'Taiwan','SENSEX':'India','BSESN':'India','IBEX':'Spain','SMI':'Switzerland',
    'JSE':'South Africa','IBOV':'Brazil','MXX':'Mexico'
}

def guess_country(idx):
    if idx in mapping:
        return mapping[idx]
    up = idx.upper()
    if '.SS' in up or up.startswith('000') or 'SH' in up:
        return 'China'
    if '.SZ' in up or up.startswith('399'):
        return 'China'
    if up in ('N225','NIKKEI','NIKKEI225'):
        return 'Japan'
    if 'HSI' in up or 'HANG' in up:
        return 'Hong Kong'
    if 'FTSE' in up or 'LSE' in up:
        return 'United Kingdom'
    if 'DAX' in up or 'DE' in up:
        return 'Germany'
    if 'S&P' in up or 'GSPC' in up or 'SPX' in up or 'DJI' in up or 'IXIC' in up or 'NASDAQ' in up:
        return 'United States'
    if 'KOSPI' in up or 'KR' in up:
        return 'South Korea'
    if 'TW' in up or 'TWN' in up or 'TWII' in up:
        return 'Taiwan'
    if 'TSX' in up or 'TO' in up:
        return 'Canada'
    if 'SENSEX' in up or 'BSE' in up:
        return 'India'
    return 'Unknown'

out = []
for _, row in top5.iterrows():
    idx = row['Index']
    out.append({'Index': idx, 'months': int(row['months']), 'multiple': float(row['multiple']), 'final_value': float(row['final_value']), 'country': guess_country(idx)})

result_json = json.dumps(out)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_OJtpbLnFSrvMOv8fgn9myOWS': ['index_trade'], 'var_call_FxNoPUSnmUnedv8fDu4W9jCA': 'file_storage/call_FxNoPUSnmUnedv8fDu4W9jCA.json', 'var_call_aB8VYhpZHVe6wZ0a2e1MPpCP': ['index_info'], 'var_call_9AZBgkQIsQzKciW6i6i2KYE5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

code = """import json, pandas as pd
from pathlib import Path

# Load full trade data
p = Path(var_call_FgAkpNgvjx25H1oozUQVh6jp)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)

# Parse and clean
# CloseUSD is string in export
for c in ['CloseUSD']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
df = df.dropna(subset=['Date','CloseUSD','Index'])

# Filter since 2000
start = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start].copy()

# Create month period
df['Month'] = df['Date'].dt.to_period('M').dt.to_timestamp()

# Monthly contribution: buy at first available trading day of month (using CloseUSD)
monthly = (df.sort_values(['Index','Date'])
             .groupby(['Index','Month'], as_index=False)
             .first()[['Index','Month','CloseUSD']])

# Need final price per index (last available)
final = (df.sort_values(['Index','Date'])
           .groupby('Index', as_index=False)
           .last()[['Index','Date','CloseUSD']]
           .rename(columns={'CloseUSD':'FinalCloseUSD','Date':'FinalDate'}))

# Shares accumulated with $1 per month DCA
monthly['Shares'] = 1.0 / monthly['CloseUSD']
shares = monthly.groupby('Index', as_index=False)['Shares'].sum()

# Total invested
invested = monthly.groupby('Index', as_index=False).size().rename(columns={'size':'Months'})
invested['TotalInvestedUSD'] = invested['Months'] * 1.0

# Portfolio value
res = shares.merge(final, on='Index').merge(invested, on='Index')
res['FinalValueUSD'] = res['Shares'] * res['FinalCloseUSD']
res['Multiple'] = res['FinalValueUSD'] / res['TotalInvestedUSD']

# Keep indices with at least e.g. 12 months of data since 2000
res = res[res['Months'] >= 12].copy()
res = res.sort_values('Multiple', ascending=False)

# Top 5
top5 = res.head(5).copy()

# Map index symbol to exchange/country using known major indices from hint
symbol_to_exchange_country = {
    'N225': ('Tokyo Stock Exchange', 'Japan'),
    'HSI': ('Hong Kong Stock Exchange', 'Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange', 'China'),
    '399001.SZ': ('Shenzhen Stock Exchange', 'China'),
    '^GSPC': ('New York Stock Exchange', 'United States'),
    '^IXIC': ('NASDAQ', 'United States'),
    '^DJI': ('New York Stock Exchange', 'United States'),
    '^FTSE': ('Euronext', 'United Kingdom'),
    '^FCHI': ('Euronext', 'France'),
    '^GDAXI': ('Frankfurt Stock Exchange', 'Germany'),
    '^STOXX50E': ('Euronext', 'Eurozone'),
    '^NSEI': ('National Stock Exchange of India', 'India'),
    '^BSESN': ('National Stock Exchange of India', 'India'),
    '^KS11': ('Korea Exchange', 'South Korea'),
    '^TWII': ('Taiwan Stock Exchange', 'Taiwan'),
    '^GSPTSE': ('Toronto Stock Exchange', 'Canada'),
    '^SSMI': ('SIX Swiss Exchange', 'Switzerland'),
    '^JN0U.JO': ('Johannesburg Stock Exchange', 'South Africa'),
}

def map_country(sym):
    v = symbol_to_exchange_country.get(sym)
    if v:
        return v[1]
    # heuristic for China tickers
    if sym.endswith('.SS'):
        return 'China'
    if sym.endswith('.SZ'):
        return 'China'
    return None

top5['Country'] = top5['Index'].map(map_country)

out = top5[['Index','Multiple','Months','FinalDate','Country']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_G7Dbs7ckzOJe2QRBaf9UaniP': ['index_info'], 'var_call_jg1lOrteebhXgHUke4j1LSsy': ['index_trade'], 'var_call_mehMoX2wpUONbFtCYIuGQyB0': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_6jgCD1NbaK8IFy4uL1ioQ11t': 'file_storage/call_6jgCD1NbaK8IFy4uL1ioQ11t.json', 'var_call_FgAkpNgvjx25H1oozUQVh6jp': 'file_storage/call_FgAkpNgvjx25H1oozUQVh6jp.json', 'var_call_kWjoWSgjfz8I1tqJ6oPP9960': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

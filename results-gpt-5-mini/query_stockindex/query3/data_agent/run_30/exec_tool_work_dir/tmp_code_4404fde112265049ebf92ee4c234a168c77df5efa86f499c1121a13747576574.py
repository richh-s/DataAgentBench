code = """import json
import pandas as pd
from datetime import datetime

# Load the large query result from indextrade_database
path = var_call_2g9ffF3I9FhSWEh8h7RQ09lu
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Convert types
df['Date'] = pd.to_datetime(df['Date'])
# Some numeric fields may be strings
for col in ['Open','High','Low','Close','Adj Close','CloseUSD']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Keep records from 2000-01-01 onwards (already done in query)
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Function to compute monthly DCA investing $1 at first trading day closeUSD each month
results = []
for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').copy()
    # create year-month period
    g['year_month'] = g['Date'].dt.to_period('M')
    # For each month, take first trading day
    first_days = g.groupby('year_month').first().reset_index()
    # Only consider months on/after the first available month (which will be >=2000-01)
    # But ensure we only start from 2000-01 onwards
    first_days = first_days[first_days['Date'] >= pd.Timestamp('2000-01-01')]
    # Use CloseUSD for purchases, skip months with missing or nonpositive CloseUSD
    valid = first_days[first_days['CloseUSD'].notna() & (first_days['CloseUSD']>0)].copy()
    months_invested = len(valid)
    if months_invested == 0:
        continue
    # invest $1 per month
    valid['shares_bought'] = 1.0 / valid['CloseUSD']
    total_shares = valid['shares_bought'].sum()
    invested = float(months_invested)
    # final value use last available CloseUSD in original group
    last_price_row = g[g['CloseUSD'].notna()].iloc[-1:]
    if last_price_row.empty:
        continue
    last_price = float(last_price_row['CloseUSD'].values[0])
    final_value = total_shares * last_price
    return_factor = final_value / invested if invested>0 else None
    percent_return = (final_value - invested) / invested * 100.0
    results.append({'Index': idx, 'months_invested': months_invested, 'invested': invested,
                    'total_shares': total_shares, 'last_price': last_price,
                    'final_value': final_value, 'return_factor': return_factor,
                    'percent_return': percent_return})

res_df = pd.DataFrame(results)
# Filter to indices that had at least 12 months of investing since 2000
res_df = res_df[res_df['months_invested'] >= 12]
# Sort by return_factor desc
res_df = res_df.sort_values('return_factor', ascending=False).reset_index(drop=True)

# Prepare mapping heuristics for index -> country
def map_index_to_country(index):
    ix = index.upper()
    if '.SS' in ix or ix.endswith('.SS') or ix.startswith('000') or ix.startswith('399'):
        return 'China'
    if '.SZ' in ix or ix.endswith('.SZ'):
        return 'China'
    if ix in ('N225','^N225','NI225'):
        return 'Japan'
    if ix in ('HSI','^HSI'):
        return 'Hong Kong'
    if ix in ('GSPC','^GSPC','SPX','^SPX'):
        return 'United States'
    if ix in ('IXIC','NASDAQ'):
        return 'United States'
    if ix in ('DJI','^DJI'):
        return 'United States'
    if 'FTSE' in ix or ix.startswith('FTSE'):
        return 'United Kingdom'
    if ix in ('DAX','GDAXI'):
        return 'Germany'
    if ix in ('NSEI','^NSEI','NIFTY'):
        return 'India'
    if ix in ('KS11','KOSPI'):
        return 'South Korea'
    if ix in ('TWII',):
        return 'Taiwan'
    if ix in ('SSMI',):
        return 'Switzerland'
    if ix in ('GSPTSE', '^GSPTSE', 'TSX'):
        return 'Canada'
    if ix in ('JSE',):
        return 'South Africa'
    # default unknown
    return 'Unknown'

# Take top 20 to inspect mapping quality
top5 = res_df.head(5).copy()
output = []
for _, row in top5.iterrows():
    idx = row['Index']
    country = map_index_to_country(idx)
    output.append({'Index': idx,
                   'Country': country,
                   'months_invested': int(row['months_invested']),
                   'invested_total_usd': round(float(row['invested']),2),
                   'final_value_usd': round(float(row['final_value']),2),
                   'return_factor': round(float(row['return_factor']),4),
                   'percent_return': round(float(row['percent_return']),2)})

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_lesJjYxA2x0lMHow5E2Pay5v': ['index_trade'], 'var_call_2g9ffF3I9FhSWEh8h7RQ09lu': 'file_storage/call_2g9ffF3I9FhSWEh8h7RQ09lu.json', 'var_call_8RAXiWWTRLKO5UM70Fx0MlTj': ['index_info'], 'var_call_KXvbKaumkPUFZZPoTDM0BsqG': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

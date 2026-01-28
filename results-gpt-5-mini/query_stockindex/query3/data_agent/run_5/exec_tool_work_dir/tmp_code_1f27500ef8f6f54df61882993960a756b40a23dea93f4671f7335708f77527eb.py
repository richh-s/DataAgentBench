code = """import pandas as pd
import json

# Load the large query result from storage file
path = var_call_JZzNG6zsZaINEC7vXnUlHYkz
df = pd.read_json(path)

# Convert types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter from 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

results = []

# mapping index -> country
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'J203.JO': 'South Africa',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'NYA': 'United States',
    'IXIC': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands'
}

for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').set_index('Date')
    monthly = g['CloseUSD'].resample('M').last().dropna()
    months = len(monthly)
    if months == 0:
        continue
    # invest $1 each month at that month's close
    units = (1.0 / monthly).sum()
    # final price = last available close
    final_price = g['CloseUSD'].iloc[-1]
    final_value = units * final_price
    total_invested = months * 1.0
    ratio = final_value / total_invested if total_invested>0 else None
    pct = (final_value - total_invested) / total_invested * 100 if total_invested>0 else None
    results.append({
        'Index': idx,
        'country': country_map.get(idx, 'Unknown'),
        'months_invested': months,
        'final_value_per_1usd_monthly': round(final_value, 6),
        'return_ratio': round(ratio, 6),
        'return_percent': round(pct, 2)
    })

# sort by return_ratio desc
results_sorted = sorted(results, key=lambda x: x['return_ratio'], reverse=True)
top5 = results_sorted[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_Jy6Z3z6BAZuRUu4TV1YLww3x': ['index_trade'], 'var_call_ymrJuqVE3u8wvRK1OdiWTDsS': ['index_info'], 'var_call_vLQi3Gd7FUu3buWgW4I0e4xr': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_2AjqcSVd7CZlKZpguak2NnvD': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_JZzNG6zsZaINEC7vXnUlHYkz': 'file_storage/call_JZzNG6zsZaINEC7vXnUlHYkz.json'}

exec(code, env_args)

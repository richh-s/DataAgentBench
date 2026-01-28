code = """import json
import pandas as pd

# Load the large query result from the provided file path
path = var_call_JSSLwie3oGoMSK6lDx45Plv3
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Some CloseUSD values may be strings; convert safely
for rec in data:
    # Normalize CloseUSD
    try:
        rec['CloseUSD'] = float(rec['CloseUSD'])
    except:
        rec['CloseUSD'] = None

# Build DataFrame
df = pd.DataFrame(data)
# Parse dates flexibly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# Filter out records with null dates or CloseUSD
df = df[df['Date'].notna() & df['CloseUSD'].notna()].copy()

# We'll simulate monthly investments: assume $1 invested on the first trading day of each month from 2000-01 to last available
# For each index, compute the number of shares bought each month = 1 / CloseUSD_on_purchase_day

def compute_return(group):
    g = group.sort_values('Date').copy()
    # Resample to month start: find first trading day of each month
    g.set_index('Date', inplace=True)
    monthly = g.groupby([g.index.year, g.index.month]).first()
    monthly.index = pd.to_datetime([f"{y}-{m:02d}-01" for y,m in monthly.index])
    monthly = monthly[monthly.index >= pd.to_datetime('2000-01-01')]
    if monthly.empty:
        return None
    # Shares bought each month with $1
    monthly['shares'] = 1.0 / monthly['CloseUSD']
    total_shares = monthly['shares'].sum()
    # Value at last available close
    last_price = g['CloseUSD'].iloc[-1]
    final_value = total_shares * last_price
    return {
        'Index': g['Index'].iloc[0],
        'TotalInvested': len(monthly) * 1.0,
        'FinalValue': final_value,
        'TotalShares': total_shares,
        'LastDate': g.index.max().strftime('%Y-%m-%d')
    }

results = []
for idx, group in df.groupby('Index'):
    res = compute_return(group)
    if res:
        results.append(res)

res_df = pd.DataFrame(results)
res_df['TotalReturn'] = res_df['FinalValue'] / res_df['TotalInvested']
res_df = res_df.sort_values('TotalReturn', ascending=False)

# Keep top 20 for inspection
top = res_df.head(20).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top))"""

env_args = {'var_call_EYqJ33W0hk39LDJPkTU7BRUr': ['index_trade'], 'var_call_rQjwq5dSQGDDW3Xq6WTecju9': ['index_info'], 'var_call_JSSLwie3oGoMSK6lDx45Plv3': 'file_storage/call_JSSLwie3oGoMSK6lDx45Plv3.json', 'var_call_sZUEwjcCZc1eKyRtzsiSWdrp': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

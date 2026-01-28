code = """import json
import pandas as pd
from datetime import datetime

# Load the large query result from the provided file path variable
data_path = var_call_lDu27glJm9Eft2kn37Hk2wmZ
with open(data_path, 'r') as f:
    records = json.load(f)

# Convert to DataFrame
# Some Date strings may have timezone or different formats; parse carefully
for r in records:
    # normalize CloseUSD
    try:
        r['CloseUSD'] = float(r['CloseUSD'])
    except:
        r['CloseUSD'] = None
    # ensure Date is a clean ISO date
    # remove any timezone-like suffix
    if isinstance(r.get('Date'), str):
        r['Date'] = r['Date'].split('+')[0].strip()







df = pd.DataFrame(records)
# Parse date robustly
try:
    df['Date'] = pd.to_datetime(df['Date'], utc=False, errors='coerce')
except Exception as e:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates or CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter from 2000-01-01 onwards
df = df[df['Date'] >= pd.to_datetime('2000-01-01')]

# Simulation parameters
invest_amount = 1.0  # $1 per month (relative returns independent of amount)

# Helper to infer country from index symbol
def infer_country(symbol):
    s = str(symbol).upper()
    # Common patterns
    if s.endswith('.SS') or s.startswith('000') or s.startswith('600'):
        return 'China'
    if s.endswith('.SZ') or s.startswith('399'):
        return 'China'
    if s in ('HSI', '^HSI') or 'HSI' in s or 'HANG' in s:
        return 'Hong Kong'
    if 'N225' in s or s in ('NIKKEI','^N225'):
        return 'Japan'
    if s in ('GSPC','^GSPC','SPX','^SPX','^GSPC') or s in ('DJI','^DJI','IXIC','^IXIC','NASDAQ') or s.endswith('.US'):
        return 'United States'
    if 'FTSE' in s or 'LON' in s or 'UK' in s:
        return 'United Kingdom'
    if 'DAX' in s or 'GDAXI' in s:
        return 'Germany'
    if 'KOSPI' in s or 'KS11' in s or s.startswith('KR'):
        return 'South Korea'
    if s.endswith('.TO') or 'TSX' in s or s.startswith('TSX'):
        return 'Canada'
    if s in ('SENSEX','BSE','NSE') or 'NSE' in s or 'BSE' in s or 'NIFTY' in s:
        return 'India'
    if s in ('TWII','^TWII') or s.startswith('TSEC') or s.endswith('.TW'):
        return 'Taiwan'
    if s in ('JSE','^JALSH') or s.endswith('.JO'):
        return 'South Africa'
    if s in ('SSE','SHCOMP'):
        return 'China'
    # Fallbacks by suffixes
    if '.' in s:
        suf = s.split('.')[-1]
        if suf == 'SS' or suf == 'SZ':
            return 'China'
        if suf == 'HK':
            return 'Hong Kong'
        if suf == 'TO':
            return 'Canada'
        if suf == 'JP' or suf == 'T' or suf == 'TYO':
            return 'Japan'
    return 'Unknown'

results = []

for idx, g in df.groupby('Index'):
    g = g.sort_values('Date').copy()
    if g.empty:
        continue
    # first row per month (first trading day in the month)
    g['Month'] = g['Date'].dt.to_period('M')
    monthly = g.groupby('Month', sort=True).first().reset_index()
    # Ensure months start at or after 2000-01
    monthly = monthly[monthly['Month'] >= pd.Period('2000-01', freq='M')]
    n_months = len(monthly)
    if n_months < 12:
        # skip indices with too few data
        continue
    # Shares accumulated
    monthly['Shares'] = invest_amount / monthly['CloseUSD']
    total_shares = monthly['Shares'].sum()
    # Use last available close price for final value
    last_close = g['CloseUSD'].iloc[-1]
    final_value = total_shares * last_close
    total_invested = invest_amount * n_months
    multiple = final_value / total_invested if total_invested > 0 else None
    results.append({
        'Index': idx,
        'Months': int(n_months),
        'TotalInvested': round(total_invested, 2),
        'FinalValue': round(final_value, 2),
        'Multiple': round(multiple, 4) if multiple is not None else None,
        'Country': infer_country(idx)
    })

# Sort by Multiple descending and pick top 5
results_sorted = sorted(results, key=lambda x: (x['Multiple'] if x['Multiple'] is not None else -999), reverse=True)
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_lDu27glJm9Eft2kn37Hk2wmZ': 'file_storage/call_lDu27glJm9Eft2kn37Hk2wmZ.json', 'var_call_SCen6EOc2DnUN5rlxZswPfuT': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

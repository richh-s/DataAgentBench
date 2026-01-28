code = """import json
import pandas as pd

# Load data
with open(var_call_Mi0qdYN0BpVQl7cja7UNtaAe, 'r') as f:
    data = json.load(f)

index_info = var_call_qp0DEN9fhAjckt8EjOeFYXdP

df = pd.DataFrame(data)
# Parse
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# Drop bad rows
df = df[df['CloseUSD'].notna() & df['Date'].notna()].copy()
# Filter since 2000-01-01
df = df[df['Date'] >= pd.to_datetime('2000-01-01')]
# YearMonth
df['YearMonth'] = df['Date'].dt.to_period('M')

results = []
monthly_contribution = 1.0

for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    # get first trading day each month robustly
    try:
        idxmin = g.groupby('YearMonth')['Date'].idxmin()
        monthly = g.loc[idxmin].sort_values('Date')
    except Exception:
        # fallback
        monthly = g.groupby('YearMonth').apply(lambda x: x.nsmallest(1, 'Date')).reset_index(drop=True)
    months = len(monthly)
    if months == 0:
        continue
    shares = (monthly_contribution / monthly['CloseUSD']).sum()
    last_price = g.iloc[-1]['CloseUSD']
    final_value = shares * last_price
    total_invested = months * monthly_contribution
    if total_invested <= 0:
        continue
    return_factor = final_value / total_invested
    results.append({
        'Index': idx,
        'months': int(months),
        'total_invested': float(round(total_invested,6)),
        'final_value': float(round(final_value,6)),
        'return_factor': float(round(return_factor,6)),
        'last_date': g.iloc[-1]['Date'].strftime('%Y-%m-%d')
    })

res_df = pd.DataFrame(results)
res_df = res_df[res_df['return_factor'].notna() & res_df['return_factor'] != float('inf')]

top5 = res_df.sort_values('return_factor', ascending=False).head(5)

# Infer country mapping heuristically
def infer_country(sym):
    s = sym.upper()
    if '.SS' in s or s.startswith('000') or s.startswith('SSEC') or s.startswith('SH') or s.startswith('SSE'):
        return 'China'
    if '.SZ' in s or s.startswith('399'):
        return 'China'
    if s in ('HSI', 'HANGSENG') or 'HANG SENG' in s or 'HKG' in s:
        return 'Hong Kong'
    if s in ('N225','NIKKEI','NI225') or 'NIKKEI' in s:
        return 'Japan'
    if s in ('GSPC','^GSPC','SPX') or 'S&P' in s or s.startswith('SP'):
        return 'United States'
    if s in ('DJI','^DJI') or 'DOW' in s:
        return 'United States'
    if 'NASDAQ' in s or 'IXIC' in s or s.startswith('NDX') or s.startswith('NQ'):
        return 'United States'
    if 'FTSE' in s or 'UK' in s or 'LON' in s:
        return 'United Kingdom'
    if 'DAX' in s or 'GDAXI' in s:
        return 'Germany'
    if 'CAC' in s:
        return 'France'
    if 'TSX' in s or 'TSE' in s:
        return 'Canada'
    if 'KOSPI' in s or 'KS' in s or 'KQ' in s:
        return 'South Korea'
    if 'SIX' in s or 'SWISS' in s:
        return 'Switzerland'
    if 'BSE' in s or 'NSE' in s:
        return 'India'
    # fallback: try to match exchange names from index_info
    for rec in index_info:
        ex = rec.get('Exchange','').upper()
        if any(tok in s for tok in ex.split()[:2]):
            # crude
            if 'JAPAN' in ex or 'TOKYO' in ex:
                return 'Japan'
            if 'HONG KONG' in ex:
                return 'Hong Kong'
            if 'SHANGHAI' in ex:
                return 'China'
            if 'NEW YORK' in ex or 'NASDAQ' in ex:
                return 'United States'
            if 'TORONTO' in ex:
                return 'Canada'
            if 'FRANKFURT' in ex or 'EURONEXT' in ex:
                return 'Europe'
    return 'Unknown'

out = []
for r in top5.to_dict(orient='records'):
    country = infer_country(r['Index'])
    out.append({
        'Index': r['Index'],
        'Country': country,
        'return_factor': r['return_factor'],
        'final_value': r['final_value'],
        'total_invested': r['total_invested'],
        'months': r['months'],
        'last_date': r['last_date']
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_g0h6mRxm2lCzdwaun3y0hEPB': ['index_trade'], 'var_call_Mi0qdYN0BpVQl7cja7UNtaAe': 'file_storage/call_Mi0qdYN0BpVQl7cja7UNtaAe.json', 'var_call_o2aQmVbVBNOdULA6hy7eruXJ': ['index_info'], 'var_call_qp0DEN9fhAjckt8EjOeFYXdP': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

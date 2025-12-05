code = """import json, pandas as pd, datetime
from datetime import datetime

# Load full results
with open(var_call_8c5pyw4bp9BpyTfP0TiF0DpB, 'r') as f:
    cpc_level5 = json.load(f)
with open(var_call_ofPmsL1WjRvuIXoHRLH0Htmw, 'r') as f:
    pubs = json.load(f)

# Prepare set of level 5 symbols (group codes)
level5_symbols = set([r['symbol'] for r in cpc_level5])

# Helper to extract year from natural language date
def extract_year(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, '%b %dth, %Y').year
    except Exception:
        try:
            return datetime.strptime(date_str, '%b %dst, %Y').year
        except Exception:
            try:
                return datetime.strptime(date_str, '%b %dnd, %Y').year
            except Exception:
                try:
                    return datetime.strptime(date_str, '%b %drd, %Y').year
                except Exception:
                    return None

# Count filings per year per CPC symbol (only level 5)
counts = {}
for r in pubs:
    year = extract_year(r['publication_date'])
    if year is None:
        continue
    try:
        cpc_list = json.loads(r['cpc'])
    except Exception:
        continue
    # Use each code at most once per patent per year
    seen = set()
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        # CPC symbol is up to the first space (usually none); keep full code string
        symbol = code.split(' ')[0]
        if symbol not in level5_symbols:
            continue
        key = (symbol, year)
        if key in seen:
            continue
        seen.add(key)
        counts[key] = counts.get(key, 0) + 1

# Build DataFrame from counts
rows = [{'symbol': s, 'year': y, 'count': c} for (s, y), c in counts.items()]
df = pd.DataFrame(rows)
if df.empty:
    result = []
else:
    # Compute EMA per symbol sorted by year
    alphas = 0.2
    df = df.sort_values(['symbol', 'year'])
    ema_vals = []
    for symbol, grp in df.groupby('symbol'):
        ema = None
        for _, row in grp.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alphas * c + (1 - alphas) * ema
            ema_vals.append({'symbol': symbol, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_vals)

    # For each symbol, find year of max EMA and its value
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best_df = ema_df.loc[idx].copy()

    # Filter to best year == 2022
    best_2022 = best_df[best_df['year'] == 2022]

    # We only need the CPC group codes at level 5
    result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8c5pyw4bp9BpyTfP0TiF0DpB': 'file_storage/call_8c5pyw4bp9BpyTfP0TiF0DpB.json', 'var_call_ofPmsL1WjRvuIXoHRLH0Htmw': 'file_storage/call_ofPmsL1WjRvuIXoHRLH0Htmw.json', 'var_call_KNRdNyNqwiAs0UhkIrzRLqBE': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}]}

exec(code, env_args)

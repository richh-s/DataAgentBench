code = """import json, pandas as pd

# Load a subset of publication data incrementally to reduce memory/time
with open(var_call_n6QpmquHkibhcJA3ZY7kSMRL, 'r') as f:
    pub_data = json.load(f)

# We'll process in chunks over the already-loaded list
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(s):
    if not isinstance(s, str) or not s.strip():
        return None
    parts = s.replace(',', '').split()
    if len(parts) < 3:
        return None
    year = parts[-1]
    try:
        return int(year)
    except:
        return None

from collections import defaultdict
symbol_year_counts = defaultdict(int)

for rec in pub_data:
    y = parse_year(rec.get('publication_date'))
    if y is None:
        continue
    cpc_raw = rec.get('cpc')
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            code = None
        if not code:
            continue
        symbol_year_counts[(code, y)] += 1

# Build DataFrame from aggregated counts
rows = [{'symbol': s, 'year': y, 'count': c} for (s, y), c in symbol_year_counts.items()]
counts = pd.DataFrame(rows)

if counts.empty:
    result = json.dumps([])
else:
    years_sorted = sorted(counts['year'].unique())
    alpha = 0.2
    ema_records = []
    for symbol, grp in counts.groupby('symbol'):
        grp = grp.set_index('year').reindex(years_sorted, fill_value=0).sort_index()
        ema = None
        for yr, cnt in grp['count'].items():
            if ema is None:
                ema = cnt
            else:
                ema = alpha*cnt + (1-alpha)*ema
            ema_records.append({'symbol': symbol, 'year': int(yr), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best_df = ema_df.loc[idx].reset_index(drop=True)
    best_2022 = best_df[best_df['year'] == 2022]
    symbols_2022 = sorted(best_2022['symbol'].unique())
    result = json.dumps(symbols_2022)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_n6QpmquHkibhcJA3ZY7kSMRL': 'file_storage/call_n6QpmquHkibhcJA3ZY7kSMRL.json', 'var_call_UG8NvhbjbktTG8UhVablTj1j': 'file_storage/call_UG8NvhbjbktTG8UhVablTj1j.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_JGmzwztZuUuxYSPU2LPjKBn7)
level5 = load_records(var_call_IF8LyVGeDn0NKvSJyXQJiS0k)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol') is not None)

def year_from_text(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

rows = []
for r in pub:
    y = year_from_text(r.get('filing_date'))
    if y is None:
        continue
    cpc_str = r.get('cpc')
    if not cpc_str:
        continue
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        continue
    for entry in cpcs if isinstance(cpcs, list) else []:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        grp = code.split('/')[0].strip()
        if grp in level5_set:
            rows.append((grp, y))

df = pd.DataFrame(rows, columns=['group','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['group','year']).size().reset_index(name='filings')
    years = sorted(counts['year'].unique().tolist())
    alpha = 0.2
    # compute EMA per group over full year index
    best = []
    for grp, gdf in counts.groupby('group'):
        s = gdf.set_index('year')['filings']
        ema = None
        best_year = None
        best_val = None
        for y in years:
            v = float(s.get(y, 0.0))
            ema = v if ema is None else (alpha*v + (1-alpha)*ema)
            if (best_val is None) or (ema > best_val):
                best_val = ema
                best_year = y
        best.append({'group': grp, 'best_year': int(best_year), 'best_ema': float(best_val)})
    best_df = pd.DataFrame(best)
    out = best_df[best_df['best_year']==2022].sort_values(['best_ema','group'], ascending=[False,True])['group'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JGmzwztZuUuxYSPU2LPjKBn7': 'file_storage/call_JGmzwztZuUuxYSPU2LPjKBn7.json', 'var_call_IF8LyVGeDn0NKvSJyXQJiS0k': 'file_storage/call_IF8LyVGeDn0NKvSJyXQJiS0k.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

# Load data from storage paths
with open(var_call_DHxRw7whb1bB1OxlQkXmpnLJ, 'r') as f:
    pubs = json.load(f)
with open(var_call_HGBQbuxNdnnzD4ENXdiFYLWw, 'r') as f:
    level5_rows = json.load(f)

level5_set = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_set.add(sym.strip().upper())

rows = []
for rec in pubs:
    filing = rec.get('filing_date')
    if not filing or not isinstance(filing, str):
        continue
    m = re.search(r'(\d{4})', filing)
    if not m:
        continue
    year = int(m.group(1))
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field is a JSON-like string; attempt to parse
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to clean some common issues
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code or not isinstance(code, str):
            continue
        code = code.strip().upper()
        group = code[:4]
        if group in level5_set:
            rows.append({'group': group, 'year': year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Determine year range to cover
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    years = list(range(min_year, max_year+1))

    groups = sorted(df['group'].unique())
    winners = []
    for g in groups:
        sub = df[df['group']==g]
        counts = sub.groupby('year').size().reindex(years, fill_value=0).sort_index()
        # compute EMA with alpha=0.2, use recursive form (adjust=False)
        ema = counts.ewm(alpha=0.2, adjust=False).mean()
        # find max EMA value and corresponding years
        max_ema = float(ema.max())
        # find years where ema is close to max_ema
        import numpy as np
        years_with_max = [int(y) for y,v in zip(counts.index, ema) if np.isclose(v, max_ema)]
        if 2022 in years_with_max:
            winners.append(g)
    result = sorted(winners)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DHxRw7whb1bB1OxlQkXmpnLJ': 'file_storage/call_DHxRw7whb1bB1OxlQkXmpnLJ.json', 'var_call_HGBQbuxNdnnzD4ENXdiFYLWw': 'file_storage/call_HGBQbuxNdnnzD4ENXdiFYLWw.json'}

exec(code, env_args)

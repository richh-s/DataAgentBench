code = """import json
import pandas as pd
import re

# Load query results from storage variables
path_pub = var_call_KyrYAJ4jdxTOF4TwLx8fElmE
path_lvl5 = var_call_Q5HYfXEC3rQk7deU3l2XQjaa

with open(path_pub, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

with open(path_lvl5, 'r', encoding='utf-8') as f:
    lvl5_rows = json.load(f)

# Build set of level 5 symbols
lvl5_symbols = set()
for r in lvl5_rows:
    sym = r.get('symbol')
    if sym:
        lvl5_symbols.add(sym.strip())

# Parse publications
records = []
year_re = re.compile(r"(19|20)\d{2}")
for r in pubs:
    cpc_field = r.get('cpc')
    filing = r.get('filing_date')
    if not cpc_field or not filing:
        continue
    # extract year
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    # parse cpc field which is a JSON-like string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpcs = json.loads(cpc_field.replace("\'", '"'))
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
        code = code.strip()
        # Extract group code at level 5: first 4 characters (letters+digits+letter)
        # Some codes may start with 'Y' etc; take first 4 chars before any space
        group = code[:4]
        records.append({'group': group, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # get full range of years
    years = sorted(df['year'].unique())
    # compute counts per group-year
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # pivot for easy access
    # build mapping
    counts_map = {(row['group'], row['year']): int(row['count']) for _, row in counts.iterrows()}

    alpha = 0.2
    groups = sorted(df['group'].unique())

    ema_results = {}  # group -> dict year->ema
    for g in groups:
        ema = None
        ema_results[g] = {}
        for y in years:
            cnt = counts_map.get((g,y), 0)
            if ema is None:
                ema = float(cnt)
            else:
                ema = alpha * cnt + (1 - alpha) * ema
            ema_results[g][y] = ema

    # determine best year per group (year with max ema)
    best_year = {}
    for g, emad in ema_results.items():
        # find year(s) with maximum ema
        max_ema = max(emad.values())
        # if multiple years tie, pick the earliest year of the ties? but we'll record all
        best_years = [y for y, v in emad.items() if abs(v - max_ema) < 1e-9]
        # choose the earliest year among best_years
        best_year[g] = min(best_years)

    # filter groups to those in level 5 symbols and whose best year is 2022
    result = [g for g, y in best_year.items() if (g in lvl5_symbols and y == 2022)]
    result = sorted(result)

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_KyrYAJ4jdxTOF4TwLx8fElmE': 'file_storage/call_KyrYAJ4jdxTOF4TwLx8fElmE.json', 'var_call_Q5HYfXEC3rQk7deU3l2XQjaa': 'file_storage/call_Q5HYfXEC3rQk7deU3l2XQjaa.json'}

exec(code, env_args)

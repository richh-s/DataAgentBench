code = """import json
import pandas as pd
import re

# Load data from storage keys
with open(var_call_nEGSG9Pgo96UjDmK1PhTS3JD, 'r') as f:
    pubs = json.load(f)
with open(var_call_ZnbiLfZJs012xnHBiMGEAlSS, 'r') as f:
    cpc_defs = json.load(f)

# Build set of level-5 symbols
level5_symbols = set()
for entry in cpc_defs:
    sym = entry.get('symbol')
    if sym:
        level5_symbols.add(sym.strip().upper())

# Helper to extract year
year_re = re.compile(r"(20\d{2}|19\d{2})")

# Count occurrences per group-year
counts = {}
for rec in pubs:
    pub_date = rec.get('publication_date') or ''
    m = year_re.search(pub_date)
    if not m:
        continue
    year = int(m.group(1))
    cpc_field = rec.get('cpc') or '[]'
    # parse cpc JSON-like string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to recover by replacing newlines etc
        try:
            cpcs = json.loads(cpc_field.strip())
        except Exception:
            continue
    groups = set()
    for c in cpcs:
        code = c.get('code') if isinstance(c, dict) else None
        if not code:
            continue
        code = code.strip().upper()
        # extract first 4 chars as group (letters+digits)
        grp = code[:4]
        # Some codes might start with spaces; ensure proper
        grp = grp.replace(' ', '')
        if grp in level5_symbols:
            groups.add(grp)
    for g in groups:
        counts.setdefault(g, {}).setdefault(year, 0)
        counts[g][year] += 1

# Build DataFrame of counts with years sorted
all_years = sorted({y for g in counts for y in counts[g]})
if not all_years:
    result = []
else:
    df = pd.DataFrame(index=sorted(counts.keys()), columns=all_years).fillna(0)
    for g, ys in counts.items():
        for y, v in ys.items():
            df.at[g, y] = v

    # Compute EMA per group across years with alpha=0.2
    ema_alpha = 0.2
    best_years = {}
    for g in df.index:
        series = pd.Series(df.loc[g].values, index=all_years)
        ema = series.ewm(alpha=ema_alpha, adjust=False).mean()
        # find year with max EMA; if multiple, pick latest year
        max_val = ema.max()
        # get years with this max (could be multiple)
        years_with_max = [int(y) for y, val in ema.items() if val == max_val]
        # choose the latest year among them as best year
        best_year = max(years_with_max) if years_with_max else None
        best_years[g] = {'best_year': best_year, 'max_ema': float(max_val), 'ema_series': {str(int(y)): float(v) for y, v in ema.items()}}

    # Select groups whose best year is 2022
    result = sorted([g for g, info in best_years.items() if info['best_year'] == 2022])

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_nEGSG9Pgo96UjDmK1PhTS3JD': 'file_storage/call_nEGSG9Pgo96UjDmK1PhTS3JD.json', 'var_call_ZnbiLfZJs012xnHBiMGEAlSS': 'file_storage/call_ZnbiLfZJs012xnHBiMGEAlSS.json'}

exec(code, env_args)

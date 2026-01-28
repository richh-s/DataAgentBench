code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load tool results from storage paths
pubs_path = var_call_Qy8TLTMJbymlJg5NMi8vsBsp
lvl5_path = var_call_endGIMHBmlkYqjJhD6Jmx1EL

with open(pubs_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

with open(lvl5_path, 'r', encoding='utf-8') as f:
    lvl5 = json.load(f)

level5_set = set()
for r in lvl5:
    sym = r.get('symbol')
    if sym:
        level5_set.add(sym.strip().upper())

# Build counts per group per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = re.search(r'(\d{4})', s)
    if m:
        return int(m.group(1))
    return None

for pub in pubs:
    year = extract_year(pub.get('filing_date'))
    if not year:
        continue
    all_years.add(year)
    cpc_field = pub.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpcs = json.loads(cpc_field.replace("\n", ""))
        except Exception:
            continue
    # collect unique level5 groups in this publication
    groups_in_pub = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        code = code.strip().upper()
        # normalize by removing spaces
        code = code.replace(' ', '')
        if len(code) < 4:
            continue
        group = code[:4]
        # ensure group is alnum
        group = re.sub(r'[^A-Z0-9]', '', group)
        if group in level5_set:
            groups_in_pub.add(group)
    for g in groups_in_pub:
        counts[g][year] += 1

if not all_years:
    result = []
else:
    min_year = min(all_years)
    max_year = max(all_years)
    years = list(range(min_year, max_year+1))

    alpha = 0.2
    result = []
    for g, year_counts in counts.items():
        # build ordered counts
        series = [year_counts.get(y, 0) for y in years]
        # compute EMA
        ema = []
        if not series:
            continue
        ema_val = series[0]
        ema.append(ema_val)
        for v in series[1:]:
            ema_val = alpha * v + (1 - alpha) * ema_val
            ema.append(ema_val)
        # find year of max EMA (if multiple, take latest year?) The prompt: "best year is 2022" likely the year with highest EMA.
        max_idx = max(range(len(ema)), key=lambda i: (ema[i], years[i]))
        best_year = years[max_idx]
        if best_year == 2022:
            result.append(g)

# Sort result for deterministic output
result_sorted = sorted(result)

import json
print("__RESULT__:")
print(json.dumps(result_sorted))"""

env_args = {'var_call_Qy8TLTMJbymlJg5NMi8vsBsp': 'file_storage/call_Qy8TLTMJbymlJg5NMi8vsBsp.json', 'var_call_endGIMHBmlkYqjJhD6Jmx1EL': 'file_storage/call_endGIMHBmlkYqjJhD6Jmx1EL.json'}

exec(code, env_args)

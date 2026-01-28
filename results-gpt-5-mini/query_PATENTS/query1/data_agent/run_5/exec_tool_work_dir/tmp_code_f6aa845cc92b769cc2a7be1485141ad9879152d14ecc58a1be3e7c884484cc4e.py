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

pattern = re.compile("\\d{4}")

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = pattern.search(s)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

for pub in pubs:
    year = extract_year(pub.get('filing_date'))
    if not year:
        continue
    all_years.add(year)
    cpc_field = pub.get('cpc')
    if not cpc_field:
        continue
    # cpc_field may be a string representing a JSON list, or already a list
    cpcs = None
    if isinstance(cpc_field, list):
        cpcs = cpc_field
    elif isinstance(cpc_field, str):
        try:
            cpcs = json.loads(cpc_field)
        except Exception:
            # try to clean newlines
            try:
                cpcs = json.loads(cpc_field.replace('\n', '').replace('\r', ''))
            except Exception:
                cpcs = None
    if not cpcs or not isinstance(cpcs, list):
        continue
    groups_in_pub = set()
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            code = entry
        if not code or not isinstance(code, str):
            continue
        code = code.strip().upper().replace(' ', '')
        if len(code) < 4:
            continue
        group = code[:4]
        group = re.sub('[^A-Z0-9]', '', group)
        if group in level5_set:
            groups_in_pub.add(group)
    for g in groups_in_pub:
        counts[g][year] += 1

result = []
if all_years:
    min_year = min(all_years)
    max_year = max(all_years)
    years = list(range(min_year, max_year+1))
    alpha = 0.2
    for g, year_counts in counts.items():
        series = [year_counts.get(y, 0) for y in years]
        if not series:
            continue
        ema_vals = []
        ema = series[0]
        ema_vals.append(ema)
        for v in series[1:]:
            ema = alpha * v + (1 - alpha) * ema
            ema_vals.append(ema)
        # find index of max EMA; if ties, choose latest year by sorting key
        max_idx = max(range(len(ema_vals)), key=lambda i: (ema_vals[i], years[i]))
        best_year = years[max_idx]
        if best_year == 2022:
            result.append(g)

result_sorted = sorted(result)
print("__RESULT__:")
print(json.dumps(result_sorted))"""

env_args = {'var_call_Qy8TLTMJbymlJg5NMi8vsBsp': 'file_storage/call_Qy8TLTMJbymlJg5NMi8vsBsp.json', 'var_call_endGIMHBmlkYqjJhD6Jmx1EL': 'file_storage/call_endGIMHBmlkYqjJhD6Jmx1EL.json'}

exec(code, env_args)

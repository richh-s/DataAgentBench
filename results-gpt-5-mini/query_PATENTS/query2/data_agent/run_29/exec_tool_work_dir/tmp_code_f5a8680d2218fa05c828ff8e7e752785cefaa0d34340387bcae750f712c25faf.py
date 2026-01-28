code = """import json
import re
from collections import defaultdict, OrderedDict

alpha = 0.1

# Load data files (paths provided in variables)
with open(var_call_2P9xvNZgsyIyHLkbna4RTdG4, 'r', encoding='utf-8') as f:
    half = json.load(f)
with open(var_call_SbUl2kznaG8flUhiEHOnSxoj, 'r', encoding='utf-8') as f:
    de_all = json.load(f)
with open(var_call_2E4EZO9rqDzqqzEaExnovhTH, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build map from (Patents_info, grant_date) to filing_date for DE records
filing_map = {}
pi_map = {}
for r in de_all:
    pi = r.get('Patents_info')
    gd = r.get('grant_date')
    fd = r.get('filing_date')
    if pi is not None and gd is not None:
        filing_map[(pi, gd)] = fd
    if pi is not None and fd is not None:
        # store by Patents_info as fallback
        if pi not in pi_map:
            pi_map[pi] = fd

# Build mapping of level-4 CPC symbols to titleFull
title_map = {str(r.get('symbol')): r.get('titleFull') for r in cpc_defs}

# Helper to parse cpc field
def parse_cpc_field(cpc_field):
    codes = []
    if not cpc_field:
        return codes
    # try JSON parse
    try:
        parsed = json.loads(cpc_field)
        if isinstance(parsed, list):
            for item in parsed:
                if isinstance(item, dict) and 'code' in item:
                    codes.append(item['code'])
    except Exception:
        # fallback regex
        codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
    return [c.strip() for c in codes if c and isinstance(c, str)]

# Filter half-year grants to Germany
selected = []
for r in half:
    pi = r.get('Patents_info','')
    if not pi:
        continue
    # crude DE detection: look for ' DE-' or 'from DE' or ', DE' or ' DE,'
    if (' DE-' in pi) or ('from DE' in pi) or (', DE' in pi) or (' DE,' in pi) or ('from DE,' in pi):
        # find filing_date from map
        gd = r.get('grant_date')
        fd = filing_map.get((pi, gd))
        if not fd:
            fd = pi_map.get(pi)
        if not fd:
            # try to find any de_all record that matches on substring of pi
            for k,v in pi_map.items():
                if k in pi or pi in k:
                    fd = v
                    break
        if not fd:
            # skip if no filing date found
            continue
        r_copy = dict(r)
        r_copy['filing_date'] = fd
        selected.append(r_copy)

# Count filings per CPC group (level-4 assumed as first 3 chars) by filing year
counts = defaultdict(lambda: defaultdict(int))
for r in selected:
    fd = r.get('filing_date','')
    m = re.search(r'(19|20)\d{2}', str(fd))
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = r.get('cpc')
    codes = parse_cpc_field(cpc_field)
    # deduplicate codes per record
    codes = list(set(codes))
    for code in codes:
        code_up = code.upper()
        # extract first 3 characters as level-4 group (e.g., G06, A61)
        grp = code_up[:3]
        if len(grp) < 3:
            continue
        counts[grp][year] += 1

# For each group compute EMA over years and find best year
results = []
for grp, year_counts in counts.items():
    # sort years
    years_sorted = sorted(year_counts.keys())
    if not years_sorted:
        continue
    ema_by_year = OrderedDict()
    ema = None
    for y in years_sorted:
        cnt = year_counts.get(y, 0)
        if ema is None:
            ema = float(cnt)
        else:
            ema = alpha * float(cnt) + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    best_ema = ema_by_year[best_year]
    title = title_map.get(grp) or title_map.get(grp.strip()) or None
    results.append({
        'cpc_group': grp,
        'titleFull': title,
        'best_year': best_year,
        'best_ema': round(best_ema, 3)
    })

# Sort results by best_ema descending
results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)

# Output JSON string
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_0zQO3Sb3ALi5ihawUy1yL68N': 'file_storage/call_0zQO3Sb3ALi5ihawUy1yL68N.json', 'var_call_SbUl2kznaG8flUhiEHOnSxoj': 'file_storage/call_SbUl2kznaG8flUhiEHOnSxoj.json', 'var_call_2E4EZO9rqDzqqzEaExnovhTH': 'file_storage/call_2E4EZO9rqDzqqzEaExnovhTH.json', 'var_call_2P9xvNZgsyIyHLkbna4RTdG4': 'file_storage/call_2P9xvNZgsyIyHLkbna4RTdG4.json'}

exec(code, env_args)

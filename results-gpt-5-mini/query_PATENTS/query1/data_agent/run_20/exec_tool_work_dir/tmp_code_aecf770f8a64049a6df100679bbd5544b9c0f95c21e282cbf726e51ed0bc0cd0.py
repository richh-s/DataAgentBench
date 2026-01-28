code = """import json
import re
from collections import defaultdict, OrderedDict

# Load data from previous query results stored in files
with open(var_call_fMlECO7TIQUsXsbKDAsNfIoa, 'r') as f:
    pubs = json.load(f)
with open(var_call_m4GCke2KQvO6V0csBgBCc96I, 'r') as f:
    defs = json.load(f)

# Extract level-5 symbols
level5_symbols = [rec['symbol'] for rec in defs if rec.get('symbol')]
# Sort by length descending to match longest prefix first
level5_symbols_sorted = sorted(level5_symbols, key=lambda x: -len(x))

alpha = 0.2

# Helper to extract year
year_re = re.compile(r"(19|20)\d{2}")

group_year_counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    fd = rec.get('filing_date')
    if not fd or not isinstance(fd, str):
        continue
    m = year_re.search(fd)
    if not m:
        continue
    year = int(m.group(0))

    cpc_field = rec.get('cpc')
    if not cpc_field or not isinstance(cpc_field, str):
        continue
    # try to parse cpc_field as JSON
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # skip malformed
        continue
    matched_groups = set()
    for entry in cpc_list:
        # entry may be dict with 'code' key
        code = None
        if isinstance(entry, dict):
            code = entry.get('code')
        elif isinstance(entry, str):
            code = entry
        if not code or not isinstance(code, str):
            continue
        code = code.strip()
        # Find matching level-5 symbol
        matched = None
        for sym in level5_symbols_sorted:
            if code.startswith(sym):
                matched = sym
                break
        if not matched:
            # as fallback try first 4 chars (letters+digits)
            norm = ''.join(ch for ch in code if ch.isalnum())
            if len(norm) >= 4:
                cand = norm[:4]
                if cand in level5_symbols:
                    matched = cand
            if not matched and len(norm) >= 3:
                cand = norm[:3]
                if cand in level5_symbols:
                    matched = cand
        if matched:
            matched_groups.add(matched)
    # For each matched group, count this patent once for that year
    for g in matched_groups:
        group_year_counts[g][year] += 1

# For each group, compute EMA over sorted years and find year with highest EMA
groups_with_best_2022 = []
for g, yc in group_year_counts.items():
    # sort years
    years = sorted(yc.keys())
    if not years:
        continue
    # Build a continuous year range from min to max to propagate zeros
    miny, maxy = years[0], years[-1]
    all_years = list(range(miny, maxy+1))
    ema_values = {}
    prev_ema = None
    for y in all_years:
        count = yc.get(y, 0)
        if prev_ema is None:
            ema = float(count)
        else:
            ema = alpha * count + (1 - alpha) * prev_ema
        ema_values[y] = ema
        prev_ema = ema
    # Find year with max EMA
    best_year = max(ema_values.items(), key=lambda x: (x[1], x[0]))[0]
    if best_year == 2022:
        groups_with_best_2022.append(g)

# Sort result
groups_with_best_2022_sorted = sorted(groups_with_best_2022)

import json as _json
print("__RESULT__:")
print(_json.dumps(groups_with_best_2022_sorted))"""

env_args = {'var_call_fMlECO7TIQUsXsbKDAsNfIoa': 'file_storage/call_fMlECO7TIQUsXsbKDAsNfIoa.json', 'var_call_m4GCke2KQvO6V0csBgBCc96I': 'file_storage/call_m4GCke2KQvO6V0csBgBCc96I.json'}

exec(code, env_args)

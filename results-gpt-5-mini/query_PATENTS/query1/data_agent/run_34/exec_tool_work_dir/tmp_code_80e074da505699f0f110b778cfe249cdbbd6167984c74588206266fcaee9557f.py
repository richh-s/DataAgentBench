code = """import json
import re
from collections import defaultdict, OrderedDict

# Load data from storage variables
# var_call_YLEJkDoRz4DSg6ej31fUWpLf and var_call_14kKNjAwdIg9QbXByF74R04z

with open(var_call_YLEJkDoRz4DSg6ej31fUWpLf, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)
with open(var_call_14kKNjAwdIg9QbXByF74R04z, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Build set of level-5 symbols
level5_symbols = set()
for r in cpc_defs:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Helper to extract year from filing_date string
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(s):
    if not s:
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# Helper to parse cpc field which is a JSON-like string

def extract_codes(cpc_field):
    if not cpc_field:
        return []
    # Sometimes it's already a Python list string; try json.loads
    try:
        codes = json.loads(cpc_field)
        # records are dicts with 'code'
        res = [rec.get('code') for rec in codes if isinstance(rec, dict) and rec.get('code')]
        return [c for c in res if c]
    except Exception:
        # fallback: find all occurrences of pattern like '"code": "..."' or just tokens like A01B...
        found = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
        if found:
            return found
        # generic find sequences like LetterDigitDigitLetter... until slash or whitespace
        found2 = re.findall(r'\b[A-Z]\d{2}[A-Z][^,\s\"]*', cpc_field)
        return found2

# Map to group symbol: take first 4 chars that match pattern Letter + 2 digits + Letter
pat_group = re.compile(r'^([A-Z]\d{2}[A-Z])')

def map_to_level5(code):
    if not code:
        return None
    m = pat_group.match(code)
    if m:
        sym = m.group(1)
        if sym in level5_symbols:
            return sym
        # sometimes symbol in defs might be like 'C01B' but case or spacing - ensure exact
        return sym
    # try stripping prefixes
    # remove anything after slash
    base = code.split('/')[0]
    if len(base) >= 4:
        sym = base[:4]
        if sym in level5_symbols:
            return sym
        return sym
    return None

# Build counts per group per year
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None:
        continue
    cpc_field = rec.get('cpc')
    codes = extract_codes(cpc_field)
    groups_seen = set()
    for code in codes:
        grp = map_to_level5(code)
        if not grp:
            continue
        # Count each publication once per group
        if (grp, year) in groups_seen:
            continue
        counts[grp][year] += 1
        groups_seen.add((grp, year))

# For each group, compute EMA across sorted years with alpha=0.2
alpha = 0.2
best_year_by_group = {}

for grp, year_counts in counts.items():
    # build ordered years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    ema = None
    for y in years:
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema; tie-breaker: choose latest year
    max_ema = max(ema_by_year.values())
    candidates = [y for y,v in ema_by_year.items() if v == max_ema]
    best_year = max(candidates)
    best_year_by_group[grp] = best_year

# Filter groups that are in level5_symbols and whose best_year == 2022
result = [grp for grp, y in best_year_by_group.items() if y == 2022 and grp in level5_symbols]
# sort result
result = sorted(result)

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_YLEJkDoRz4DSg6ej31fUWpLf': 'file_storage/call_YLEJkDoRz4DSg6ej31fUWpLf.json', 'var_call_14kKNjAwdIg9QbXByF74R04z': 'file_storage/call_14kKNjAwdIg9QbXByF74R04z.json'}

exec(code, env_args)

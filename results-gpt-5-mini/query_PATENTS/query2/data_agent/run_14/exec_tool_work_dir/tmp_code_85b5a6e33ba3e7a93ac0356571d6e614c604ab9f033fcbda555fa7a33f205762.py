code = """import json
import os
import re
from collections import defaultdict, OrderedDict

# Load data from storage variables
path_publications = var_call_zCP3LFUTSV3rEcF2l8JYnJOE
path_cpc_defs = var_call_GAb3inX5UHocCa1MPM8xC7zu

# helper to load
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

pubs = load_var(path_publications)
cpc_defs = load_var(path_cpc_defs)

# Build mapping from level-4 symbol to titleFull
cpc_title = {}
for rec in cpc_defs:
    sym = rec.get('symbol')
    title = rec.get('titleFull')
    level = str(rec.get('level'))
    # consider level 4 entries
    if level.startswith('4'):
        cpc_title[sym] = title

# Aggregate counts per group (level-4) per filing year for DE H2 2019 grants
# pubs is a list of records
counts = defaultdict(lambda: defaultdict(int))

year_pattern = re.compile(r"(19|20)\d{2}")
group_pattern = re.compile(r'^([A-Z]\d{2})')

for rec in pubs:
    # extract filing_date year
    filing = rec.get('filing_date') or ''
    m = year_pattern.search(filing)
    if not m:
        # try extracting from other fields
        # skip if no year
        continue
    year = int(m.group(0))
    # parse cpc field (stringified JSON)
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to extract codes via regex
        codes = re.findall(r'"code":\s*"([^"]+)"', cpc_field)
        cpc_list = [{'code': c} for c in codes]
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else entry
        if not code:
            continue
        gm = group_pattern.match(code)
        if not gm:
            continue
        group = gm.group(1)
        counts[group][year] += 1

# For each group, compute EMA over sorted years
alpha = 0.1
results = []
for group, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = OrderedDict()
    ema = None
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    max_ema = max(ema_by_year.values())
    title = cpc_title.get(group, None)
    results.append({'cpc_group': group, 'titleFull': title, 'best_year': best_year, 'max_ema': max_ema, 'years': list(ema_by_year.keys())})

# Sort results by max_ema desc and take top 20
results_sorted = sorted(results, key=lambda x: x['max_ema'], reverse=True)
top_results = results_sorted[:20]

# Prepare output
out = []
for r in top_results:
    out.append({'cpc_group': r['cpc_group'], 'titleFull': r['titleFull'], 'best_year': r['best_year'], 'peak_ema': r['max_ema']})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_AaYFfT87wbBYV07EfrJOtuAr': [], 'var_call_kz7aPMtI11K1uz3UWeL1HmZU': ['cpc_definition'], 'var_call_hoJqb8GkMHFzpqeUvMc5RjRY': 'file_storage/call_hoJqb8GkMHFzpqeUvMc5RjRY.json', 'var_call_eWcWwQyvQfTmoIc0NNqZ6dby': ['publicationinfo'], 'var_call_R4e7pniKG4ctX9zv31FEVaMq': 'file_storage/call_R4e7pniKG4ctX9zv31FEVaMq.json', 'var_call_GAb3inX5UHocCa1MPM8xC7zu': 'file_storage/call_GAb3inX5UHocCa1MPM8xC7zu.json', 'var_call_AcgPAcdzLHqArEzbN6sZOA9M': 'file_storage/call_AcgPAcdzLHqArEzbN6sZOA9M.json', 'var_call_zCP3LFUTSV3rEcF2l8JYnJOE': 'file_storage/call_zCP3LFUTSV3rEcF2l8JYnJOE.json'}

exec(code, env_args)

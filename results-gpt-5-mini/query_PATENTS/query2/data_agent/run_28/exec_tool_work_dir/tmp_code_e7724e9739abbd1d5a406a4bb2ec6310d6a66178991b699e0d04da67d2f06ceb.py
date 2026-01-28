code = """import json
import re
from collections import defaultdict, OrderedDict

# Load the query results from the provided storage file paths
with open(var_call_tDN9p4CjGf8xf55yC1iAcvMp, 'r', encoding='utf-8') as f:
    patents = json.load(f)
with open(var_call_H7MwRYKJicvO0tNY2cyd6sIw, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from level-4 symbol to titleFull
symbol_to_title = {}
for row in cpc_defs:
    sym = row.get('symbol')
    title = row.get('titleFull')
    if sym:
        symbol_to_title[sym] = title

# Helper to extract year from a date-like string
year_re = re.compile(r'(19|20)\d{2}')
code_re = re.compile(r'^([A-Z]\d{2})')

# Count filings per group per year
counts = defaultdict(lambda: defaultdict(int))  # counts[group][year] = count

for rec in patents:
    pat_info = rec.get('Patents_info','') or ''
    # ensure this is Germany; simple check
    if 'DE' not in pat_info and ' Germany' not in pat_info and ' from DE' not in pat_info:
        # skip non-DE
        continue
    filing_date = rec.get('filing_date','') or ''
    year_match = year_re.search(filing_date)
    if not year_match:
        # fallback to grant_date
        year_match = year_re.search(rec.get('grant_date','') or '')
    if not year_match:
        continue
    year = int(year_match.group(0))
    # parse CPC field which is JSON-like
    cpc_field = rec.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix common issues: replace single quotes with double quotes
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    # cpc_list is a list of dicts with 'code'
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        m = code_re.match(code)
        if not m:
            continue
        group = m.group(1)
        counts[group][year] += 1

# For each group, compute EMA over years (ascending) with alpha=0.1
alpha = 0.1
results = []
for group, year_counts in counts.items():
    # sort years
    years_sorted = sorted(year_counts.keys())
    if not years_sorted:
        continue
    ema = None
    ema_by_year = {}
    for y in years_sorted:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with maximum EMA
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    best_ema = ema_by_year[best_year]
    title = symbol_to_title.get(group)
    results.append({
        'cpc_group_code': group,
        'titleFull': title,
        'best_year': best_year,
        'best_ema': round(best_ema,4)
    })

# Sort results by best_ema descending
results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)

# Output only groups at level 4 (mapping exists in symbol_to_title), include all found
# Prepare JSON string
out = json.dumps(results_sorted, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Qk8ScuPqaxnCUGQx7MO5dkV0': 'file_storage/call_Qk8ScuPqaxnCUGQx7MO5dkV0.json', 'var_call_H7MwRYKJicvO0tNY2cyd6sIw': 'file_storage/call_H7MwRYKJicvO0tNY2cyd6sIw.json', 'var_call_7oGBenh6Mbvt3Gr5kQDe2TsI': 'file_storage/call_7oGBenh6Mbvt3Gr5kQDe2TsI.json', 'var_call_tDN9p4CjGf8xf55yC1iAcvMp': 'file_storage/call_tDN9p4CjGf8xf55yC1iAcvMp.json'}

exec(code, env_args)

code = """import json, re

# Load level-5 symbols
data_file_levels = var_call_m9DE7wdk4qJJwEBQ4BiwFqET
if isinstance(data_file_levels, str):
    with open(data_file_levels, 'r', encoding='utf-8') as f:
        level_records = json.load(f)
else:
    level_records = data_file_levels
level_symbols = set()
for r in level_records:
    sym = r.get('symbol') if isinstance(r, dict) else None
    if sym:
        level_symbols.add(sym.strip().upper())

# Load publication records
data_file_pubs = var_call_DogR8Me2oUjvrsoEYZtRefwz
if isinstance(data_file_pubs, str):
    with open(data_file_pubs, 'r', encoding='utf-8') as f:
        pub_records = json.load(f)
else:
    pub_records = data_file_pubs

# Helper to extract year
year_re = re.compile(r"\b(19|20)\d{2}\b")
# Helper to extract group (first 4 chars like C01B or fallback)
group_re = re.compile(r'^([A-Z]\d{2}[A-Z])', re.I)

# Count occurrences per group per year
counts = {}  # {group: {year: count}}
min_year = None
max_year = None

for rec in pub_records:
    filing = rec.get('filing_date', '') or ''
    m = year_re.search(filing)
    if not m:
        # try publication_date or grant_date? skip if no year
        continue
    year = int(m.group(0))
    if min_year is None or year < min_year:
        min_year = year
    if max_year is None or year > max_year:
        max_year = year
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field may be a JSON string
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # maybe already list
        cpc_list = cpc_field if isinstance(cpc_field, list) else []
    # collect unique group symbols for this patent to avoid double counting same group in same doc
    groups_in_doc = set()
    for entry in cpc_list:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code:
            continue
        code = code.strip().upper()
        m2 = group_re.match(code)
        if m2:
            grp = m2.group(1).upper()
        else:
            # fallback to first four alnum chars
            grp = ''.join([c for c in code if c.isalnum()])[:4].upper()
        groups_in_doc.add(grp)
    for grp in groups_in_doc:
        if grp not in level_symbols:
            continue
        counts.setdefault(grp, {}).setdefault(year, 0)
        counts[grp][year] += 1

# If no years found, return empty
if min_year is None:
    result = []
else:
    # compute EMA per group across full year range with alpha=0.2
    alpha = 0.2
    result = []
    for grp, year_counts in counts.items():
        # iterate years from min_year to max_year
        ema = None
        best_year = None
        best_ema = None
        for y in range(min_year, max_year+1):
            val = year_counts.get(y, 0)
            if ema is None:
                ema = val
            else:
                ema = alpha * val + (1-alpha) * ema
            if (best_ema is None) or (ema > best_ema):
                best_ema = ema
                best_year = y
        if best_year == 2022:
            result.append(grp)

# Sort result for consistency
result = sorted(result)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_m9DE7wdk4qJJwEBQ4BiwFqET': 'file_storage/call_m9DE7wdk4qJJwEBQ4BiwFqET.json', 'var_call_DogR8Me2oUjvrsoEYZtRefwz': 'file_storage/call_DogR8Me2oUjvrsoEYZtRefwz.json'}

exec(code, env_args)

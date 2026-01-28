code = """import json, re, os
from collections import defaultdict

# Load level-5 symbols from CPCDefinition query result
data_path = var_call_8suFDN02uyuXAEWg2gYiO5kJ
if isinstance(data_path, str) and os.path.exists(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        level5_rows = json.load(f)
else:
    level5_rows = data_path
level5_symbols = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Load publication records
pub_path = var_call_fhyjtxqxVH1Wm49mEq60Qo5j
if isinstance(pub_path, str) and os.path.exists(pub_path):
    with open(pub_path, 'r', encoding='utf-8') as f:
        pub_rows = json.load(f)
else:
    pub_rows = pub_path

# Helper to extract group code (level-5) from a CPC code like 'C01B33/00' -> 'C01B'
def extract_group(code):
    if not code or not isinstance(code, str):
        return None
    m = re.match(r'^([A-Z]\d{2}[A-Z])', code)
    if m:
        return m.group(1)
    return None

# Helper to extract year from publication_date
def extract_year(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    m = re.findall(r'(\d{4})', date_str)
    if m:
        return int(m[-1])
    return None

# Build counts per group per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()
for rec in pub_rows:
    cpc_field = rec.get('cpc')
    pub_date = rec.get('publication_date')
    year = extract_year(pub_date)
    if year is None:
        continue
    all_years.add(year)
    # cpc_field appears to be a JSON string representing a list
    try:
        codes = json.loads(cpc_field) if isinstance(cpc_field, str) else cpc_field
    except Exception:
        # skip if cannot parse
        continue
    if not isinstance(codes, list):
        continue
    seen_groups = set()
    for entry in codes:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        grp = extract_group(code)
        if not grp:
            continue
        # count each group once per publication (avoid duplicate codes in same publication)
        if grp in seen_groups:
            continue
        seen_groups.add(grp)
        counts[grp][year] += 1

# For each group that is in level5_symbols, compute EMA across its years
alpha = 0.2
result_groups = []
for grp in counts:
    if grp not in level5_symbols:
        continue
    year_counts = counts[grp]
    years = sorted(year_counts.keys())
    if not years:
        continue
    # compute EMA sequentially over the group's years
    ema_by_year = {}
    ema = None
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA
    max_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    if max_year == 2022:
        result_groups.append(grp)

result_groups = sorted(result_groups)

import json
print("__RESULT__:")
print(json.dumps(result_groups))"""

env_args = {'var_call_8suFDN02uyuXAEWg2gYiO5kJ': 'file_storage/call_8suFDN02uyuXAEWg2gYiO5kJ.json', 'var_call_fhyjtxqxVH1Wm49mEq60Qo5j': 'file_storage/call_fhyjtxqxVH1Wm49mEq60Qo5j.json'}

exec(code, env_args)

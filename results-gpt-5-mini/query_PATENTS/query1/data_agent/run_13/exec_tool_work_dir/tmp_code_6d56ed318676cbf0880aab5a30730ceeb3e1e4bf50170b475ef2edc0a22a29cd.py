code = """import json, re
from collections import defaultdict

# Load the large query results from storage file paths
with open(var_call_MHFCNWGmQrU9EXbjRq1OJcQ3, 'r') as f:
    cpc_level5_list = json.load(f)
with open(var_call_CyD7H73Efg7G5TnFWMMXglfs, 'r') as f:
    pubs = json.load(f)

level5_symbols = set()
for d in cpc_level5_list:
    sym = d.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Regex to find 4-digit year
year_re = re.compile(r'(19|20)\d{2}')
# Regex to match first 4-char group like 'A01B' or 'H01M'
group_re = re.compile(r'^([A-Z]\d{2}[A-Z])')

counts = defaultdict(lambda: defaultdict(int))  # group -> year -> count

for rec in pubs:
    fd = rec.get('filing_date') or ''
    m = year_re.search(fd)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc')
    # cpc_field may be a JSON string; attempt to load
    cpc_list = []
    if isinstance(cpc_field, str):
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            # try to extract codes with a simple regex fallback
            codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
            cpc_list = [{"code": c} for c in codes]
    elif isinstance(cpc_field, list):
        cpc_list = cpc_field
    else:
        continue

    groups_in_pub = set()
    for item in cpc_list:
        if isinstance(item, dict):
            code = item.get('code')
        else:
            code = str(item)
        if not code:
            continue
        code = code.strip()
        mg = group_re.match(code)
        if mg:
            grp = mg.group(1)
        else:
            # fallback: take first 4 alnum characters
            compact = ''.join(ch for ch in code if ch.isalnum())
            if len(compact) >= 4:
                grp = compact[:4]
            else:
                continue
        groups_in_pub.add(grp)

    for g in groups_in_pub:
        counts[g][year] += 1

# Compute EMA (alpha=0.2) for each group (only consider groups present in level5 list)
alpha = 0.2
groups_with_peak_2022 = []
for g, year_dict in counts.items():
    if g not in level5_symbols:
        continue
    years = sorted(year_dict.keys())
    if not years:
        continue
    ema_prev = None
    ema_by_year = {}
    for y in years:
        c = year_dict[y]
        if ema_prev is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema_prev
        ema_by_year[y] = ema
        ema_prev = ema
    # find year with max EMA; if tie, choose the latest year
    max_ema = None
    max_year = None
    for y, v in ema_by_year.items():
        if (max_ema is None) or (v > max_ema) or (v == max_ema and y > max_year):
            max_ema = v
            max_year = y
    if max_year == 2022:
        groups_with_peak_2022.append(g)

groups_with_peak_2022_sorted = sorted(groups_with_peak_2022)

import json
print("__RESULT__:")
print(json.dumps(groups_with_peak_2022_sorted))"""

env_args = {'var_call_MHFCNWGmQrU9EXbjRq1OJcQ3': 'file_storage/call_MHFCNWGmQrU9EXbjRq1OJcQ3.json', 'var_call_CyD7H73Efg7G5TnFWMMXglfs': 'file_storage/call_CyD7H73Efg7G5TnFWMMXglfs.json'}

exec(code, env_args)

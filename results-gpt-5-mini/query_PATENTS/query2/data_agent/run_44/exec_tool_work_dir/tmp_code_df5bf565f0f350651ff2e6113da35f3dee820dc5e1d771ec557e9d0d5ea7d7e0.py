code = """import json,re
# Load data from previous query results stored as files
pub_path = var_call_PyBy7XKF31n9GnG8PB6TS6dz
cpc_path = var_call_BBQJ17mlNqW2GCZO7LQYElYR

with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpcs_level4 = json.load(f)

# Build map of level-4 symbols to titleFull
level4_map = {}
for r in cpcs_level4:
    sym = r.get('symbol')
    title = r.get('titleFull')
    if sym:
        level4_map[sym] = title

level4_symbols = sorted(level4_map.keys(), key=lambda x: -len(x))  # long-first for prefix matching

# Helper to extract CPC codes from the cpc field (stringified JSON array)
def extract_codes(cpc_field):
    codes = []
    if not cpc_field:
        return codes
    try:
        arr = json.loads(cpc_field)
        for entry in arr:
            code = entry.get('code')
            if code:
                codes.append(code.strip())
    except Exception:
        # fallback: try to find patterns like A12B3/45
        codes = re.findall(r"[A-HY][0-9]{1,2}[A-Z]?[^,\]\s]{0,}\/?[0-9]*", cpc_field)
    return codes

# Count filings per year for each matched level-4 group
counts = {}  # group -> {year: count}

for rec in pubs:
    filing_date = rec.get('filing_date') or ''
    # extract year from filing_date
    m = re.search(r"(19|20)\d{2}", filing_date)
    if not m:
        # skip if no filing year
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc') or ''
    codes = extract_codes(cpc_field)
    for code in codes:
        # find longest matching level4 symbol prefix
        matched = None
        for sym in level4_symbols:
            if code.startswith(sym):
                matched = sym
                break
        if not matched:
            continue
        counts.setdefault(matched, {})
        counts[matched][year] = counts[matched].get(year, 0) + 1

# For each group, compute EMA across years with alpha=0.1 and find year with max EMA
alpha = 0.1
results = []
for group, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    # build series
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    if not ema_by_year:
        continue
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    results.append({
        'cpc_group_code': group,
        'titleFull': level4_map.get(group),
        'best_year': best_year
    })

# Sort results by group code
results = sorted(results, key=lambda x: x['cpc_group_code'])

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_0gud4zSE6xreBOgzX8Kc12sB': 'file_storage/call_0gud4zSE6xreBOgzX8Kc12sB.json', 'var_call_p9k2i3cLI77FaTmWla24K6ji': 'file_storage/call_p9k2i3cLI77FaTmWla24K6ji.json', 'var_call_PyBy7XKF31n9GnG8PB6TS6dz': 'file_storage/call_PyBy7XKF31n9GnG8PB6TS6dz.json', 'var_call_BBQJ17mlNqW2GCZO7LQYElYR': 'file_storage/call_BBQJ17mlNqW2GCZO7LQYElYR.json', 'var_call_zawGmnUMCk8fSNf6UcQ6W1lp': 'file_storage/call_zawGmnUMCk8fSNf6UcQ6W1lp.json'}

exec(code, env_args)

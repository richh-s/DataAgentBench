code = """import json, re
# Load the query results from storage file paths
with open(var_call_C6jNBhBbdCkrxA7izMxbw2Qh, 'r', encoding='utf-8') as f:
    patents = json.load(f)
with open(var_call_kzAI1h9qwE9DiOHvEnxfNYi5, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build symbol -> titleFull map
title_map = {r['symbol']: r.get('titleFull', '') for r in cpc_defs}

# Helper to extract level-4 symbol: first letter + two digits (e.g., A61, B30, G07)
def extract_level4(code):
    if not code or not isinstance(code, str):
        return None
    m = re.match(r'^([A-Z]\d{2})', code)
    if m:
        return m.group(1)
    # fallback: take first 3 chars
    return code[:3]

# Helper to extract year from filing_date or grant_date
year_re = re.compile(r'\b(19|20)\d{2}\b')

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# Aggregate counts per level4 symbol per filing year
from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))

for rec in patents:
    # Ensure it's a German patent row via Patents_info containing 'DE'
    info = rec.get('Patents_info','')
    if 'DE' not in info:
        continue
    filing = rec.get('filing_date') or ''
    grant = rec.get('grant_date') or ''
    year = extract_year(filing) or extract_year(grant)
    if not year:
        continue
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to sanitize single quotes
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            cpc_list = []
    # For each cpc code in list, increment count for its level4 symbol
    for c in cpc_list:
        code = c.get('code') if isinstance(c, dict) else None
        if not code:
            continue
        sym = extract_level4(code)
        if not sym:
            continue
        counts[sym][year] += 1

# For each symbol, compute EMA over sorted years with alpha=0.1 and find year with max EMA
alpha = 0.1
results = []
for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda kv: kv[1])[0]
    best_ema = ema_by_year[best_year]
    results.append({
        'symbol': sym,
        'titleFull': title_map.get(sym, ''),
        'best_year': best_year,
        'best_ema': round(float(best_ema),4)
    })

# Sort results by best_ema descending and limit to those with non-empty title maybe
results_sorted = sorted(results, key=lambda r: r['best_ema'], reverse=True)

# Output only requested fields: full title, CPC group code, best year
out = [{'titleFull': r['titleFull'], 'symbol': r['symbol'], 'best_year': r['best_year']} for r in results_sorted]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_eb9dGoRjEOgfsqeIrFu0y5A0': 'file_storage/call_eb9dGoRjEOgfsqeIrFu0y5A0.json', 'var_call_kzAI1h9qwE9DiOHvEnxfNYi5': 'file_storage/call_kzAI1h9qwE9DiOHvEnxfNYi5.json', 'var_call_C6jNBhBbdCkrxA7izMxbw2Qh': 'file_storage/call_C6jNBhBbdCkrxA7izMxbw2Qh.json'}

exec(code, env_args)

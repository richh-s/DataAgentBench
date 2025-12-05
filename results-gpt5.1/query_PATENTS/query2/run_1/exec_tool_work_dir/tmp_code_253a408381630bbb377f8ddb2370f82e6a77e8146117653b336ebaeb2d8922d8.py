code = """import json, re, pandas as pd
from datetime import datetime

# Load full grants data
with open(var_call_87YyQoDbVHsI0HcOxwcv2fsb, 'r') as f:
    grants = json.load(f)

# Filter to Germany using Patents_info country code 'DE'
country_pattern = re.compile(r'\bDE\b')

def is_germany(info):
    return bool(country_pattern.search(info or ''))

filtered = [g for g in grants if is_germany(g.get('Patents_info', ''))]

# Parse grant_date to year
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    if not date_str:
        return None
    # extract 4-digit year
    m = re.search(r'(20\d{2})', date_str)
    return int(m.group(1)) if m else None

for g in filtered:
    g['year'] = parse_year(g.get('grant_date', ''))

filtered = [g for g in filtered if g.get('year') is not None]

# explode CPC codes, normalise to level-4 group (first 3 characters) as per examples
rows = []
for g in filtered:
    year = g['year']
    cpc_raw = g.get('cpc')
    try:
        codes = json.loads(cpc_raw) if cpc_raw else []
    except Exception:
        continue
    for entry in codes:
        code = entry.get('code','')
        if not code:
            continue
        # Take section+2 digits as group, e.g., A61B... -> A61
        m = re.match(r'([A-HY]\d{2})', code)
        if not m:
            continue
        group = m.group(1)
        rows.append({'group': group, 'year': year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # count filings per group-year
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # build yearly range per group
    out_rows = []
    alpha = 0.1
    for group, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        years = list(range(sub['year'].min(), sub['year'].max()+1))
        year_to_count = {int(r.year): int(r['count']) for r in sub.itertuples(index=False)}
        ema = None
        best_year = None
        best_ema = None
        for y in years:
            c = year_to_count.get(y, 0)
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = y
        out_rows.append({'group': group, 'best_year': best_year, 'best_ema': best_ema})
    result = out_rows

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_87YyQoDbVHsI0HcOxwcv2fsb': 'file_storage/call_87YyQoDbVHsI0HcOxwcv2fsb.json', 'var_call_W3E1h6GZymbx68sfRqdhEICq': 'file_storage/call_W3E1h6GZymbx68sfRqdhEICq.json', 'var_call_4PWOpWdWjQI24LfrqUBlhu8L': ['publicationinfo'], 'var_call_0t82ItFDGZGx7y7NMUpCBg1s': ['cpc_definition']}

exec(code, env_args)

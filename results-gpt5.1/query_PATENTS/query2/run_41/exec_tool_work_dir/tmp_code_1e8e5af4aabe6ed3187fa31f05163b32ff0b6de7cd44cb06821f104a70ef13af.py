code = """import json, re, pandas as pd
from datetime import datetime

# Load large query results from files
with open(var_call_8D3Qr7BY7DbufLAbFIv97G00, 'r') as f:
    grants = json.load(f)
with open(var_call_Cj4SsQJqDbtpZYtdVGwiTp9U, 'r') as f:
    cpc_defs = json.load(f)

# Filter to Germany using Patents_info country code "DE"
country_pattern = re.compile(r'\bDE\b')
filtered_grants = []
for rec in grants:
    info = rec.get('Patents_info') or ''
    if country_pattern.search(info):
        filtered_grants.append(rec)

# Parse natural-language grant_date to year
months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

 def parse_year(date_str):
    if not date_str:
        return None
    # Extract year as 4 digits
    m = re.search(r'(19|20)\d{2}', date_str)
    if m:
        return int(m.group(0))
    return None

for rec in filtered_grants:
    rec['year'] = parse_year(rec.get('grant_date') or '')

# Explode CPC codes per patent
rows = []
for rec in filtered_grants:
    year = rec.get('year')
    if not year:
        continue
    cpc_raw = rec.get('cpc') or '[]'
    try:
        codes = json.loads(cpc_raw)
    except Exception:
        continue
    for c in codes:
        code = c.get('code')
        if not code:
            continue
        # Level 4 group code approximated as first 3 characters (section+class)?
        # Better: take up to first non-alphanumeric? But here use first 3 for main class like "A61".
        m = re.match(r'([A-Z]\d\d)', code)
        if not m:
            continue
        group = m.group(1)
        rows.append({'group': group, 'year': year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Count patents per group per year
    counts = df.groupby(['group','year']).size().reset_index(name='count')

    # Compute EMA per group across years sorted ascending, alpha=0.1
    alpha = 0.1
    ema_records = []
    for group, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            y = r['year']; c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_records.append({'group': group, 'year': int(y), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)
    # For each group, get year with highest EMA
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # Map to CPC definitions at level 4 (symbol and titleFull)
    defs_df = pd.DataFrame(cpc_defs)
    # level might be float-like strings; keep all and match symbol
    defs_df['symbol'] = defs_df['symbol'].astype(str)
    defs_df['titleFull'] = defs_df['titleFull'].astype(str)

    merged = best.merge(defs_df[['symbol','titleFull']], left_on='group', right_on='symbol', how='left')
    merged = merged[['group','titleFull','year','ema']]
    merged = merged.sort_values('ema', ascending=False)

    result = merged.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8D3Qr7BY7DbufLAbFIv97G00': 'file_storage/call_8D3Qr7BY7DbufLAbFIv97G00.json', 'var_call_Cj4SsQJqDbtpZYtdVGwiTp9U': 'file_storage/call_Cj4SsQJqDbtpZYtdVGwiTp9U.json', 'var_call_QIPB7fuXBoCVFJkDrHIhNfpA': ['publicationinfo'], 'var_call_tkA9VyMdsOpAlHSnKoDAtzIS': ['cpc_definition']}

exec(code, env_args)

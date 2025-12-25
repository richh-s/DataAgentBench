code = """import json, re, pandas as pd

# Load large query results from files
grants_path = var_call_8D3Qr7BY7DbufLAbFIv97G00
cpc_defs_path = var_call_Cj4SsQJqDbtpZYtdVGwiTp9U
with open(grants_path, 'r') as f:
    grants = json.load(f)
with open(cpc_defs_path, 'r') as f:
    cpc_defs = json.load(f)

# Filter to Germany using country code "DE" in Patents_info
country_pattern = re.compile(r'\bDE\b')
filtered_grants = []
for rec in grants:
    info = rec.get('Patents_info') or ''
    if country_pattern.search(info):
        filtered_grants.append(rec)

# Parse year from grant_date
def parse_year(date_str):
    if not date_str:
        return None
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
        m = re.match(r'([A-Z]\d\d)', code)
        if not m:
            continue
        group = m.group(1)
        rows.append({'group': group, 'year': year})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['group','year']).size().reset_index(name='count')

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
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    defs_df = pd.DataFrame(cpc_defs)
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

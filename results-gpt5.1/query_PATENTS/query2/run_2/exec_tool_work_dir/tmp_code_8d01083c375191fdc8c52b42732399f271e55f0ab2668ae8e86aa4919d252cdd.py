code = """import json, re, pandas as pd

# Load full publication data
with open(var_call_SsgIdKfqvKy6AQNDwhGONP1j, 'r') as f:
    pubs = json.load(f)

# Filter to Germany using Patents_info country code "DE-"
pat_de = []
for r in pubs:
    info = r.get('Patents_info') or ''
    if ' DE-' in info or ' DE' in info or 'Germany' in info or ' DE,' in info or ' DE.' in info:
        pat_de.append(r)

# Parse natural-language grant_date into year (4-digit)
def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

records = []
for r in pat_de:
    year = extract_year(r.get('grant_date',''))
    if year is None:
        continue
    cpc_raw = r.get('cpc') or '[]'
    try:
        codes = [c.get('code') for c in json.loads(cpc_raw) if c.get('code')]
    except Exception:
        continue
    for code in codes:
        # derive level-4 group: use prefix up to first space or first slash-level pattern
        # Simplify: take up to first '/' if present, else full main group
        lvl4 = code.split('/')[0]
        records.append({'year': year, 'cpc_group4': lvl4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per year per group
    counts = df.groupby(['cpc_group4','year']).size().reset_index(name='count')
    # For each group compute EMA over years sorted ascending
    alpha = 0.1
    best_rows = []
    for grp, gdf in counts.groupby('cpc_group4'):
        gdf = gdf.sort_values('year')
        ema = None
        best_year = None
        best_ema = None
        for _, row in gdf.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = int(row['year'])
        best_rows.append({'cpc_group4': grp, 'best_year': best_year, 'best_ema': best_ema})
    best_df = pd.DataFrame(best_rows)
    # Keep groups with highest EMA (top 20 for practicality)
    best_df = best_df.sort_values('best_ema', ascending=False).head(20)
    result = best_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SsgIdKfqvKy6AQNDwhGONP1j': 'file_storage/call_SsgIdKfqvKy6AQNDwhGONP1j.json', 'var_call_wXZTOBJamxc1YxAIxc1zoTcs': 'file_storage/call_wXZTOBJamxc1YxAIxc1zoTcs.json'}

exec(code, env_args)

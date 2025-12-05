code = """import json, re, pandas as pd

# Load full publication data
with open(var_call_7dGfNYcAAcuxvDMSxEqR8sJz, 'r') as f:
    pubs = json.load(f)

# Filter to Germany using Patents_info country code 'DE'
pat_de = []
for r in pubs:
    info = r.get('Patents_info') or ''
    if ' DE ' in info or ' DE-' in info or 'from DE,' in info or 'the DE application' in info:
        pat_de.append(r)

# Parse year from grant_date (natural language)
def extract_year(s):
    if not s:
        return None
    m = re.search(r'(20\d{2})', s)
    return int(m.group(1)) if m else None

for r in pat_de:
    r['year'] = extract_year(r.get('grant_date',''))

pat_de = [r for r in pat_de if r.get('year')]

# Extract CPC codes (full codes) from JSON-like cpc field
records = []
for r in pat_de:
    cpc_raw = r.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    year = r['year']
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # level 4 group code: first 3 characters (section+class+subclass or main group). Assume 3-char symbols to match level 4 table
        grp = code[:3]
        records.append({'group4': grp, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per group per year
    counts = df.groupby(['group4','year']).size().reset_index(name='count')
    # Compute EMA per group over years ascending
    alphas = 0.1
    best_rows = []
    for g, sub in counts.groupby('group4'):
        sub = sub.sort_values('year')
        ema = None
        best_ema = None
        best_year = None
        for _, row in sub.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alphas * c + (1-alphas) * ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = int(row['year'])
        best_rows.append({'group4': g, 'best_year': best_year, 'best_ema': best_ema})
    best_df = pd.DataFrame(best_rows)
    # Keep groups with highest EMA (top, but question slightly vague; return all with their best year and EMA)
    # We'll join titles later
    result = best_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7dGfNYcAAcuxvDMSxEqR8sJz': 'file_storage/call_7dGfNYcAAcuxvDMSxEqR8sJz.json', 'var_call_s3DqhAJjxPFAEIxAdE1Ba3Pz': 'file_storage/call_s3DqhAJjxPFAEIxAdE1Ba3Pz.json'}

exec(code, env_args)

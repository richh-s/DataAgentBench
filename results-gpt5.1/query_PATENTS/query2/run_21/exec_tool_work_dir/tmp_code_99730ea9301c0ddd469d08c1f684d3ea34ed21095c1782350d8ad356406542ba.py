code = """import json, re, pandas as pd

# Load full results for publicationinfo query
path_pubs = var_call_HyP0mjSxb0dodCrS5P5BxCcG
with open(path_pubs, 'r') as f:
    pubs = json.load(f)

# Filter to Germany using Patents_info containing ' DE-' or ' DE '
# Here we look for ' DE-' in publication number pattern 'DE-xxxx'
pat = re.compile(r'\bDE-')
pubs_de = [r for r in pubs if pat.search(r.get('Patents_info',''))]

# Parse grant year from natural-language grant_date (look for a 4-digit year)
for r in pubs_de:
    gd = r.get('grant_date','') or ''
    m = re.search(r'(20\d{2})', gd)
    r['grant_year'] = int(m.group(1)) if m else None

pubs_de = [r for r in pubs_de if r.get('grant_year') is not None]

# Extract CPC codes (list of dicts) from JSON-like string
records = []
for r in pubs_de:
    cpc_str = r.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_str)
    except Exception:
        # try to fix minor issues
        try:
            cpc_list = json.loads(cpc_str.replace("'", '"'))
        except Exception:
            cpc_list = []
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # derive level-4 group: take first 3 chars (letter+2 digits) as class; but CPC level4 likely main class (1 letter+2 digits)
        # From cpc_definition preview, level 4 symbols are like 'A61', 'B04' etc.
        m = re.match(r'([A-HY][0-9]{2})', code)
        if not m:
            continue
        group = m.group(1)
        records.append({'group': group, 'year': r['grant_year']})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per year per group
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # Build full year range per group
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    groups = counts['group'].unique()
    rows = []
    alpha = 0.1
    for g in groups:
        sub = counts[counts['group']==g].set_index('year')['count']
        ema = None
        for y in sorted(all_years):
            c = int(sub.get(y, 0))
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            rows.append({'group': g, 'year': y, 'ema': float(ema)})
    ema_df = pd.DataFrame(rows)
    # For each group, find year with max EMA
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    best.rename(columns={'year':'best_year','ema':'best_ema'}, inplace=True)
    result = best.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HyP0mjSxb0dodCrS5P5BxCcG': 'file_storage/call_HyP0mjSxb0dodCrS5P5BxCcG.json', 'var_call_4Twe9lfa4fwHAZVoxcAKAtEa': 'file_storage/call_4Twe9lfa4fwHAZVoxcAKAtEa.json'}

exec(code, env_args)

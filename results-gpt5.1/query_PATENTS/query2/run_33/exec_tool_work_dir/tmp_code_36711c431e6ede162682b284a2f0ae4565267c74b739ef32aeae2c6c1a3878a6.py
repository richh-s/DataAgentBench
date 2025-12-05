code = """import json, re, pandas as pd

# Load full publication data
path_pubs = var_call_UeIr5uRsysw2vgQLd1qggBnW
with open(path_pubs, 'r') as f:
    pubs = json.load(f)

# Filter to Germany using Patents_info country code 'DE'
pattern = re.compile(r'\bDE\b')
filtered_pubs = [r for r in pubs if pattern.search(r.get('Patents_info',''))]

# Parse year from grant_date (last 4-digit number)
def extract_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(20\d{2}|19\d{2})', date_str)
    return int(m.group(1)) if m else None

records = []
for r in filtered_pubs:
    year = extract_year(r.get('grant_date',''))
    if not year:
        continue
    # parse CPC JSON-like string
    cpc_raw = r.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # Reduce to CPC group at level 4: take first 3 characters (section+class) e.g., A61
        group = code[:3]
        records.append({'year': year, 'group': group})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per year per group
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # Build full year range for EMA calculation
    all_years = sorted(counts['year'].unique())
    alpha = 0.1
    ema_rows = []
    for g, sub in counts.groupby('group'):
        sub = sub.set_index('year').reindex(all_years, fill_value=0)
        ema = None
        for y in all_years:
            c = sub.loc[y, 'count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_rows.append({'group': g, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # For each group, find year with max EMA
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    result = best.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_UeIr5uRsysw2vgQLd1qggBnW': 'file_storage/call_UeIr5uRsysw2vgQLd1qggBnW.json', 'var_call_fj8SQVd0XSA53FLEZF2Sm1FS': 'file_storage/call_fj8SQVd0XSA53FLEZF2Sm1FS.json'}

exec(code, env_args)

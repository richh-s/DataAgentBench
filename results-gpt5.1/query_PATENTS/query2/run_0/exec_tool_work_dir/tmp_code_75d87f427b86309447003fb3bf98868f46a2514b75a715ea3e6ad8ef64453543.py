code = """import json, re, pandas as pd

# Load full query results from files
with open(var_call_HqPrcGmWMKcpOefvTEHEOsaJ, 'r') as f:
    grants = json.load(f)
with open(var_call_BwI1Zgd68eYvo2YRrJbKpcLZ, 'r') as f:
    cpc_defs = json.load(f)

# Filter to Germany using Patents_info country code 'DE'
country_pattern = re.compile(r'\bfrom DE\b|\bDE application\b|\bin DE, the application\b|\bthe DE patent application\b|\bfrom Germany\b', re.IGNORECASE)

grants_de = [g for g in grants if country_pattern.search(g.get('Patents_info',''))]

# Helper to parse natural-language grant_year
year_pattern = re.compile(r'(19|20)\d{2}')
for g in grants_de:
    gd = g.get('grant_date','') or ''
    m = year_pattern.search(gd)
    g['grant_year'] = int(m.group(0)) if m else None

# Extract CPC codes per grant
records = []
for g in grants_de:
    year = g.get('grant_year')
    if not year:
        continue
    cpc_raw = g.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        # Level-4 group: take section+class (first 3 chars as in defs like "A61", "B04")
        group = code[:3]
        records.append({'group': group, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per group-year
    counts = df.groupby(['group','year']).size().reset_index(name='count')
    # Ensure continuous years per group
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    groups = counts['group'].unique()
    ema_rows = []
    alpha = 0.1
    for gcode in groups:
        sub = counts[counts['group']==gcode].set_index('year')['count']
        # reindex over all years, fill missing with 0
        sub = sub.reindex(all_years, fill_value=0)
        ema = None
        for y, c in sub.items():
            if ema is None:
                ema = c  # start EMA at first observed count
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_rows.append({'group': gcode, 'year': y, 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # For each group, find year with max EMA
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # Map to CPC titles (level 4)
    defs_df = pd.DataFrame(cpc_defs)
    defs_df['symbol'] = defs_df['symbol'].astype(str)
    defs_df_lvl4 = defs_df[defs_df['level'].astype(float)==4.0][['symbol','titleFull']]

    merged = best.merge(defs_df_lvl4, left_on='group', right_on='symbol', how='left')
    merged = merged.sort_values('ema', ascending=False)
    result = []
    for _, row in merged.iterrows():
        result.append({
            'cpc_group_code': row['group'],
            'titleFull': row.get('titleFull'),
            'best_year': int(row['year']),
            'max_ema_filings': row['ema']
        })

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HqPrcGmWMKcpOefvTEHEOsaJ': 'file_storage/call_HqPrcGmWMKcpOefvTEHEOsaJ.json', 'var_call_BwI1Zgd68eYvo2YRrJbKpcLZ': 'file_storage/call_BwI1Zgd68eYvo2YRrJbKpcLZ.json', 'var_call_oSSGBO3p4x9onabcAmIt4D2B': ['publicationinfo'], 'var_call_TeHhyjgfzbFg0cQlIBrLZrKq': ['cpc_definition']}

exec(code, env_args)

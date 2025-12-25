code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_hQOKZpZYpAE0oStVV4TZF4Kl, 'r') as f:
    grants = json.load(f)
with open(var_call_aQRjCXXNdph5Upr1jSQ411FJ, 'r') as f:
    cpc_defs = json.load(f)

# Filter to Germany using Patents_info containing ' DE '
rows_de = []
for r in grants:
    info = r.get('Patents_info','')
    # crude country detection: ' DE ' or ' DE,' or ' DE.' or ' DE-'
    if re.search(r'\bDE\b', info):
        rows_de.append(r)

# Parse grant year from grant_date (last 4-digit year in string)
for r in rows_de:
    m = re.search(r'(20[0-9]{2})', r.get('grant_date',''))
    r['year'] = int(m.group(1)) if m else None

rows_de = [r for r in rows_de if r.get('year')]

# Extract CPC codes; map to level-4 group = first 3 characters of code (letter+2 digits)
patent_rows = []
for r in rows_de:
    try:
        cpc_list = json.loads(r.get('cpc','[]'))
    except Exception:
        continue
    for e in cpc_list:
        code = e.get('code')
        if not code:
            continue
        m = re.match(r'^[A-HY][0-9]{2}', code)
        if not m:
            continue
        group = m.group(0)
        patent_rows.append({'group': group, 'year': r['year']})

if not patent_rows:
    result = []
else:
    df = pd.DataFrame(patent_rows)
    counts = df.groupby(['group','year']).size().reset_index(name='count')

    # Build complete year range per group
    all_years = range(counts['year'].min(), counts['year'].max()+1)
    res_rows = []
    alpha = 0.1
    for g, sub in counts.groupby('group'):
        sub = sub.set_index('year').reindex(all_years, fill_value=0).reset_index()
        ema = []
        prev = sub.loc[0,'count']
        ema.append(prev)
        for i in range(1, len(sub)):
            v = sub.loc[i,'count']
            prev = alpha*v + (1-alpha)*prev
            ema.append(prev)
        sub['ema'] = ema
        best_idx = sub['ema'].idxmax()
        best_year = int(sub.loc[best_idx,'year'])
        best_ema = float(sub.loc[best_idx,'ema'])
        res_rows.append({'group': g, 'best_year': best_year, 'best_ema': best_ema})

    res_df = pd.DataFrame(res_rows)
    # Join with cpc definitions on symbol == group
    defs_df = pd.DataFrame(cpc_defs)
    defs_df = defs_df[['symbol','titleFull','level']]
    defs_df['level'] = defs_df['level'].astype(float)
    defs_df4 = defs_df[defs_df['level']==4.0]
    merged = res_df.merge(defs_df4, left_on='group', right_on='symbol', how='left')
    merged = merged.sort_values('best_ema', ascending=False).head(20)
    out = merged[['group','titleFull','best_year','best_ema']]
    result = out.to_dict(orient='records')

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_hQOKZpZYpAE0oStVV4TZF4Kl': 'file_storage/call_hQOKZpZYpAE0oStVV4TZF4Kl.json', 'var_call_aQRjCXXNdph5Upr1jSQ411FJ': 'file_storage/call_aQRjCXXNdph5Upr1jSQ411FJ.json', 'var_call_pqFqSndMFx9qiM7kJ5ujIFl0': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}]}

exec(code, env_args)

code = """import json, re, pandas as pd

# Load full large results from files
with open(var_call_oMSc5cgizTKptkcPjKdIH7gO, 'r') as f:
    data_2019 = json.load(f)
with open(var_call_0Hc4GFfcoVDdc9w8th9YoSEu, 'r') as f:
    data_hist = json.load(f)
with open(var_call_xlucStlgDNU81CqyR8dagQQO, 'r') as f:
    cpc_defs = json.load(f)

# Helper to get country code from Patents_info
cc_re = re.compile(r'In ([A-Z]{2}),|from ([A-Z]{2}),|from ([A-Z]{2}) |The ([A-Z]{2}) patent|In ([A-Z]{2}) |Application \(ID ([A-Z]{2})-|Application \(number ([A-Z]{2})-|Patent filing \(application no. ([A-Z]{2})-|Patent application \(no. ([A-Z]{2})')

def get_cc(text):
    m = cc_re.search(text)
    if not m:
        return None
    for i in range(1, m.lastindex+1):
        if m.group(i):
            return m.group(i)
    return None

# Filter to Germany (DE) and grant in H2 2019
records_2019 = []
for r in data_2019:
    if get_cc(r['Patents_info']) != 'DE':
        continue
    # crude year 2019 already filtered by SQL; ensure month is Jul-Dec is already done
    records_2019.append(r)

# Historical records for EMA: only DE
records_hist = [r for r in data_hist if get_cc(r['Patents_info']) == 'DE']

# Function to parse grant year (fallbacks)
year_re = re.compile(r'(20\d{2})')

def get_year(s):
    m = year_re.search(s or '')
    return int(m.group(1)) if m else None

for r in records_2019:
    r['year'] = get_year(r['grant_date'])
for r in records_hist:
    r['year'] = get_year(r['grant_date'])

records_2019 = [r for r in records_2019 if r['year'] is not None]
records_hist = [r for r in records_hist if r['year'] is not None]

# Parse CPC list and get group at level 4 (section+2-digit class)

def extract_cpcs(cpc_json_str):
    try:
        arr = json.loads(cpc_json_str)
    except Exception:
        return []
    res = []
    for it in arr:
        code = it.get('code')
        if not code:
            continue
        # get high-level group: first letter + next two digits
        m = re.match(r'([A-HY]\d{2})', code)
        if m:
            res.append(m.group(1))
    return list(set(res))

for r in records_2019:
    r['groups'] = extract_cpcs(r['cpc'])
for r in records_hist:
    r['groups'] = extract_cpcs(r['cpc'])

# Build yearly counts per group
rows = []
for r in records_hist + records_2019:
    y = r['year']
    for g in r['groups']:
        rows.append({'year': y, 'group': g, 'count': 1})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    df = df.groupby(['group','year'])['count'].sum().reset_index()

    # compute EMA per group over years sorted ascending, alpha=0.1
    alpha = 0.1
    ema_rows = []
    for g, gdf in df.sort_values('year').groupby('group'):
        ema = None
        for _, row in gdf.sort_values('year').iterrows():
            y = int(row['year'])
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'group': g, 'year': y, 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)

    # Restrict to groups that appear in DE patents granted H2 2019
    groups_2019 = set([g for r in records_2019 for g in r['groups']])
    ema_2019 = ema_df[ema_df['group'].isin(groups_2019)]

    # For each group, find year with max EMA
    idx = ema_2019.groupby('group')['ema'].idxmax()
    best_df = ema_2019.loc[idx].copy()

    # Map to CPC definitions level 4
    defs_df = pd.DataFrame(cpc_defs)
    defs_df = defs_df.rename(columns={'symbol':'group', 'titleFull':'titleFull'})
    best_df = best_df.merge(defs_df[['group','titleFull']], on='group', how='left')

    best_df = best_df.sort_values('ema', ascending=False)
    result = best_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oMSc5cgizTKptkcPjKdIH7gO': 'file_storage/call_oMSc5cgizTKptkcPjKdIH7gO.json', 'var_call_xlucStlgDNU81CqyR8dagQQO': 'file_storage/call_xlucStlgDNU81CqyR8dagQQO.json', 'var_call_0Hc4GFfcoVDdc9w8th9YoSEu': 'file_storage/call_0Hc4GFfcoVDdc9w8th9YoSEu.json'}

exec(code, env_args)

code = """import json, pandas as pd, re

pub_path = var_call_z4PkV7FWRypH9YgYcVlPG11E
cpcdef_path = var_call_cLDtjpsBckPNwOfOX0LAhX3l

with open(pub_path, 'r') as f:
    pub_data = json.load(f)
with open(cpcdef_path, 'r') as f:
    cpcdef_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year

def parse_year(s):
    if not isinstance(s, str) or not s.strip():
        return None
    m = re.search(r'(19|20)\d{2}', s)
    if m:
        return int(m.group(0))
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

codes = []
for _, row in pub_df.iterrows():
    cpc_raw = row['cpc']
    year = row['year']
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        lst = json.loads(cpc_raw)
    except Exception:
        continue
    if not isinstance(lst, list):
        continue
    for entry in lst:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code:
            continue
        codes.append({'code': code, 'year': year})

code_df = pd.DataFrame(codes)

cpcdef_df = pd.DataFrame(cpcdef_data)

# symbols in cpc_definition may be truncated higher-level codes; we need level==5 but full group codes
cpcdef_df['level'] = cpcdef_df['level'].astype(float)
level5 = set(cpcdef_df[cpcdef_df['level'] == 5.0]['symbol'].astype(str).unique())

code_df = code_df[code_df['code'].isin(level5)]

if code_df.empty:
    result_codes = []
else:
    counts = code_df.groupby(['code','year']).size().reset_index(name='count')
    alpha = 0.2
    records = []
    for code, grp in counts.groupby('code'):
        grp = grp.sort_values('year')
        ema = None
        for _, r in grp.iterrows():
            y = int(r['year'])
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            records.append({'code': code, 'year': y, 'ema': float(ema)})

    ema_df = pd.DataFrame(records)
    best = ema_df.sort_values(['code','ema','year'], ascending=[True,False,True]).groupby('code').head(1)
    best_2022 = best[best['year'] == 2022]
    result_codes = sorted(best_2022['code'].unique().tolist())

import json as _json
out = _json.dumps(result_codes)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_z4PkV7FWRypH9YgYcVlPG11E': 'file_storage/call_z4PkV7FWRypH9YgYcVlPG11E.json', 'var_call_cLDtjpsBckPNwOfOX0LAhX3l': 'file_storage/call_cLDtjpsBckPNwOfOX0LAhX3l.json', 'var_call_9y4UgyDXSSl0K4r51M1NEAIN': {'sample_entry': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, 'keys': ['code', 'first', 'inventive', 'tree']}}

exec(code, env_args)

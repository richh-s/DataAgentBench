code = """import json, pandas as pd, re, datetime as dt

# Load full results
with open(var_call_PMhurUdNQCJWEg4NOh48IGTB, 'r') as f:
    pubs = json.load(f)
with open(var_call_ZHWjhcVBYlvE9tSg5nCuFoV9, 'r') as f:
    lvl5 = json.load(f)

pubs_df = pd.DataFrame(pubs)

# Parse year from natural-language publication_date
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def get_year(s):
    if not isinstance(s,str) or not s.strip():
        return None
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}[a-z]{2},?\s+(\d{4})', s)
    if not m:
        m = re.search(r'(\d{4})', s)
        return int(m.group(1)) if m else None
    return int(m.group(2))

pubs_df['year'] = pubs_df['publication_date'].apply(get_year)
pubs_df = pubs_df.dropna(subset=['year'])
pubs_df['year'] = pubs_df['year'].astype(int)

# Extract CPC codes

def extract_codes(cpc_str):
    if not isinstance(cpc_str,str) or not cpc_str.strip():
        return []
    try:
        data = json.loads(cpc_str)
        return [d.get('code') for d in data if isinstance(d, dict) and d.get('code')]
    except Exception:
        # fallback regex
        return re.findall(r'[A-HY][0-9]{2}[A-Z](?:[0-9]{1,4}/[0-9]{2,})?', cpc_str)

pubs_df['codes'] = pubs_df['cpc'].apply(extract_codes)

rows = []
for _, r in pubs_df.iterrows():
    y = r['year']
    for code in r['codes']:
        rows.append({'year': y, 'code': code})

if not rows:
    result = []
else:
    codes_df = pd.DataFrame(rows)
    yearly_counts = codes_df.groupby(['code','year']).size().reset_index(name='count')

    # Compute EMA per code ordered by year
    alpha = 0.2
    ema_records = []
    for code, grp in yearly_counts.sort_values(['code','year']).groupby('code'):
        ema = None
        for _, row in grp.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_records.append({'code': code, 'year': int(row['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)

    # For each code, find year with max EMA
    idx = ema_df.groupby('code')['ema'].idxmax()
    best_df = ema_df.loc[idx].copy()

    # Keep only codes whose best year is 2022
    best_2022 = best_df[best_df['year'] == 2022]

    # Filter to CPC level 5 symbols
    lvl5_df = pd.DataFrame(lvl5)
    lvl5_codes = set(lvl5_df['symbol'].astype(str))

    best_2022_lvl5 = best_2022[best_2022['code'].isin(lvl5_codes)]

    result = sorted(best_2022_lvl5['code'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PMhurUdNQCJWEg4NOh48IGTB': 'file_storage/call_PMhurUdNQCJWEg4NOh48IGTB.json', 'var_call_ZHWjhcVBYlvE9tSg5nCuFoV9': 'file_storage/call_ZHWjhcVBYlvE9tSg5nCuFoV9.json'}

exec(code, env_args)

code = """import json, pandas as pd, re

# Load smaller chunks / optimize reading
with open(var_call_PMhurUdNQCJWEg4NOh48IGTB, 'r') as f:
    pubs = json.load(f)

# Limit to necessary columns and convert incrementally
month_abbr = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

import datetime as dt
month_pattern = r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}[a-z]{2},?\s+(\d{4})'

def get_year(s):
    if not isinstance(s,str) or not s.strip():
        return None
    m = re.search(month_pattern, s)
    if not m:
        m = re.search(r'(\d{4})', s)
        return int(m.group(1)) if m else None
    return int(m.group(2))

code_pattern = re.compile(r'[A-HY][0-9]{2}[A-Z][0-9]{0,4}/?[0-9]{0,4}')

def extract_codes(cpc_str):
    if not isinstance(cpc_str,str) or not cpc_str.strip():
        return []
    try:
        data = json.loads(cpc_str)
        return [d.get('code') for d in data if isinstance(d, dict) and d.get('code')]
    except Exception:
        return code_pattern.findall(cpc_str)

rows = []
for rec in pubs:
    y = get_year(rec.get('publication_date'))
    if not y:
        continue
    for code in extract_codes(rec.get('cpc')):
        rows.append({'year': y, 'code': code})

if not rows:
    result = []
else:
    codes_df = pd.DataFrame(rows)
    yearly_counts = codes_df.groupby(['code','year']).size().reset_index(name='count')

    alpha = 0.2
    ema_records = []
    for code, grp in yearly_counts.sort_values(['code','year']).groupby('code'):
        ema = None
        for _, row in grp.iterrows():
            c = row['count']
            ema = c if ema is None else alpha * c + (1-alpha) * ema
            ema_records.append({'code': code, 'year': int(row['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)
    idx = ema_df.groupby('code')['ema'].idxmax()
    best_df = ema_df.loc[idx]
    best_2022 = best_df[best_df['year'] == 2022]

    # load lvl5
    with open(var_call_ZHWjhcVBYlvE9tSg5nCuFoV9, 'r') as f:
        lvl5 = json.load(f)
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

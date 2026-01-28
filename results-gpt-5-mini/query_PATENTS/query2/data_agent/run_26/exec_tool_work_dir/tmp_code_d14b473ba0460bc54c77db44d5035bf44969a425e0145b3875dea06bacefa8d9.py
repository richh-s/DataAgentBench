code = """import json
import pandas as pd
import ast
import re

pub_file = var_call_kJb7YcVWqHK44RmcnteUMyXl
cpc_def_file = var_call_pYFOeyTt9cKRsHFZ0M19dyqi

with open(pub_file, 'r', encoding='utf-8') as f:
    pub = json.load(f)
with open(cpc_def_file, 'r', encoding='utf-8') as f:
    cpc_def = json.load(f)

df = pd.DataFrame(pub)

# parse year from grant_date

def parse_year(s):
    if not s or not isinstance(s, str):
        return None
    import re
    m = re.search(r'(19|20)\d{2}', s)
    if m:
        return int(m.group(0))
    return None

df['year'] = df['grant_date'].apply(parse_year)

# extract codes

def extract_codes(cpc_str):
    if not cpc_str or not isinstance(cpc_str, str):
        return []
    try:
        lst = ast.literal_eval(cpc_str)
        codes = [it.get('code') for it in lst if isinstance(it, dict) and it.get('code')]
        return codes
    except Exception:
        # fallback: find patterns like 'A61B' etc
        return re.findall(r'[A-Z]\d{2}[A-Z]?', cpc_str)

df['codes'] = df['cpc'].apply(extract_codes)

df_exp = df.explode('codes').dropna(subset=['codes'])

# filter Germany heuristics
df_exp = df_exp[df_exp['Patents_info'].str.contains('DE', na=False) | df_exp['Patents_info'].str.contains('Germany', na=False)]

# compute level4: first letter + two digits (e.g., G06)
def to_level4(code):
    if not isinstance(code, str):
        return None
    m = re.match(r'^([A-Z]\d{2})', code)
    if m:
        return m.group(1)
    return None

df_exp['level4'] = df_exp['codes'].apply(to_level4)

df_exp = df_exp.dropna(subset=['level4','year'])

# counts per level4 per year
counts = df_exp.groupby(['level4','year']).size().reset_index(name='count')

# compute EMA per group
results = []
for grp, gdf in counts.groupby('level4'):
    g = gdf.sort_values('year')
    ema = None
    years = []
    emas = []
    for _, row in g.iterrows():
        x = float(row['count'])
        if ema is None:
            ema = x
        else:
            ema = 0.1 * x + 0.9 * ema
        years.append(int(row['year']))
        emas.append(ema)
    if len(emas) > 0:
        idx = int(pd.Series(emas).idxmax())
        results.append({'level4': grp, 'best_year': years[idx], 'best_ema': emas[idx]})

res_df = pd.DataFrame(results)

# merge with cpc definitions
cpcdf = pd.DataFrame(cpc_def)
merged = res_df.merge(cpcdf, left_on='level4', right_on='symbol', how='left')

# sort and take top 10
merged_sorted = merged.sort_values('best_ema', ascending=False).head(10)

out = []
for _, r in merged_sorted.iterrows():
    out.append({
        'titleFull': r['titleFull'] if not pd.isna(r.get('titleFull')) else None,
        'cpc_group_level4': r['level4'],
        'best_year': int(r['best_year']),
        'best_ema': float(r['best_ema'])
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_7i6UBBTw7x6LfNL0cHrPd8Cp': 'file_storage/call_7i6UBBTw7x6LfNL0cHrPd8Cp.json', 'var_call_kJb7YcVWqHK44RmcnteUMyXl': 'file_storage/call_kJb7YcVWqHK44RmcnteUMyXl.json', 'var_call_pYFOeyTt9cKRsHFZ0M19dyqi': 'file_storage/call_pYFOeyTt9cKRsHFZ0M19dyqi.json'}

exec(code, env_args)

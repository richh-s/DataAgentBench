code = """import json
import pandas as pd

# Load the query results from storage
pub_file = var_call_kJb7YcVWqHK44RmcnteUMyXl
cpc_def_file = var_call_pYFOeyTt9cKRsHFZ0M19dyqi

with open(pub_file, 'r', encoding='utf-8') as f:
    pub = json.load(f)
with open(cpc_def_file, 'r', encoding='utf-8') as f:
    cpc_def = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(pub)
# Extract country code from Patents_info to ensure DE entries (already filtered but be safe)
# We'll normalize grant_date to extract year and month

def parse_month_year(s):
    # naive month extraction
    s = s or ''
    s = s.replace(',', ' ')
    parts = s.split()
    month = None
    year = None
    for p in parts:
        if p.strip().isdigit() and len(p.strip())==4:
            year = int(p.strip())
            break
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    for m in months:
        if m in s:
            month = m
            break
    return month, year

parsed = df['grant_date'].apply(parse_month_year)
DF = df.copy()
DF['month'] = parsed.apply(lambda x: x[0])
DF['year'] = parsed.apply(lambda x: x[1])

# Expand CPC JSON-like string into codes per row
import ast

def extract_codes(cpc_str):
    try:
        lst = ast.literal_eval(cpc_str)
        codes = []
        for item in lst:
            if isinstance(item, dict) and 'code' in item:
                codes.append(item['code'])
        return codes
    except Exception:
        return []

DF['codes'] = DF['cpc'].apply(extract_codes)
DF_exp = DF.explode('codes')
DF_exp = DF_exp.dropna(subset=['codes'])

# Filter DE by Patents_info heuristics
DF_exp = DF_exp[DF_exp['Patents_info'].str.contains('DE', na=False) | DF_exp['Patents_info'].str.contains('Germany', na=False)]

# Keep only level-4 CPC groups: take first 4 chars up to first letter+number? CPC group level 4 typically like 'A01B1/00' -> group is first 4? But examples show 'G06F21/31' level 4 means symbol like 'G06F'??
# We'll define level4 as the section+class+subclass? Commonly CPC level 4 is the subgroup code up to the slash and two digits: e.g., G06F21/31 is level 6; level 4 might be G06F? But user asked CPC group at level 4. In cpc_definition we have symbols like 'G06' for level 4 earlier. So extract first 3 chars? However cpc_definition symbols at level 4 are like 'G06'. We'll take first 3 characters of code (letters+2 digits) as level4 symbol.

import re

def to_level4(code):
    # extract leading letters then up to two digits
    m = re.match(r'^([A-Z]+\d{1,2})', code)
    if m:
        return m.group(1)
    return None

DF_exp['level4'] = DF_exp['codes'].apply(to_level4)
DF_exp = DF_exp.dropna(subset=['level4'])

# Now compute yearly counts per level4 for available years
counts = DF_exp.groupby(['level4','year']).size().reset_index(name='count')

# For each level4, compute EMA with smoothing factor 0.1 across years sorted ascending
results = []
for grp, gdf in counts.groupby('level4'):
    g = gdf.sort_values('year')
    ema = None
    years = []
    emas = []
    for _, row in g.iterrows():
        x = row['count']
        if ema is None:
            ema = x
        else:
            ema = 0.1 * x + 0.9 * ema
        years.append(int(row['year']))
        emas.append(ema)
    # pick best year for this group = year with highest EMA value
    if len(emas)>0:
        max_idx = int(pd.Series(emas).idxmax())
        best_year = years[max_idx]
        best_ema = emas[max_idx]
        results.append({'level4':grp,'best_year':best_year,'best_ema':best_ema})

res_df = pd.DataFrame(results)
# merge titleFull from cpc_def
cpcdf = pd.DataFrame(cpc_def)
# cpc_definition symbols are e.g., 'G06' etc. Make sure match
merged = res_df.merge(cpcdf, left_on='level4', right_on='symbol', how='left')

# Select top groups by best_ema descending
top = merged.sort_values('best_ema', ascending=False).head(20)

# Prepare output list of dicts: full title, level4 code, best year
out = []
for _, r in top.iterrows():
    out.append({'titleFull': r.get('titleFull') if not pd.isna(r.get('titleFull')) else None,
                'cpc_group_level4': r['level4'],
                'best_year': int(r['best_year']),
                'best_ema': float(r['best_ema'])})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_7i6UBBTw7x6LfNL0cHrPd8Cp': 'file_storage/call_7i6UBBTw7x6LfNL0cHrPd8Cp.json', 'var_call_kJb7YcVWqHK44RmcnteUMyXl': 'file_storage/call_kJb7YcVWqHK44RmcnteUMyXl.json', 'var_call_pYFOeyTt9cKRsHFZ0M19dyqi': 'file_storage/call_pYFOeyTt9cKRsHFZ0M19dyqi.json'}

exec(code, env_args)

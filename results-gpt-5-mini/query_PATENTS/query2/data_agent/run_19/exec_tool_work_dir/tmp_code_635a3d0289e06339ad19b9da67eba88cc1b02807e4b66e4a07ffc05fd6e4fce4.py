code = """import json
import pandas as pd

# Load publication records
pub_path = var_call_ovXijmq2dyliGcDJnVaM97Hm
with open(pub_path, 'r', encoding='utf-8') as f:
    pub_records = json.load(f)

# DataFrame
df = pd.DataFrame(pub_records)
# Filter Germany
mask_germany = df['Patents_info'].str.contains('GERMANY', case=False, na=False)
df = df[mask_germany].copy()

import re

def parse_date_to_year_month(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(19|20)\d{2}", s)
    if not m:
        return None
    year = int(m.group(0))
    month_map = { 'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12 }
    mo = None
    for k in month_map:
        if re.search(k, s, re.IGNORECASE):
            mo = month_map[k]
            break
    return (year, mo)

ym = df['grant_date'].apply(parse_date_to_year_month)
df['grant_year'] = ym.apply(lambda x: x[0] if x else None)
df['grant_month'] = ym.apply(lambda x: x[1] if x else None)

# Filter grants in second half of 2019
df = df[(df['grant_year']==2019) & (df['grant_month'].isin([7,8,9,10,11,12]))].copy()

# Extract CPC codes
import ast

def extract_codes(cpc_str):
    try:
        arr = ast.literal_eval(cpc_str)
        codes = [ item.get('code') for item in arr if isinstance(item, dict) and 'code' in item ]
        return codes
    except Exception:
        return []

df['cpc_codes'] = df['cpc'].apply(extract_codes)

# Explode
if df.empty:
    final = []
else:
    df_expl = df.explode('cpc_codes')
    df_expl = df_expl.dropna(subset=['cpc_codes'])

    # level4 extraction
    def level4_group(code):
        if not isinstance(code, str):
            return None
        m = re.match(r"^([A-HJ-Y]\d{2})", code)
        if m:
            return m.group(1)
        return None

    df_expl['cpc_level4'] = df_expl['cpc_codes'].apply(level4_group)
    df_expl = df_expl.dropna(subset=['cpc_level4'])

    # filing year
    def parse_filing_year(s):
        if not isinstance(s, str):
            return None
        m = re.search(r"(19|20)\d{2}", s)
        if not m:
            return None
        return int(m.group(0))

    df_expl['filing_year'] = df_expl['filing_date'].apply(parse_filing_year)
    df_expl = df_expl.dropna(subset=['filing_year']).copy()

    # groups
    groups = {}
    for g, grp in df_expl.groupby('cpc_level4'):
        counts = grp.groupby('filing_year').size().to_dict()
        groups[g] = counts

    alpha = 0.1
    result_rows = []
    for g, counts in groups.items():
        years = sorted(counts.keys())
        if not years:
            continue
        ema = None
        ema_by_year = {}
        for y in range(min(years), max(years)+1):
            val = counts.get(y, 0)
            if ema is None:
                ema = val
            else:
                ema = alpha * val + (1-alpha) * ema
            ema_by_year[y] = ema
        best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
        best_ema = ema_by_year[best_year]
        result_rows.append({'cpc_level4': g, 'best_year': int(best_year), 'best_ema': float(best_ema)})

    if not result_rows:
        final = []
    else:
        res_df = pd.DataFrame(result_rows)
        res_df = res_df.sort_values('best_ema', ascending=False).reset_index(drop=True)

        # load cpc defs
        cpc_def_path = var_call_hc0MJAZv42WfDBMyycgiB2Ft
        with open(cpc_def_path, 'r', encoding='utf-8') as f:
            cpc_defs = json.load(f)
        def_map = { item['symbol']: item['titleFull'] for item in cpc_defs }
        res_df['titleFull'] = res_df['cpc_level4'].map(def_map).fillna('')
        final = res_df[['titleFull','cpc_level4','best_year','best_ema']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_ovXijmq2dyliGcDJnVaM97Hm': 'file_storage/call_ovXijmq2dyliGcDJnVaM97Hm.json', 'var_call_hc0MJAZv42WfDBMyycgiB2Ft': 'file_storage/call_hc0MJAZv42WfDBMyycgiB2Ft.json'}

exec(code, env_args)

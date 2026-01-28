code = """import json
import pandas as pd

# Load the large publication results from storage
pub_path = var_call_ovXijmq2dyliGcDJnVaM97Hm
with open(pub_path, 'r', encoding='utf-8') as f:
    pub_records = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(pub_records)

# Extract country from Patents_info (look for 'GERMANY' or 'Germany')
# We'll filter records that mention 'GERMANY' case-insensitive
mask_germany = df['Patents_info'].str.contains('GERMANY', case=False, na=False)
df = df[mask_germany].copy()

# Parse grant_date into a year and month
import re

def parse_date_to_year_month(s):
    if not isinstance(s, str):
        return None
    # find year
    m = re.search(r"(19|20)\d{2}", s)
    if not m:
        return None
    year = int(m.group(0))
    # find month name
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

# Filter for grants in second half of 2019 (months 7-12 and year 2019)
df = df[(df['grant_year']==2019) & (df['grant_month'].isin([7,8,9,10,11,12]))].copy()

# Expand CPC codes: cpc field is a JSON-like string list of objects with 'code'
import ast

def extract_codes(cpc_str):
    try:
        # some strings have newlines, ensure safe eval
        arr = ast.literal_eval(cpc_str)
        codes = [ item.get('code') for item in arr if isinstance(item, dict) and 'code' in item ]
        return codes
    except Exception:
        return []

df['cpc_codes'] = df['cpc'].apply(extract_codes)

# Explode to one row per cpc code
df_expl = df.explode('cpc_codes')
df_expl = df_expl.dropna(subset=['cpc_codes'])

# We need CPC group at level 4: take first character(s) before first number? For CPC level 4, the symbol is like 'A61' maybe first letter+two digits?
# Observing cpc_definition symbols from the other query, level 4 symbols are two or three chars, e.g., 'A61', 'B01'. Typically section A..H + two digits -> e.g., A61 is level4.
# Extract the alpha + two digits prefix from code: take first letter and next two digits
import re

def level4_group(code):
    if not isinstance(code, str):
        return None
    m = re.match(r"^([A-HJ-Y]\d{2})", code)
    if m:
        return m.group(1)
    # sometimes codes like 'B99' exist, above covers it
    return None

df_expl['cpc_level4'] = df_expl['cpc_codes'].apply(level4_group)

df_expl = df_expl.dropna(subset=['cpc_level4'])

# Count filings per group per year - but we only have 2019 subset; the user wants EMA each year for patents granted in second half of 2019.
# That suggests we should look at filing_date years for those patents and compute annual counts over years, then EMA with smoothing 0.1.

# Parse filing_date year

def parse_filing_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(19|20)\d{2}", s)
    if not m:
        return None
    return int(m.group(0))

df_expl['filing_year'] = df_expl['filing_date'].apply(parse_filing_year)

# Keep records with filing_year
df_expl = df_expl.dropna(subset=['filing_year']).copy()

# For each level4 group, build a time series of yearly counts from min to max filing_year
groups = {}
for g, grp in df_expl.groupby('cpc_level4'):
    counts = grp.groupby('filing_year').size().to_dict()
    groups[g] = counts

# Compute EMA with smoothing factor alpha=0.1 for each group's yearly series, ordered by year.
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
    # find year with highest EMA
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    best_ema = ema_by_year[best_year]
    result_rows.append({'cpc_level4': g, 'best_year': int(best_year), 'best_ema': float(best_ema)})

# Convert to DataFrame and pick top groups by best_ema
res_df = pd.DataFrame(result_rows)
res_df = res_df.sort_values('best_ema', ascending=False).reset_index(drop=True)

# Load cpc definition titles to map
cpc_def_path = var_call_hc0MJAZv42WfDBMyycgiB2Ft
with open(cpc_def_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

def_map = { item['symbol']: item['titleFull'] for item in cpc_defs }

# Map titles
res_df['titleFull'] = res_df['cpc_level4'].map(def_map).fillna('')

# Prepare final output: include full title, CPC group code, and best year for each CPC group at level 4.
final = res_df[['titleFull','cpc_level4','best_year','best_ema']].head(20).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_ovXijmq2dyliGcDJnVaM97Hm': 'file_storage/call_ovXijmq2dyliGcDJnVaM97Hm.json', 'var_call_hc0MJAZv42WfDBMyycgiB2Ft': 'file_storage/call_hc0MJAZv42WfDBMyycgiB2Ft.json'}

exec(code, env_args)

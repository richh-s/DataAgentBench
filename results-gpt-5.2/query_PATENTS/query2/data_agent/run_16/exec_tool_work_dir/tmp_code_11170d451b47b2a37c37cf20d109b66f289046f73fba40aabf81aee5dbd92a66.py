code = """import json, re, pandas as pd

# load records
path_or_records = var_call_REZtQSLJ4pddSAbA4lK9qjo2
if isinstance(path_or_records, str):
    with open(path_or_records, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = path_or_records

df = pd.DataFrame(recs)

# filter to Germany using Patents_info: look for country_code DE patterns (avoid just any 'DE' in text)
pat = re.compile(r'country_code\s*[=:]\s*DE|"country_code"\s*:\s*"DE"')
df = df[df['Patents_info'].fillna('').apply(lambda x: bool(pat.search(x)))]

# parse grant_date: ensure second half 2019
months = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}

def parse_year_month(s):
    if not isinstance(s,str):
        return None
    s2 = s.lower()
    y = re.search(r'(19|20)\d{2}', s2)
    if not y:
        return None
    year = int(y.group(0))
    m = None
    for name,num in months.items():
        if name in s2:
            m = num
            break
    return (year,m)

df['grant_ym'] = df['grant_date'].apply(parse_year_month)
df = df[df['grant_ym'].notna()]
df['grant_year'] = df['grant_ym'].apply(lambda t: t[0])
df['grant_month'] = df['grant_ym'].apply(lambda t: t[1])
df = df[(df['grant_year']==2019) & (df['grant_month'].between(7,12))]

# parse filing year

def parse_year(s):
    if not isinstance(s,str):
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

df['filing_year'] = df['filing_date'].apply(parse_year)
df = df[df['filing_year'].notna()]

# extract CPC level-4 group: like A61M1/34 -> A61M1/34 ; A61M2230/30 -> A61M2230/30 (level 4 definition here treated as up to 2 digits after slash)
# We'll take part before '/' plus first two digits after '/'

def cpc_lvl4(code):
    if not isinstance(code,str) or '/' not in code:
        return None
    pre, post = code.split('/',1)
    digits = re.match(r'(\d+)', post)
    if not digits:
        return None
    d = digits.group(1)
    d2 = d[:2] if len(d)>=2 else d
    return f"{pre}/{d2}"

# explode CPC codes
rows = []
for _,r in df.iterrows():
    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if isinstance(cpc_raw,str) else []
    except Exception:
        cpcs = []
    for c in cpcs:
        code = c.get('code') if isinstance(c,dict) else None
        lv4 = cpc_lvl4(code)
        if lv4:
            rows.append({'cpc_lvl4': lv4, 'filing_year': int(r['filing_year'])})

cpc_df = pd.DataFrame(rows)
if cpc_df.empty:
    out = []
else:
    # count filings per year per cpc
    counts = cpc_df.groupby(['cpc_lvl4','filing_year']).size().reset_index(name='filings')

    # EMA per cpc
    alpha = 0.1
    best_rows = []
    for cpc, g in counts.groupby('cpc_lvl4'):
        g2 = g.sort_values('filing_year').copy()
        ema = None
        emas = []
        for _,rr in g2.iterrows():
            x = rr['filings']
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            emas.append(ema)
        g2['ema'] = emas
        # best year (max ema)
        idx = g2['ema'].idxmax()
        br = g2.loc[idx]
        best_rows.append({'cpc_lvl4': cpc, 'best_year': int(br['filing_year']), 'best_ema': float(br['ema'])})

    best = pd.DataFrame(best_rows).sort_values(['best_ema','cpc_lvl4'], ascending=[False,True]).reset_index(drop=True)
    out = best.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_278tllUhBmbhU1CP6qoUoP6u': ['publicationinfo'], 'var_call_1aXIyOhvAT7RlwM02XNW4gMy': ['cpc_definition'], 'var_call_Iv7yyJ6vthwGIOxl5W4CJaY6': [], 'var_call_REZtQSLJ4pddSAbA4lK9qjo2': 'file_storage/call_REZtQSLJ4pddSAbA4lK9qjo2.json'}

exec(code, env_args)

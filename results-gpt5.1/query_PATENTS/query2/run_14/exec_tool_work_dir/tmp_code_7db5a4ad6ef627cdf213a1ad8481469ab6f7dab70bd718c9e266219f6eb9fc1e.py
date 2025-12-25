code = """import json, re, pandas as pd

# Load full datasets from files
with open(var_call_1VaApRSL23Y1aZLw5zqAU4EA, 'r') as f:
    grants = json.load(f)
with open(var_call_CbKrFoISdF2o6J4EUSvSEPML, 'r') as f:
    cpc_defs = json.load(f)

# Filter to Germany using Patents_info country code "DE"
pattern = re.compile(r"\bDE\b")
filtered = [r for r in grants if pattern.search(r.get('Patents_info',''))]

# Parse grant year from grant_date (natural language); keep only successfully parsed
months = { 'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
           'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

def parse_year(date_str):
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', date_str)
    y = re.search(r'(19|20)\d{2}', date_str)
    if not m or not y:
        return None
    return int(y.group(0))

records = []
for r in filtered:
    y = parse_year(r.get('grant_date',''))
    if y is None:
        continue
    cpc_raw = r.get('cpc') or '[]'
    try:
        codes = json.loads(cpc_raw)
    except Exception:
        continue
    for c in codes:
        code = c.get('code')
        if not code:
            continue
        # derive level-4 group as first 3 characters (section+class) per provided defs examples
        group = code[:3]
        records.append({'year': y, 'group': group})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # count filings per group per year
    counts = df.groupby(['group','year']).size().reset_index(name='count')

    # compute EMA per group across years (sorted) with alpha=0.1
    alpha = 0.1
    ema_rows = []
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'group': g, 'year': int(row['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_rows)
    # for each group, find year with max EMA
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # attach titles from level-4 CPC definitions
    defs_df = pd.DataFrame(cpc_defs)
    defs_df['symbol'] = defs_df['symbol'].astype(str)
    best = best.merge(defs_df[['symbol','titleFull']], left_on='group', right_on='symbol', how='left')

    # sort by ema desc
    best = best.sort_values('ema', ascending=False)
    result = best.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1VaApRSL23Y1aZLw5zqAU4EA': 'file_storage/call_1VaApRSL23Y1aZLw5zqAU4EA.json', 'var_call_CbKrFoISdF2o6J4EUSvSEPML': 'file_storage/call_CbKrFoISdF2o6J4EUSvSEPML.json'}

exec(code, env_args)

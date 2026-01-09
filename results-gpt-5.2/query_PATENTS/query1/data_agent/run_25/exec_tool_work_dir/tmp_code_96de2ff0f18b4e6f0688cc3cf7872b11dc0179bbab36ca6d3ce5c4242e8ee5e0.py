code = """import json, re
import pandas as pd

# Load publications (may be file path)
pubs_src = var_call_REoDMUnOBgmbd5xwdRfOEhX1
if isinstance(pubs_src, str):
    with open(pubs_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pubs_src

lvl5_src = var_call_6yla0irl6VU6ENGs5R6p0oRQ
if isinstance(lvl5_src, str):
    with open(lvl5_src, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl5_src

lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol') is not None)

month_map = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
    'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for e in arr:
            c = e.get('code')
            if c:
                codes.append(c.strip())
        return codes
    except Exception:
        # fallback regex for codes like H01M10/0565
        return re.findall(r'"code"\\s*:\\s*"([A-Z]\\d{2}[A-Z]\\d+(?:/\\d+)?[A-Z0-9]*)"', cpc_str)

rows = []
for rec in pubs:
    y = parse_year(rec.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(rec.get('cpc'))
    if not codes:
        continue
    # unique codes per publication-year to avoid duplicates in same record
    for c in set(codes):
        # map to level-5 group code: take substring before '/' if present
        grp = c.split('/')[0]
        if grp in lvl5_set:
            rows.append((grp, y))

df = pd.DataFrame(rows, columns=['cpc5','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc5','year']).size().reset_index(name='filings')

    alpha = 0.2
    def compute_ema(sub):
        sub = sub.sort_values('year').copy()
        ema = []
        prev = None
        for v in sub['filings'].tolist():
            if prev is None:
                prev = float(v)
            else:
                prev = alpha*float(v) + (1-alpha)*prev
            ema.append(prev)
        sub['ema'] = ema
        return sub

    ema_df = counts.groupby('cpc5', group_keys=False).apply(compute_ema)

    # for each year, find max EMA across CPC5s
    year_max = ema_df.groupby('year')['ema'].transform('max')
    top_each_year = ema_df[ema_df['ema'] == year_max].copy()

    # Determine best year per CPC5 among these year-top entries? or overall best year per CPC5 by ema.
    # Requirement: "CPC technology areas with the highest EMA of patent filings each year" => consider top_each_year.
    # Then "return only the CPC group codes at level 5 whose best year is 2022." => best year for that CPC5 within full EMA series.
    best_year = ema_df.sort_values(['cpc5','ema','year'], ascending=[True,False,False]).groupby('cpc5').head(1)[['cpc5','year']]
    best_year_map = dict(zip(best_year['cpc5'], best_year['year']))

    filt = top_each_year[top_each_year['cpc5'].map(best_year_map).eq(2022)]
    out = sorted(filt['cpc5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_REoDMUnOBgmbd5xwdRfOEhX1': 'file_storage/call_REoDMUnOBgmbd5xwdRfOEhX1.json', 'var_call_6yla0irl6VU6ENGs5R6p0oRQ': 'file_storage/call_6yla0irl6VU6ENGs5R6p0oRQ.json'}

exec(code, env_args)

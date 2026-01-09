code = """import json, re
import pandas as pd

# Load publication records
src = var_call_V9Tm4BQIhOAAlJTSjZ37hB3k
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        pub_recs = json.load(f)
else:
    pub_recs = src

# Load level-5 CPC group symbols
src2 = var_call_2d5vo0wRSMfLhjD2cCXbxUD2
if isinstance(src2, str):
    with open(src2, 'r', encoding='utf-8') as f:
        lvl5_recs = json.load(f)
else:
    lvl5_recs = src2
lvl5_set = set(r['symbol'] for r in lvl5_recs if r.get('symbol') is not None)

# Helpers
month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if s is None:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if not m:
        return None
    y = int(m.group(1))
    return y

# Extract year and CPC codes, then map to level-5 group code
rows = []
code_re = re.compile(r'"code"\s*:\s*"([A-Z]\d\d[A-Z][0-9A-Z]*\s*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+|[A-Z]\d\d[A-Z][0-9A-Z]*\d*/\d+)"')

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    # Try JSON
    try:
        data = json.loads(cpc_str)
        codes = []
        for it in data:
            c = it.get('code')
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex
        return code_re.findall(cpc_str)

def to_lvl5(code):
    if not code:
        return None
    code = code.strip().replace(' ', '')
    # If exact symbol exists in level5 set, keep
    if code in lvl5_set:
        return code
    # For subgroup like H01M10/0565 -> group H01M10/00 (or H01M10/05? but level5 are main groups e.g., H01M)
    # Prefer mapping to 4-char subclass if that's level 5 in this dataset
    m = re.match(r'^([A-Z]\d\d[A-Z])', code)
    if m and m.group(1) in lvl5_set:
        return m.group(1)
    # else take first 4 anyway
    return None

for r in pub_recs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    lvl5_codes = set(filter(None, (to_lvl5(c) for c in codes)))
    for c in lvl5_codes:
        rows.append((c, y))

if not rows:
    out = []
else:
    df = pd.DataFrame(rows, columns=['cpc5','year'])
    counts = df.groupby(['cpc5','year']).size().reset_index(name='filings').sort_values(['cpc5','year'])

    alpha = 0.2
    # compute EMA per cpc5
    def ema_series(g):
        g = g.sort_values('year').copy()
        ema = []
        prev = None
        for v in g['filings'].tolist():
            if prev is None:
                prev = v
            else:
                prev = alpha*v + (1-alpha)*prev
            ema.append(prev)
        g['ema'] = ema
        return g

    counts2 = counts.groupby('cpc5', group_keys=False).apply(ema_series)
    # For each year, pick cpc5 with max ema
    idx = counts2.groupby('year')['ema'].idxmax()
    top_each_year = counts2.loc[idx, ['year','cpc5','ema']].sort_values('year')
    # For each cpc5, find its best year (max ema, tiebreak latest year)
    def best_year(g):
        max_ema = g['ema'].max()
        gy = g[g['ema']==max_ema]
        by = int(gy['year'].max())
        return pd.Series({'best_year': by, 'best_ema': float(max_ema)})
    best = counts2.groupby('cpc5').apply(best_year).reset_index()
    # Filter cpc5 that are top in some year and whose best_year is 2022
    top_codes = set(top_each_year['cpc5'].tolist())
    res = best[(best['cpc5'].isin(top_codes)) & (best['best_year']==2022)].sort_values(['best_ema','cpc5'], ascending=[False, True])
    out = res['cpc5'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_V9Tm4BQIhOAAlJTSjZ37hB3k': 'file_storage/call_V9Tm4BQIhOAAlJTSjZ37hB3k.json', 'var_call_2d5vo0wRSMfLhjD2cCXbxUD2': 'file_storage/call_2d5vo0wRSMfLhjD2cCXbxUD2.json'}

exec(code, env_args)

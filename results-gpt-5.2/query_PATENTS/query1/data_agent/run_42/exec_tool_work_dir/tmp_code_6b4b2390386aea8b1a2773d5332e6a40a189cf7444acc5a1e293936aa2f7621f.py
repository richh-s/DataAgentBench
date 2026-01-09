code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

lvl5_syms = load_records(var_call_SVhk7ZOTAtgMUmk2L5aZqiz8)
pubs = load_records(var_call_Sdqyp7jpkkxmm75o8kuarAYJ)

lvl5_set = set(r['symbol'] for r in lvl5_syms if r.get('symbol'))

# parse year from filing_date natural language
month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if not m:
        return None
    y = int(m.group(1))
    if y < 1800 or y > 2100:
        return None
    return y

def parse_cpc_codes(s):
    if not s:
        return []
    try:
        arr = json.loads(s)
        codes = []
        for obj in arr:
            c = obj.get('code')
            if c:
                codes.append(c)
        return codes
    except Exception:
        return []

rows = []
for r in pubs:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    # unique per publication-year to avoid duplicates within same record
    seen = set()
    for c in codes:
        grp = c.split('/')[0].strip()
        if grp in lvl5_set and grp not in seen:
            rows.append((grp, y))
            seen.add(grp)

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')
    # build full year range per symbol
    results = []
    alpha = 0.2
    for sym, g in counts.groupby('symbol'):
        g = g.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        g2 = pd.DataFrame({'year': years}).merge(g[['year','filings']], on='year', how='left').fillna({'filings':0})
        g2['filings'] = g2['filings'].astype(float)
        ema = []
        prev = None
        for v in g2['filings'].tolist():
            if prev is None:
                prev = v
            else:
                prev = alpha*v + (1-alpha)*prev
            ema.append(prev)
        g2['ema'] = ema
        # best year is max ema; choose latest year if tie
        max_ema = g2['ema'].max()
        best_year = int(g2.loc[g2['ema'].eq(max_ema), 'year'].max())
        results.append((sym, best_year, float(max_ema)))

    resdf = pd.DataFrame(results, columns=['symbol','best_year','best_ema'])
    out = resdf.loc[resdf['best_year'].eq(2022), 'symbol'].sort_values().tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SVhk7ZOTAtgMUmk2L5aZqiz8': 'file_storage/call_SVhk7ZOTAtgMUmk2L5aZqiz8.json', 'var_call_Sdqyp7jpkkxmm75o8kuarAYJ': 'file_storage/call_Sdqyp7jpkkxmm75o8kuarAYJ.json'}

exec(code, env_args)

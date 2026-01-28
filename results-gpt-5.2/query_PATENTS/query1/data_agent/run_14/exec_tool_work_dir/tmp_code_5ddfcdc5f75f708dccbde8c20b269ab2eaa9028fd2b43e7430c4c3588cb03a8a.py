code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pub = load_records(var_call_pk6guEq3XuZCaniRTAOoC7WL)
level5 = load_records(var_call_QpDBz58W8vIKhOnbKSTRrT1J)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol') is not None)

# Parse year from natural-language filing_date
month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if m:
        y = int(m.group(1))
        return y
    return None

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for d in data:
            c = d.get('code')
            if c:
                codes.append(c.strip())
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d\d[A-Z]\d+/?\d+)"', cpc_str)

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    # de-duplicate codes per patent-year record to avoid repeats within same publication
    for c in set(codes):
        # Keep only CPC group codes at level 5 (per definition table)
        # Remove spaces
        c2 = c.replace(' ', '')
        if c2 in level5_set:
            rows.append((c2, y))

df = pd.DataFrame(rows, columns=['cpc5','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc5','year']).size().rename('filings').reset_index()

    # ensure continuous years per cpc5
    all_years = sorted(counts['year'].unique().tolist())

    alpha = 0.2
    results = []
    for cpc5, g in counts.groupby('cpc5'):
        g2 = g.set_index('year').reindex(all_years, fill_value=0).sort_index()
        ema = None
        for y, val in g2['filings'].items():
            if ema is None:
                ema = float(val)
            else:
                ema = alpha*float(val) + (1-alpha)*ema
            results.append({'cpc5': cpc5, 'year': int(y), 'ema': float(ema)})

    ema_df = pd.DataFrame(results)

    # for each year, find CPC(s) with highest EMA
    max_by_year = ema_df.groupby('year')['ema'].max().reset_index().rename(columns={'ema':'max_ema'})
    top = ema_df.merge(max_by_year, on='year')
    top = top[top['ema'] == top['max_ema']][['cpc5','year','ema']]

    # Determine best year for each CPC among years where it is top
    best_year = top.sort_values(['cpc5','ema','year'], ascending=[True,False,False]).groupby('cpc5').head(1)
    best_year = best_year.rename(columns={'year':'best_year','ema':'best_year_ema'})

    # Filter those whose best year is 2022
    out = sorted(best_year[best_year['best_year']==2022]['cpc5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pk6guEq3XuZCaniRTAOoC7WL': 'file_storage/call_pk6guEq3XuZCaniRTAOoC7WL.json', 'var_call_QpDBz58W8vIKhOnbKSTRrT1J': 'file_storage/call_QpDBz58W8vIKhOnbKSTRrT1J.json'}

exec(code, env_args)

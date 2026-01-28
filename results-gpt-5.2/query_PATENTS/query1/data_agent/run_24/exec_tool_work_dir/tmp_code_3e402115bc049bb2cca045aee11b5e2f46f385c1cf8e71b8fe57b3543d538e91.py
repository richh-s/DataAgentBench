code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_records(var_call_ssFiRLvvyuc6sJOhgwCQOAxw)
level5 = load_records(var_call_bUSs1nIq2vuA8sltsZrnRQ9P)

level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

months = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if not m:
        return None
    return int(m.group(1))

codes_year_rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    cpc_str = r.get('cpc')
    if not cpc_str:
        continue
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        continue
    codes = []
    for e in cpcs:
        code = e.get('code') if isinstance(e, dict) else None
        if not code:
            continue
        code = code.strip()
        # Map to CPC group code at level 5: keep section+class+subclass (e.g., H01M) by taking leading letter+2 digits+letter
        m = re.match(r'^([A-HY]\d\d[A-Z])', code)
        if not m:
            continue
        grp = m.group(1)
        if grp in level5_set:
            codes.append(grp)
    if not codes:
        continue
    for grp in set(codes):
        codes_year_rows.append((grp, y))

df = pd.DataFrame(codes_year_rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().reset_index(name='filings')

    alpha = 0.2
    # compute EMA per symbol over sorted years, filling missing years with 0 between min and max
    res = []
    for sym, g in counts.groupby('symbol'):
        g = g.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        m = g.set_index('year')['filings'].to_dict()
        ema = None
        for yr in years:
            x = float(m.get(yr, 0))
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            res.append((sym, yr, ema))
    ema_df = pd.DataFrame(res, columns=['symbol','year','ema'])
    # find max ema per year
    idx = ema_df.groupby('year')['ema'].idxmax()
    top = ema_df.loc[idx, ['year','symbol','ema']].sort_values('year')
    # for each symbol, best year = year where it was top (could be multiple years); we only want those with best year 2022
    sym_best_year = top.sort_values(['symbol','ema','year']).groupby('symbol').apply(lambda x: x.loc[x['ema'].idxmax(),'year']).to_dict()
    selected = sorted([sym for sym, by in sym_best_year.items() if int(by)==2022])
    out = selected

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ssFiRLvvyuc6sJOhgwCQOAxw': 'file_storage/call_ssFiRLvvyuc6sJOhgwCQOAxw.json', 'var_call_bUSs1nIq2vuA8sltsZrnRQ9P': 'file_storage/call_bUSs1nIq2vuA8sltsZrnRQ9P.json'}

exec(code, env_args)

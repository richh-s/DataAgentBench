code = """import json, re
import pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_result(var_call_PxGIEMGTvld0CYNW8udzG0r5)
level5 = load_result(var_call_r5whG8IJGCywWPtiLPthQVQn)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

# parse year from natural language date
_year_re = re.compile(r'(19\d{2}|20\d{2})')

def parse_year(s):
    if not s:
        return None
    m = _year_re.search(s)
    return int(m.group(1)) if m else None

codes_year = []
for rec in pub:
    y = parse_year(rec.get('filing_date'))
    if y is None:
        continue
    cpc_raw = rec.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    for e in cpcs:
        code = e.get('code') or e.get('symbol')
        if not code:
            continue
        # keep only level-5 symbols exactly as in definition table
        if code in level5_set:
            codes_year.append((code, y))

if not codes_year:
    out = []
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df = pd.DataFrame(codes_year, columns=['symbol','year'])
counts = df.groupby(['symbol','year']).size().reset_index(name='filings')

# build full year range per symbol
all_years = pd.DataFrame({'year': range(int(counts['year'].min()), int(counts['year'].max())+1)})

alpha = 0.2
rows = []
for sym, g in counts.groupby('symbol'):
    g2 = all_years.merge(g, on='year', how='left').fillna({'filings':0})
    g2 = g2.sort_values('year')
    ema = None
    for yr, val in zip(g2['year'].tolist(), g2['filings'].tolist()):
        if ema is None:
            ema = val
        else:
            ema = alpha*val + (1-alpha)*ema
        rows.append((sym, int(yr), float(ema)))

ema_df = pd.DataFrame(rows, columns=['symbol','year','ema'])

# for each year, select symbol(s) with max ema
max_by_year = ema_df.groupby('year')['ema'].max().reset_index(name='max_ema')
leaders = ema_df.merge(max_by_year, on='year')
leaders = leaders[leaders['ema'] == leaders['max_ema']]

# for each symbol, determine best year (year of max ema; tie -> latest year)
best = (ema_df.sort_values(['symbol','ema','year'], ascending=[True, False, False])
        .groupby('symbol').head(1)[['symbol','year','ema']]
        .rename(columns={'year':'best_year','ema':'best_ema'}))

leaders = leaders.merge(best, on='symbol', how='left')
res = sorted(leaders[leaders['best_year']==2022]['symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_PxGIEMGTvld0CYNW8udzG0r5': 'file_storage/call_PxGIEMGTvld0CYNW8udzG0r5.json', 'var_call_r5whG8IJGCywWPtiLPthQVQn': 'file_storage/call_r5whG8IJGCywWPtiLPthQVQn.json'}

exec(code, env_args)

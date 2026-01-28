code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_recs = load_records(var_call_rfpq5tB8QV0GCZiQFRIMX1Yi)
level5_recs = load_records(var_call_qsQQkX4VfFmAOgwgtcs7OH3k)

level5_set = set(r['symbol'] for r in level5_recs if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group()) if m else None

def extract_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        data = json.loads(cpc_field)
        codes = []
        for e in data if isinstance(data, list) else []:
            code = e.get('code') if isinstance(e, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        return []

def to_level5_group(code):
    # Convert detailed CPC code like H01M10/0565 to group code H01M
    code = code.strip()
    m = re.match(r'^([A-HY]\d{2}[A-Z])', code)
    return m.group(1) if m else None

rows = []
for r in pub_recs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    groups = set()
    for c in codes:
        g = to_level5_group(c)
        if g and g in level5_set:
            groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['group','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['group','year']).reset_index(name='n')
    years = sorted(counts['year'].unique().tolist())
    alpha = 0.2
    # ensure full grid per group-year with 0s
    all_groups = counts['group'].unique()
    grid = pd.MultiIndex.from_product([all_groups, years], names=['group','year']).to_frame(index=False)
    grid = grid.merge(counts, on=['group','year'], how='left').fillna({'n':0})
    grid['n'] = grid['n'].astype(float)
    grid = grid.sort_values(['group','year'])

    def ema_series(x):
        ema = None
        out_ema = []
        for v in x['n'].tolist():
            ema = v if ema is None else alpha*v + (1-alpha)*ema
            out_ema.append(ema)
        return pd.Series(out_ema, index=x.index)

    grid['ema'] = grid.groupby('group', group_keys=False).apply(ema_series)

    # for each year, find group(s) with max ema
    max_by_year = grid.groupby('year')['ema'].transform('max')
    winners = grid[grid['ema'] == max_by_year][['year','group','ema']]

    # for each group, find best year (max ema; tie -> latest year)
    grp = grid.groupby('group')
    best_ema = grp['ema'].max().rename('best_ema')
    tmp = grid.merge(best_ema, on='group')
    tmp = tmp[tmp['ema'] == tmp['best_ema']]
    best_year = tmp.groupby('group')['year'].max().rename('best_year')

    winners = winners.merge(best_year, on='group', how='left')
    winners_2022 = winners[winners['best_year'] == 2022]

    out = sorted(winners_2022['group'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rfpq5tB8QV0GCZiQFRIMX1Yi': 'file_storage/call_rfpq5tB8QV0GCZiQFRIMX1Yi.json', 'var_call_qsQQkX4VfFmAOgwgtcs7OH3k': 'file_storage/call_qsQQkX4VfFmAOgwgtcs7OH3k.json'}

exec(code, env_args)

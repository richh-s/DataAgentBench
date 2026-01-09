code = """import json, re
import pandas as pd

# load filings
filings_src = var_call_uAQ6ZoBz4s41YQvEsOZjNThJ
if isinstance(filings_src, str):
    with open(filings_src, 'r') as f:
        filings = json.load(f)
else:
    filings = filings_src

lvl5_src = var_call_vn0yGVmc8wVw53FlxNspFaX0
if isinstance(lvl5_src, str):
    with open(lvl5_src, 'r') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl5_src

lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol'))

# parse year from filing_date
month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = [d.get('code') for d in data if isinstance(d, dict) and d.get('code')]
    except Exception:
        codes = re.findall(r'"code"\\s*:\\s*"([A-Z0-9/]+)"', cpc_str)
    # map to level-5 group code = first 4 chars before any '/' e.g. H01M10/0565 -> H01M
    out = []
    for c in codes:
        if not isinstance(c, str):
            continue
        m = re.match(r'^([A-HY][0-9]{2}[A-Z])', c.strip())
        if m:
            out.append(m.group(1))
    return out

rows=[]
for r in filings:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    for g in extract_codes(r.get('cpc')):
        if g in lvl5_set:
            rows.append((g,y))

df = pd.DataFrame(rows, columns=['group','year'])
if df.empty:
    res = []
else:
    counts = df.value_counts().reset_index(name='n').sort_values(['group','year'])

    # compute EMA per group
    alpha = 0.2
    ema_records = []
    for g, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            n = float(row['n'])
            if ema is None:
                ema = n
            else:
                ema = alpha*n + (1-alpha)*ema
            ema_records.append({'group': g, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)

    # for each year pick group(s) with max ema
    max_per_year = ema_df.groupby('year')['ema'].max().reset_index().rename(columns={'ema':'max_ema'})
    top = ema_df.merge(max_per_year, on='year')
    top = top[top['ema'] == top['max_ema']]

    # for each group, determine best year (max ema), tie -> latest year
    gbest = (ema_df.sort_values(['group','ema','year'])
                .groupby('group', as_index=False)
                .apply(lambda x: x.loc[x['ema'].max()==x['ema']].sort_values('year').tail(1))
            )
    # groupby apply creates multiindex
    if isinstance(gbest.index, pd.MultiIndex):
        gbest = gbest.reset_index(drop=True)

    groups_best_2022 = set(gbest[gbest['year']==2022]['group'])

    # return only CPC group codes at level 5 whose best year is 2022 and that are top in any year (highest ema of that year)
    final_groups = sorted(set(top['group']).intersection(groups_best_2022))
    res = final_groups

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_uAQ6ZoBz4s41YQvEsOZjNThJ': 'file_storage/call_uAQ6ZoBz4s41YQvEsOZjNThJ.json', 'var_call_vn0yGVmc8wVw53FlxNspFaX0': 'file_storage/call_vn0yGVmc8wVw53FlxNspFaX0.json'}

exec(code, env_args)

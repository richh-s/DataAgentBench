code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_N89X80Dkn41wxX3heJ4wnmr1)
level5 = load_records(var_call_J3Ie3sBZzhK9i9ukWoVGUZ5z)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if s is None:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for e in data:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback: regex like H01M10/0565
        return re.findall(r'[A-HY]\d{2}[A-Z]\d+(?:/\d+)?', cpc_str)

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    # unique per publication per year to avoid duplicates within same cpc list
    seen = set()
    for c in codes:
        grp = re.match(r'^([A-HY]\d{2}[A-Z])', c)
        if not grp:
            continue
        g = grp.group(1)
        if g in level5_set and g not in seen:
            rows.append((g, y))
            seen.add(g)

df = pd.DataFrame(rows, columns=['group','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['group','year']).size().reset_index(name='n')
    years_sorted = sorted(counts['year'].unique())
    alpha = 0.2
    # build complete panel per group-year with zeros
    all_groups = counts['group'].unique()
    panel = pd.MultiIndex.from_product([all_groups, years_sorted], names=['group','year']).to_frame(index=False)
    panel = panel.merge(counts, on=['group','year'], how='left').fillna({'n':0})
    panel = panel.sort_values(['group','year'])
    # compute EMA per group
    ema_list = []
    for g, sub in panel.groupby('group', sort=False):
        ema = None
        for _, rr in sub.iterrows():
            x = float(rr['n'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            ema_list.append((g, int(rr['year']), float(ema)))
    ema_df = pd.DataFrame(ema_list, columns=['group','year','ema'])
    # per year, take max ema and keep all ties
    max_per_year = ema_df.groupby('year')['ema'].max().reset_index().rename(columns={'ema':'max_ema'})
    top = ema_df.merge(max_per_year, on='year')
    top = top[top['ema'] == top['max_ema']]
    # best year per group among years where it is top
    best = top.sort_values(['group','year','ema']).groupby('group').tail(1)
    # filter best year == 2022
    res = sorted(best[best['year']==2022]['group'].unique().tolist())
    out = res

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_N89X80Dkn41wxX3heJ4wnmr1': 'file_storage/call_N89X80Dkn41wxX3heJ4wnmr1.json', 'var_call_J3Ie3sBZzhK9i9ukWoVGUZ5z': 'file_storage/call_J3Ie3sBZzhK9i9ukWoVGUZ5z.json'}

exec(code, env_args)

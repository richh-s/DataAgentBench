code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_e0m5EUNZNQENNHffZKoIW2J9)
level5 = load_records(var_call_JaJuwyjWPAlJBIBJ0jbzvdx0)

level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

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
        for it in arr:
            c = it.get('code')
            if c:
                codes.append(c.strip())
        return codes
    except Exception:
        # fallback regex for codes like H01M10/0565
        return re.findall(r'"code"\s*:\s*"([A-Z]\\d{2}[A-Z]\\d+(?:/\\d+)?)"', cpc_str)

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    for code in codes:
        grp = code.split('/')[0]
        if grp in level5_set:
            rows.append((grp, y))

df = pd.DataFrame(rows, columns=['cpc5','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc5','year']).size().reset_index(name='n')
    # ensure continuous yearly index per cpc5
    res = []
    alpha = 0.2
    for cpc5, g in counts.groupby('cpc5'):
        g = g.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        gm = g.set_index('year')['n'].to_dict()
        ema = None
        for yr in years:
            x = float(gm.get(yr, 0))
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            res.append((cpc5, yr, ema))
    ema_df = pd.DataFrame(res, columns=['cpc5','year','ema'])
    # identify highest EMA technology areas each year (global maxima)
    # handle ties
    max_by_year = ema_df.groupby('year')['ema'].max().reset_index().rename(columns={'ema':'max_ema'})
    top = ema_df.merge(max_by_year, on='year')
    top = top[top['ema'] == top['max_ema']]
    # for each cpc5, compute best year (year of max ema for that cpc5). pick earliest? but need best year == 2022; ties include 2022
    best = ema_df.groupby('cpc5')['ema'].max().reset_index().rename(columns={'ema':'best_ema'})
    ema_df2 = ema_df.merge(best, on='cpc5')
    best_years = ema_df2[ema_df2['ema'] == ema_df2['best_ema']].groupby('cpc5')['year'].apply(lambda s: sorted(set(map(int,s)))).reset_index(name='best_years')
    # filter to cpc5 whose best_years includes 2022
    cpc_best2022 = set(best_years[best_years['best_years'].apply(lambda ys: 2022 in ys)]['cpc5'])
    # now keep only those cpc5 that are among top-by-year for some year AND have best year 2022
    top_filt = top[top['cpc5'].isin(cpc_best2022)]
    out = sorted(top_filt['cpc5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_e0m5EUNZNQENNHffZKoIW2J9': 'file_storage/call_e0m5EUNZNQENNHffZKoIW2J9.json', 'var_call_JaJuwyjWPAlJBIBJ0jbzvdx0': 'file_storage/call_JaJuwyjWPAlJBIBJ0jbzvdx0.json'}

exec(code, env_args)

code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

pub_recs = load_records(var_call_KKoNnOzinbnsJH3OlaSrUO18)
lvl5_recs = load_records(var_call_hMCvvoPoQB2hWmn7anHSQdLw)
lvl5_set = set(r['symbol'] for r in lvl5_recs if r.get('symbol'))

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def parse_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        out = []
        for it in arr:
            if isinstance(it, dict) and it.get('code'):
                out.append(it['code'].strip())
        return out
    except Exception:
        return []

def to_level5(code):
    if code in lvl5_set:
        return code
    code2 = code.split()[0]
    if code2 in lvl5_set:
        return code2
    if '/' in code2:
        pref = code2.split('/')[0]
        if pref in lvl5_set:
            return pref
    return None

rows=[]
for r in pub_recs:
    y=extract_year(r.get('filing_date'))
    if y is None or y>2022:
        continue
    codes=set()
    for c in parse_cpc_codes(r.get('cpc')):
        l5=to_level5(c)
        if l5:
            codes.add(l5)
    for l5 in codes:
        rows.append((y,l5))

df=pd.DataFrame(rows, columns=['year','cpc5'])

if df.empty:
    out=[]
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

counts = df.groupby(['cpc5','year']).size().reset_index(name='n')
min_year = int(counts['year'].min())
all_years = list(range(min_year, 2023))
alpha=0.2
best_codes=set()

for cpc5, g in counts.groupby('cpc5'):
    s = pd.Series(0.0, index=all_years)
    s.update(g.set_index('year')['n'].astype(float))
    ema=None
    ema_vals={}
    for yr in all_years:
        x=float(s.loc[yr])
        if ema is None:
            ema=x
        else:
            ema=alpha*x + (1-alpha)*ema
        ema_vals[yr]=ema
    max_ema=max(ema_vals.values())
    # use tolerance for float equality
    best_years=[yr for yr,val in ema_vals.items() if abs(val-max_ema) < 1e-12]
    if 2022 in best_years:
        best_codes.add(cpc5)

out = sorted(best_codes)
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DbA0rd8zrZGceBlUvzJcbE5k': [], 'var_call_KKoNnOzinbnsJH3OlaSrUO18': 'file_storage/call_KKoNnOzinbnsJH3OlaSrUO18.json', 'var_call_f0W5m5mG59McgcrmAroP0Dfj': {'need_more_data': True, 'message': 'Need CPC level=5 symbol list (status filter returned none). Please query cpc_definition where level=5 (no status filter).'}, 'var_call_hMCvvoPoQB2hWmn7anHSQdLw': 'file_storage/call_hMCvvoPoQB2hWmn7anHSQdLw.json'}

exec(code, env_args)

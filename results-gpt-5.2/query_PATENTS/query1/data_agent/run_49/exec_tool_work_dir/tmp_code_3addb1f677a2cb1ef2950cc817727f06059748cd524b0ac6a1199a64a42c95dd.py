code = """import json, re
import pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

pubrecs = load_records(var_call_RzuM4DwHxy42gVurFA0eankc)
level5recs = load_records(var_call_CVotZ2CsIyQ94nwwhBDWQ4KO)

level5_symbols = set(r['symbol'] for r in level5recs if r.get('symbol') is not None)

month_map = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
    'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

def parse_year(s):
    if s is None:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    return int(m.group(1)) if m else None

def extract_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        obj = json.loads(cpc_field)
        codes = []
        if isinstance(obj, list):
            for it in obj:
                if isinstance(it, dict) and 'code' in it and it['code']:
                    codes.append(it['code'])
        return codes
    except Exception:
        # fallback: regex codes like A01B1/00 or H01M10/0525 etc
        return re.findall(r'([A-HY]\d{2}[A-Z]\d+(?:/\d+)?(?:\d+)?)', cpc_field)

def level5_group(code):
    if code is None:
        return None
    return code.strip().split('/')[0]

rows = []
for r in pubrecs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    groups = set()
    for c in codes:
        g = level5_group(c)
        if g in level5_symbols:
            groups.add(g)
    for g in groups:
        rows.append({'year': y, 'group': g})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    counts = df.groupby(['group','year']).size().reset_index(name='filings')
    # ensure full year grid per group
    years = sorted(counts['year'].unique().tolist())
    alpha = 0.2
    res_rows = []
    for g, sub in counts.groupby('group'):
        s = sub.set_index('year')['filings']
        # fill missing years with 0
        s = s.reindex(years, fill_value=0).sort_index()
        ema = None
        for yr, val in s.items():
            ema = val if ema is None else alpha*val + (1-alpha)*ema
            res_rows.append({'group': g, 'year': int(yr), 'ema': float(ema)})
    ema_df = pd.DataFrame(res_rows)
    # per year max ema across groups
    idx = ema_df.groupby('year')['ema'].transform('max') == ema_df['ema']
    winners = ema_df[idx].copy()
    # for each group, its best year (max ema), choose latest if tie
    gbest = winners.sort_values(['group','ema','year']).groupby('group').tail(1)
    out = sorted(gbest.loc[gbest['year']==2022, 'group'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_RzuM4DwHxy42gVurFA0eankc': 'file_storage/call_RzuM4DwHxy42gVurFA0eankc.json', 'var_call_CVotZ2CsIyQ94nwwhBDWQ4KO': 'file_storage/call_CVotZ2CsIyQ94nwwhBDWQ4KO.json'}

exec(code, env_args)

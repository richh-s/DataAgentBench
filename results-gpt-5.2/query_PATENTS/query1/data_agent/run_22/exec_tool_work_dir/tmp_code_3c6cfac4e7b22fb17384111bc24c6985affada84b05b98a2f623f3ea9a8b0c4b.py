code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_zEMksPEfsocekt29Z0w7903d)
lev5 = load_records(var_call_b2RvAMpUOdYCegc9PfXE9GV2)

lev5_syms = set([r['symbol'] for r in lev5 if r.get('symbol')])

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def extract_codes(cpc_str):
    if not cpc_str: return []
    # find all occurrences of "code": "..."
    codes = re.findall(r'"code"\\s*:\\s*"([A-Z]\d{2}[A-Z]\d*[A-Z]?[^"\\s]*)"', cpc_str)
    out = []
    for c in codes:
        c = c.strip()
        # level5 in this dataset appears as section+class+subclass, e.g., H01M
        prefix = c[:4]
        if prefix in lev5_syms:
            out.append(prefix)
    return list(set(out))

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None: 
        continue
    codes = extract_codes(r.get('cpc'))
    for code in codes:
        rows.append((y, code))

df = pd.DataFrame(rows, columns=['year','cpc5'])
if df.empty:
    res = []
else:
    counts = df.groupby(['cpc5','year']).size().reset_index(name='filings')
    # compute EMA per cpc5 over years
    alpha = 0.2
    ema_records = []
    for cpc5, g in counts.groupby('cpc5'):
        g2 = g.sort_values('year')
        ema = None
        for _, row in g2.iterrows():
            x = float(row['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            ema_records.append({'cpc5': cpc5, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    # for each year, find cpc5 with max ema (ties keep all)
    year_max = ema_df.groupby('year')['ema'].max().reset_index().rename(columns={'ema':'max_ema'})
    top = ema_df.merge(year_max, on='year')
    top = top[top['ema'] == top['max_ema']]
    # best year per cpc5 (max ema across years)
    best = ema_df.sort_values(['cpc5','ema','year'], ascending=[True, False, False]).groupby('cpc5').head(1)
    best = best.rename(columns={'year':'best_year','ema':'best_ema'})[['cpc5','best_year','best_ema']]
    # filter those whose best year is 2022
    winners_2022 = set(best[best['best_year']==2022]['cpc5'])
    # from per-year top list, keep cpc5 in winners_2022 AND year=2022? question: "return only the CPC group codes at level 5 whose best year is 2022" and "Identify the CPC technology areas with the highest EMA of patent filings each year".
    # So output those yearly winners whose own best year is 2022.
    top_filt = top[top['cpc5'].isin(winners_2022)].copy()
    res = sorted(top_filt['cpc5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_zEMksPEfsocekt29Z0w7903d': 'file_storage/call_zEMksPEfsocekt29Z0w7903d.json', 'var_call_b2RvAMpUOdYCegc9PfXE9GV2': 'file_storage/call_b2RvAMpUOdYCegc9PfXE9GV2.json'}

exec(code, env_args)

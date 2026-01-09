code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_records(var_call_PnUXNk9bQZ8BMQQALEjgpVMh)
level5 = load_records(var_call_1a6ONDKkpgScur6RRo5ybUeJ)
level5_set = set(r.get('symbol') for r in level5 if r.get('symbol'))

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', str(s))
    return int(m.group(1)) if m else None

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
    except Exception:
        try:
            data = json.loads(str(cpc_str).replace("'", '"'))
        except Exception:
            return []
    codes = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and item.get('code'):
                codes.append(item['code'].strip())
    return codes

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    for c in extract_codes(r.get('cpc')):
        if c in level5_set:
            rows.append((c, y))

df = pd.DataFrame(rows, columns=['cpc','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['cpc','year']).reset_index(name='filings')
    all_years = sorted(counts['year'].unique())
    grid = pd.MultiIndex.from_product([counts['cpc'].unique(), all_years], names=['cpc','year']).to_frame(index=False)
    full = grid.merge(counts, on=['cpc','year'], how='left').fillna({'filings':0})
    full['filings'] = full['filings'].astype(float)
    full = full.sort_values(['cpc','year'])
    alpha = 0.2
    def ema(s):
        prev = None
        out_s = []
        for x in s.tolist():
            prev = x if prev is None else (alpha*x + (1-alpha)*prev)
            out_s.append(prev)
        return pd.Series(out_s, index=s.index)
    full['ema'] = full.groupby('cpc', group_keys=False)['filings'].apply(ema)
    year_max = full.groupby('year')['ema'].transform('max')
    winners = full[full['ema'] == year_max][['year','cpc','ema']]
    tmp = full.copy()
    tmp['max_ema'] = tmp.groupby('cpc')['ema'].transform('max')
    best = tmp[tmp['ema'] == tmp['max_ema']]
    best_year = best.groupby('cpc')['year'].max().reset_index(name='best_year')
    winners = winners.merge(best_year, on='cpc', how='left')
    out = sorted(winners[winners['best_year'] == 2022]['cpc'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PnUXNk9bQZ8BMQQALEjgpVMh': 'file_storage/call_PnUXNk9bQZ8BMQQALEjgpVMh.json', 'var_call_1a6ONDKkpgScur6RRo5ybUeJ': 'file_storage/call_1a6ONDKkpgScur6RRo5ybUeJ.json'}

exec(code, env_args)

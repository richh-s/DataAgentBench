code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str):
        # file path
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_records(var_call_PnUXNk9bQZ8BMQQALEjgpVMh)
level5 = load_records(var_call_1a6ONDKkpgScur6RRo5ybUeJ)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {
 'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
 'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if not m: return None
    y = int(m.group(1))
    return y

def extract_codes(cpc_str):
    if not cpc_str: return []
    try:
        data = json.loads(cpc_str)
    except Exception:
        # try to salvage common issues
        try:
            data = json.loads(cpc_str.replace("'","\""))
        except Exception:
            return []
    codes=[]
    for item in data:
        c = item.get('code') if isinstance(item, dict) else None
        if c:
            codes.append(c.strip())
    return codes

rows=[]
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None: 
        continue
    codes = extract_codes(r.get('cpc'))
    for c in codes:
        if c in level5_set:
            rows.append((c,y))

df = pd.DataFrame(rows, columns=['cpc','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['cpc','year']).reset_index(name='filings')
    # complete years per cpc (fill missing with 0)
    all_years = sorted(counts['year'].unique())
    # build full grid
    grid = pd.MultiIndex.from_product([counts['cpc'].unique(), all_years], names=['cpc','year']).to_frame(index=False)
    full = grid.merge(counts, on=['cpc','year'], how='left').fillna({'filings':0})
    full['filings'] = full['filings'].astype(float)
    full = full.sort_values(['cpc','year'])
    alpha = 0.2
    # compute EMA per cpc
    def ema(series):
        e=[]
        prev=None
        for x in series:
            prev = x if prev is None else (alpha*x + (1-alpha)*prev)
            e.append(prev)
        return pd.Series(e, index=series.index)
    full['ema'] = full.groupby('cpc', group_keys=False)['filings'].apply(ema)
    # for each year, find cpc(s) with highest ema
    year_max = full.groupby('year')['ema'].transform('max')
    winners = full[full['ema'] == year_max][['year','cpc','ema']]
    # for each cpc, determine best year (max ema, tie -> latest year)
    tmp = full.copy()
    tmp['max_ema'] = tmp.groupby('cpc')['ema'].transform('max')
    best = tmp[tmp['ema']==tmp['max_ema']].sort_values(['cpc','year'])
    # pick latest year among ties
    best_year = best.groupby('cpc')['year'].max().reset_index(name='best_year')
    winners = winners.merge(best_year, on='cpc', how='left')
    out = sorted(winners[winners['best_year']==2022]['cpc'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PnUXNk9bQZ8BMQQALEjgpVMh': 'file_storage/call_PnUXNk9bQZ8BMQQALEjgpVMh.json', 'var_call_1a6ONDKkpgScur6RRo5ybUeJ': 'file_storage/call_1a6ONDKkpgScur6RRo5ybUeJ.json'}

exec(code, env_args)

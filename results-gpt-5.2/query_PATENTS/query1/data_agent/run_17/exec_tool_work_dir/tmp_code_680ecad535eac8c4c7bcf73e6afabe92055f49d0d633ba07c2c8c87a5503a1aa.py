code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

lvl5 = load_records(var_call_AwLO669IOtivdB8LkTQ1bCbi)
recs = load_records(var_call_6P5Ozy12vsScsxeuRvkMv3xX)

lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol'))

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def extract_codes(cpc_str):
    if not cpc_str: return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for it in data:
            c = it.get('code') if isinstance(it, dict) else None
            if c: codes.append(c)
        return codes
    except Exception:
        # fallback: regex for CPC-like codes
        return re.findall(r'([A-HY]\d{2}[A-Z]\d*\s*\d+/\d+)', cpc_str.replace(' ', ''))

rows = []
for r in recs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count each publication once per CPC level-5 group (truncate to 4 chars like 'H01M')
    groups = set()
    for c in codes:
        g = re.sub(r'\s+', '', c)[:4]
        if g in lvl5_set:
            groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')
    # build EMA per symbol over years
    alpha = 0.2
    res = []
    for sym, g in counts.groupby('symbol'):
        g2 = g.sort_values('year')
        ema = None
        for _, row in g2.iterrows():
            x = float(row['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            res.append({'symbol': sym, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(res)
    # for each year, find max EMA and symbols achieving it
    max_by_year = ema_df.groupby('year')['ema'].max().reset_index().rename(columns={'ema':'max_ema'})
    top = ema_df.merge(max_by_year, on='year')
    top = top[top['ema'] == top['max_ema']]
    # best year per symbol (max EMA; if tie pick latest year)
    tmp = ema_df.sort_values(['symbol','ema','year'], ascending=[True, False, False])
    best = tmp.groupby('symbol').head(1)[['symbol','year']].rename(columns={'year':'best_year'})
    top = top.merge(best, on='symbol', how='left')
    out = sorted(top[top['best_year']==2022]['symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AwLO669IOtivdB8LkTQ1bCbi': 'file_storage/call_AwLO669IOtivdB8LkTQ1bCbi.json', 'var_call_6P5Ozy12vsScsxeuRvkMv3xX': 'file_storage/call_6P5Ozy12vsScsxeuRvkMv3xX.json'}

exec(code, env_args)

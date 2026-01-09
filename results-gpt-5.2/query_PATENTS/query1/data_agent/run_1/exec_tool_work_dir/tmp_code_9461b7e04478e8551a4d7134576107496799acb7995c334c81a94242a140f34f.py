code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_records(var_call_xj4K9GwT0nZ5bpQ5nHao6DGK)
level5 = load_records(var_call_tIz7weJkqBAM5CMkBfv9WTzb)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    return int(m.group(1)) if m else None

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for e in arr if isinstance(arr, list) else []:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c.strip())
        return codes
    except Exception:
        # fall back regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d?.*?)"', cpc_str)

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    for c in codes:
        grp = c.split('/')[0]
        if grp in level5_set:
            rows.append((grp, y))

df = pd.DataFrame(rows, columns=['cpc5','year'])
# count filings per year per cpc5
counts = df.groupby(['cpc5','year']).size().rename('count').reset_index()

alpha = 0.2

def ema_for_group(g):
    g = g.sort_values('year')
    ema = None
    emas = []
    for _, row in g.iterrows():
        x = float(row['count'])
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        emas.append(ema)
    g = g.copy()
    g['ema'] = emas
    return g

emas = counts.groupby('cpc5', group_keys=False).apply(ema_for_group)
# best year per cpc5 (max ema); break ties by latest year
emas_sorted = emas.sort_values(['cpc5','ema','year'], ascending=[True, False, False])
best = emas_sorted.groupby('cpc5').head(1)
res = sorted(best.loc[best['year']==2022, 'cpc5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_xj4K9GwT0nZ5bpQ5nHao6DGK': 'file_storage/call_xj4K9GwT0nZ5bpQ5nHao6DGK.json', 'var_call_tIz7weJkqBAM5CMkBfv9WTzb': 'file_storage/call_tIz7weJkqBAM5CMkBfv9WTzb.json'}

exec(code, env_args)

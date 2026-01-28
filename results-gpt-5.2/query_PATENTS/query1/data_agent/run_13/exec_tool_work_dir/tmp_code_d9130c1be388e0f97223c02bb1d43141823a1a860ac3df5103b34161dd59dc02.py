code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_recs = load_records(var_call_4usfeDCRkF2VSIbLJzrZXtJa)
lev5_recs = load_records(var_call_QUHjDjavmPzgmFYZTWIH1bMS)

lev5_set = set(r['symbol'] for r in lev5_recs if r.get('symbol'))

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def extract_year(s):
    if not s: return None
    m = re.search(r'(19\d{2}|20\d{2})', str(s))
    return int(m.group(1)) if m else None

# Parse CPC codes from the JSON-like string
code_pat = re.compile(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+(?:/\d+(?:\.?\d+)?)?)"')

def extract_codes(cpc_str):
    if not cpc_str: return []
    return code_pat.findall(cpc_str)

rows = []
for r in pub_recs:
    y = extract_year(r.get('filing_date'))
    if y is None: 
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count each unique code once per publication
    for c in set(codes):
        if c in lev5_set:
            rows.append((c, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().reset_index(name='n')
    # build full year index per symbol
    alpha = 0.2
    all_out = []
    for sym, g in counts.groupby('symbol'):
        g2 = g.set_index('year').sort_index()
        years = list(range(int(g2.index.min()), int(g2.index.max())+1))
        s = g2.reindex(years, fill_value=0)['n']
        ema = []
        prev = None
        for val in s.tolist():
            prev = val if prev is None else alpha*val + (1-alpha)*prev
            ema.append(prev)
        ema_s = pd.Series(ema, index=years)
        best_year = int(ema_s.idxmax())
        best_val = float(ema_s.max())
        if best_year == 2022:
            all_out.append({'symbol': sym, 'best_year': best_year, 'best_ema': best_val})
    # We only need CPC group codes; sort by best_ema desc then symbol
    out = [d['symbol'] for d in sorted(all_out, key=lambda x: (-x['best_ema'], x['symbol']))]

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4usfeDCRkF2VSIbLJzrZXtJa': 'file_storage/call_4usfeDCRkF2VSIbLJzrZXtJa.json', 'var_call_QUHjDjavmPzgmFYZTWIH1bMS': 'file_storage/call_QUHjDjavmPzgmFYZTWIH1bMS.json'}

exec(code, env_args)

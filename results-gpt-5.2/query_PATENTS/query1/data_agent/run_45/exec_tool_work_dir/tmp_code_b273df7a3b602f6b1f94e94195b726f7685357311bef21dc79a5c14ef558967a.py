code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pub = load_records(var_call_fLFp1eGTjv9bY8J4shonPXL7)
level5 = load_records(var_call_zoSh07oYuyzTSMIAyRLnYtHn)
level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

# parse year from natural language filing_date
month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    return int(m.group(1)) if m else None

def extract_codes(cpc_str):
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
        # fallback regex for CPC-like codes
        return re.findall(r'\b[A-HY]\d{2}[A-Z]\d*(?:/\d+)?\b', cpc_str)

rows = []
for r in pub:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count each CPC code once per publication record
    for c in set(codes):
        # map to level-5 group code by taking section+class+subclass (e.g., H01M10/0565 -> H01M)
        m = re.match(r'^([A-HY]\d{2}[A-Z])', c)
        if not m:
            continue
        grp5 = m.group(1)
        if grp5 in level5_set:
            rows.append((y, grp5))

df = pd.DataFrame(rows, columns=['year','cpc5'])
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc5','year']).size().rename('n').reset_index()
    # compute EMA per cpc5 across years (sorted)
    alpha = 0.2
    res = []
    for cpc5, g in counts.groupby('cpc5'):
        g2 = g.sort_values('year').copy()
        ema = None
        for _, row in g2.iterrows():
            n = float(row['n'])
            ema = n if ema is None else (alpha*n + (1-alpha)*ema)
            res.append({'cpc5': cpc5, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(res)
    # for each year, find cpc5 with highest ema
    idx = ema_df.sort_values(['year','ema'], ascending=[True, False]).groupby('year').head(1)
    # keep only those where best year is 2022
    out = sorted(idx[idx['year']==2022]['cpc5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fLFp1eGTjv9bY8J4shonPXL7': 'file_storage/call_fLFp1eGTjv9bY8J4shonPXL7.json', 'var_call_zoSh07oYuyzTSMIAyRLnYtHn': 'file_storage/call_zoSh07oYuyzTSMIAyRLnYtHn.json'}

exec(code, env_args)

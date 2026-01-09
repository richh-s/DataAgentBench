code = """import json, re
import pandas as pd

# Load filings
filings_src = var_call_q7xG7lc5QsH83AGhtMphTkHi
if isinstance(filings_src, str):
    with open(filings_src, 'r', encoding='utf-8') as f:
        filings = json.load(f)
else:
    filings = filings_src

# Load level-5 CPC group symbols
lvl5_src = var_call_BA8DsWeLrwIZqZlG1vuCnBl8
if isinstance(lvl5_src, str):
    with open(lvl5_src, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl5_src

lvl5_set = set([r['symbol'] for r in lvl5 if r.get('symbol')])

month_map = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
    'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

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
        for e in arr:
            c = e.get('code')
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback: find CPC-like patterns
        return re.findall(r'[A-HY][0-9]{2}[A-Z]\s*\d+(?:/\d+)?', cpc_str)

rows = []
for rec in filings:
    y = parse_year(rec.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(rec.get('cpc'))
    if not codes:
        continue
    # map to level-5 group: first 4 chars (e.g., H01M) per provided level-5 symbols list
    groups = set()
    for c in codes:
        g = c.replace(' ', '')[:4]
        if g in lvl5_set:
            groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['group','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['group','year']).reset_index(name='filings').sort_values(['group','year'])
    alpha = 0.2

    def ema_per_group(sub):
        sub = sub.sort_values('year')
        ema = []
        prev = None
        for v in sub['filings'].tolist():
            prev = v if prev is None else (alpha*v + (1-alpha)*prev)
            ema.append(prev)
        sub = sub.copy()
        sub['ema'] = ema
        return sub

    ema_df = counts.groupby('group', group_keys=False).apply(ema_per_group)
    # best year per group
    idx = ema_df.groupby('group')['ema'].idxmax()
    best = ema_df.loc[idx, ['group','year','ema']]
    best_2022 = best[best['year']==2022].sort_values('ema', ascending=False)
    out = best_2022['group'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_q7xG7lc5QsH83AGhtMphTkHi': 'file_storage/call_q7xG7lc5QsH83AGhtMphTkHi.json', 'var_call_BA8DsWeLrwIZqZlG1vuCnBl8': 'file_storage/call_BA8DsWeLrwIZqZlG1vuCnBl8.json'}

exec(code, env_args)

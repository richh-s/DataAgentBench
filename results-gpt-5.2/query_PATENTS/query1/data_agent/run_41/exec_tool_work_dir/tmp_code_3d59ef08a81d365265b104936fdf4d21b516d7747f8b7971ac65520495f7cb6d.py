code = """import json, re
import pandas as pd
from datetime import datetime

# Load data
pub_src = var_call_eiXpPQh1psvAn5lq3SQxmy5N
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

lvl5_src = var_call_tnXAf73SG1SCIYU5eTUwnpM5
if isinstance(lvl5_src, str):
    with open(lvl5_src, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl5_src

lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol') is not None)

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    if not m:
        return None
    return int(m.group(0))

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for it in arr:
            c = it.get('code') if isinstance(it, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\\s*:\\s*"([A-Z]\d{2}[A-Z]?[0-9A-Z]*/?[^\"]*)"', cpc_str)

rows = []
for r in pubs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count one filing per (year, code) occurrence; de-dup within publication
    seen = set()
    for c in codes:
        if c in seen:
            continue
        seen.add(c)
        # take level-5 group as substring before '/'
        grp = c.split('/')[0]
        if grp in lvl5_set:
            rows.append((y, grp))

df = pd.DataFrame(rows, columns=['year','symbol'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')
    # compute EMA per symbol over years ascending
    alpha = 0.2
    def ema_for_symbol(g):
        g = g.sort_values('year').copy()
        ema = []
        prev = None
        for v in g['filings'].tolist():
            if prev is None:
                prev = v
            else:
                prev = alpha*v + (1-alpha)*prev
            ema.append(prev)
        g['ema'] = ema
        return g
    ema_df = counts.groupby('symbol', group_keys=False).apply(ema_for_symbol)
    # best year per symbol is year with max ema; tie -> latest year
    ema_df['rank_key'] = ema_df['ema']
    best = (ema_df.sort_values(['symbol','ema','year'], ascending=[True, False, False])
                  .groupby('symbol', as_index=False).head(1))
    res = best[best['year']==2022]['symbol'].sort_values().tolist()
    out = res

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eiXpPQh1psvAn5lq3SQxmy5N': 'file_storage/call_eiXpPQh1psvAn5lq3SQxmy5N.json', 'var_call_tnXAf73SG1SCIYU5eTUwnpM5': 'file_storage/call_tnXAf73SG1SCIYU5eTUwnpM5.json'}

exec(code, env_args)

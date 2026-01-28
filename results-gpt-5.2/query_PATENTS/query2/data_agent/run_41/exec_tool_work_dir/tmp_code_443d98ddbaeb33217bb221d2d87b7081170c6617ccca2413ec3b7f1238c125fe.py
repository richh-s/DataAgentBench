code = """import json, re, pandas as pd
from datetime import datetime

# load full results from file
path = var_call_lJIqyEVbkWdViV1nw7bCmiLb
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

def parse_grant_in_2019_h2(s):
    if not s: return False
    s2 = s.lower()
    if '2019' not in s2: return False
    h2_months = ['july','august','september','october','november','december']
    return any(m in s2 for m in h2_months)

def country_is_de(pat_info):
    if not pat_info: return False
    # try explicit country_code: DE
    if 'country_code' in pat_info:
        return bool(re.search(r'country_code\s*:\s*DE\b', pat_info))
    # fallback: starts with 'The DE ' or 'In DE,' or 'Application ... from DE'
    return bool(re.search(r'(^|\b)(DE)\b', pat_info)) and (' the de ' in pat_info.lower() or ' in de' in pat_info.lower() or ' from de' in pat_info.lower())

def extract_year(filing_date):
    if not filing_date: return None
    m = re.search(r'(19\d{2}|20\d{2})', filing_date)
    return int(m.group(1)) if m else None

def cpc_level4(code):
    if not code or '/' not in code: return None
    main, sub = code.split('/',1)
    # keep first digit after slash
    m = re.match(r'(\d)', sub.strip())
    if not m: return None
    return f"{main}/{m.group(1)}"

records=[]
for r in rows:
    if not parse_grant_in_2019_h2(r.get('grant_date')):
        continue
    if not country_is_de(r.get('Patents_info','')):
        continue
    y = extract_year(r.get('filing_date'))
    if y is None: continue
    cpc_str = r.get('cpc')
    if not cpc_str: continue
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lvl4 = cpc_level4(code)
        if lvl4:
            records.append({'lvl4': lvl4, 'year': y})

df = pd.DataFrame(records)
if df.empty:
    out = {'error':'No DE patents granted in H2 2019 found with parsable filing_date/CPC in this dataset.'}
    import json as _json
    print('__RESULT__:')
    print(_json.dumps(out))
    raise SystemExit

counts = df.groupby(['lvl4','year']).size().reset_index(name='filings')

alpha = 0.1
best=[]
for lvl4, g in counts.groupby('lvl4'):
    g2 = g.sort_values('year').copy()
    ema = []
    prev = None
    for v in g2['filings'].tolist():
        prev = v if prev is None else alpha*v + (1-alpha)*prev
        ema.append(prev)
    g2['ema']=ema
    idx = g2['ema'].idxmax()
    row = g2.loc[idx]
    best.append({'lvl4': lvl4, 'best_year': int(row['year']), 'max_ema': float(row['ema'])})

best_df = pd.DataFrame(best).sort_values(['max_ema','lvl4'], ascending=[False,True]).reset_index(drop=True)
# keep all with highest ema (ties)
max_ema = best_df['max_ema'].max()
leaders = best_df[best_df['max_ema']==max_ema].copy()

# query titles for these lvl4 symbols
symbols = leaders['lvl4'].tolist()

import json as _json
print('__RESULT__:')
print(_json.dumps({'symbols': symbols, 'leaders': leaders.to_dict(orient='records')}))"""

env_args = {'var_call_PhPbGH1dvYTAuiOmjQqmdKiP': ['publicationinfo'], 'var_call_BMzPzmEyVG2PqnZbT0FYrltr': ['cpc_definition'], 'var_call_GirDRb8rGDSWbJfVQd3Ub24I': [], 'var_call_DXGoGaA5MLEJABv3gAKp5KFR': 'file_storage/call_DXGoGaA5MLEJABv3gAKp5KFR.json', 'var_call_lJIqyEVbkWdViV1nw7bCmiLb': 'file_storage/call_lJIqyEVbkWdViV1nw7bCmiLb.json'}

exec(code, env_args)

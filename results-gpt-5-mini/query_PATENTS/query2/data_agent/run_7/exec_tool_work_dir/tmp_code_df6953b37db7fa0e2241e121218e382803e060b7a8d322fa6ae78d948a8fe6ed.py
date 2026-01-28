code = """import json
import pandas as pd
import re

data_path = var_call_DOJ8NTBO8k3pUFTiKas6Zehx
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def clean_date(s):
    if not s or not isinstance(s, str):
        return None
    s2 = s
    s2 = s2.replace('on ', ' ')
    s2 = s2.replace('dated ', ' ')
    s2 = s2.replace('the ', ' ')
    s2 = re.sub('(\d+)(st|nd|rd|th)', '\\1', s2)
    s2 = s2.replace(',', ' ')
    s2 = s2.strip()
    return pd.to_datetime(s2, dayfirst=True, errors='coerce')

filtered = []
for r in records:
    gd = clean_date(r.get('grant_date'))
    if gd is None:
        continue
    if not (pd.Timestamp('2019-07-01') <= gd <= pd.Timestamp('2019-12-31')):
        continue
    pi = r.get('Patents_info','')
    pi_up = pi.upper()
    is_germany = False
    if 'GERMANY' in pi_up:
        is_germany = True
    else:
        if 'DE-' in pi_up or ' DE ' in pi_up or pi_up.startswith('DE'):
            is_germany = True
    if not is_germany:
        continue
    cpc_field = r.get('cpc')
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        cpc_list = []
    fd = clean_date(r.get('filing_date'))
    if fd is None:
        continue
    filing_year = int(fd.year)
    codes = []
    for item in cpc_list:
        code = item.get('code') if isinstance(item, dict) else None
        if not code:
            continue
        code = str(code).strip()
        if len(code) >= 4:
            group = code[:4]
            codes.append(group)
    if not codes:
        continue
    for g in codes:
        filtered.append({'group': g, 'filing_year': filing_year})

if not filtered:
    out = {'groups': []}
    print('__RESULT__:')
    print(json.dumps(out))
else:
    df = pd.DataFrame(filtered)
    counts = df.groupby(['group','filing_year']).size().reset_index(name='count')
    results = []
    for group, grp_df in counts.groupby('group'):
        grp_sorted = grp_df.sort_values('filing_year')
        years = list(grp_sorted['filing_year'])
        vals = list(grp_sorted['count'])
        s = pd.Series(vals, index=years)
        ema = s.ewm(alpha=0.1, adjust=False).mean()
        best_year = int(ema.idxmax())
        best_ema = float(ema.max())
        results.append({'symbol': group, 'best_year': best_year, 'best_ema': best_ema})
    results = sorted(results, key=lambda x: x['best_ema'], reverse=True)
    out = {'groups': results}
    print('__RESULT__:')
    print(json.dumps(out))"""

env_args = {'var_call_DOJ8NTBO8k3pUFTiKas6Zehx': 'file_storage/call_DOJ8NTBO8k3pUFTiKas6Zehx.json'}

exec(code, env_args)

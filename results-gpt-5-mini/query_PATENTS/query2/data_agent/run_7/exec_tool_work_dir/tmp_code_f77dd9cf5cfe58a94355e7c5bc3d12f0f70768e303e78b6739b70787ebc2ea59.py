code = """import json
import pandas as pd
import re

# Load the query result stored in var_call_DOJ8NTBO8k3pUFTiKas6Zehx
data_path = var_call_DOJ8NTBO8k3pUFTiKas6Zehx

with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Helper to clean ordinal suffixes and stray words and parse date
def clean_date(s):
    if not s or not isinstance(s, str):
        return None
    s2 = s
    s2 = s2.replace('on ', ' ')
    s2 = s2.replace('dated ', ' ')
    s2 = s2.replace('the ', ' ')
    s2 = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", s2)
    s2 = s2.replace(',', ' ')
    s2 = s2.strip()
    try:
        return pd.to_datetime(s2, dayfirst=True, errors='coerce')
    except Exception:
        return None

# Filter for grants in second half of 2019 and Germany
filtered = []
for r in records:
    gd = clean_date(r.get('grant_date'))
    if gd is None:
        continue
    if not (pd.Timestamp('2019-07-01') <= gd <= pd.Timestamp('2019-12-31')):
        continue
    pi = r.get('Patents_info','')
    pi_up = pi.upper()
    # Consider as Germany if 'DE' present as whole word or 'GERMANY' present
    is_germany = False
    if 'GERMANY' in pi_up:
        is_germany = True
    else:
        # look for DE as separate token or DE- pattern
        if re.search(r'\bDE\b', pi_up) or re.search(r'DE[-_]', pi_up):
            is_germany = True
    if not is_germany:
        continue
    # parse cpc field
    cpc_field = r.get('cpc')
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpc_list = json.loads(cpc_field.replace("\n", "").replace("\t", ""))
        except Exception:
            cpc_list = []
    # parse filing date
    fd = clean_date(r.get('filing_date'))
    if fd is None:
        continue
    filing_year = int(fd.year)
    # extract codes
    codes = []
    for item in cpc_list:
        code = item.get('code')
        if not code or not isinstance(code, str):
            continue
        code = code.strip()
        if len(code) >= 4:
            group = code[:4]
            codes.append(group)
    if not codes:
        continue
    for g in codes:
        filtered.append({'group': g, 'filing_year': filing_year})

if not filtered:
    result = {'groups': []}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    df = pd.DataFrame(filtered)
    # get annual counts per group
    counts = df.groupby(['group','filing_year']).size().reset_index(name='count')
    results = []
    for group, grp_df in counts.groupby('group'):
        grp_sorted = grp_df.sort_values('filing_year')
        years = list(grp_sorted['filing_year'])
        vals = list(grp_sorted['count'])
        s = pd.Series(vals, index=years)
        ema = s.ewm(alpha=0.1, adjust=False).mean()
        # find year with max EMA value
        best_year = int(ema.idxmax())
        best_ema = float(ema.max())
        results.append({'symbol': group, 'best_year': best_year, 'best_ema': best_ema})
    # sort by best_ema descending
    results = sorted(results, key=lambda x: x['best_ema'], reverse=True)
    out = {'groups': results}
    print('__RESULT__:')
    print(json.dumps(out))"""

env_args = {'var_call_DOJ8NTBO8k3pUFTiKas6Zehx': 'file_storage/call_DOJ8NTBO8k3pUFTiKas6Zehx.json'}

exec(code, env_args)

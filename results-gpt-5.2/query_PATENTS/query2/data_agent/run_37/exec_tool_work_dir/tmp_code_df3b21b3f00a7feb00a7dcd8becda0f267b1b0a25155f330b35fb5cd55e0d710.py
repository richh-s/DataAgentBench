code = """import json, re, pandas as pd
from datetime import datetime

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

recs = load_records(var_call_RiCRSu3nJsBDToOCdy52cLia)

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def grant_in_h2_2019(s):
    if not s: return False
    s2 = s.lower()
    if '2019' not in s2:
        return False
    months = ['july','august','september','october','november','december']
    return any(m in s2 for m in months)

# Germany filter: look for country_code: DE or (application no/pub number starting with DE)

def is_germany(pi):
    if not pi: return False
    s = pi.upper()
    if 'COUNTRY_CODE: DE' in s or 'COUNTRY CODE: DE' in s or 'COUNTRY_CODE DE' in s:
        return True
    # publication number patterns like DE-xxxx or DE xxxxxx
    if re.search(r'\bDE[-\s]\d', s):
        return True
    # application no. DE-...
    if re.search(r'\bDE[-\s]\d', s):
        return True
    return False

rows=[]
for r in recs:
    if not grant_in_h2_2019(r.get('grant_date')):
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    fy = parse_year(r.get('filing_date',''))
    if fy is None:
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpcs:
        code = c.get('code')
        if not code or '/' not in code:
            continue
        # level 4 group: subclass+main group (before '/')
        group4 = code.split('/')[0]
        rows.append({'group4': group4, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out = {'error':'No Germany patents found granted in H2 2019 with parsable filing_year/CPC.'}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

counts = df.groupby(['group4','filing_year']).size().reset_index(name='n').sort_values(['group4','filing_year'])

alpha = 0.1
# compute EMA per group over years in ascending order
emas=[]
for g, sub in counts.groupby('group4'):
    sub = sub.sort_values('filing_year')
    ema = None
    for _, row in sub.iterrows():
        x = float(row['n'])
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        emas.append({'group4': g, 'year': int(row['filing_year']), 'count': int(row['n']), 'ema': float(ema)})
ema_df = pd.DataFrame(emas)
# best year per group
idx = ema_df.groupby('group4')['ema'].idxmax()
best = ema_df.loc[idx].copy()
# find groups with highest best ema
max_ema = best['ema'].max()
top = best[best['ema'] == max_ema].copy().sort_values(['group4'])

result = {
    'max_best_ema': float(max_ema),
    'top_groups': top[['group4','year','count','ema']].to_dict(orient='records'),
    'all_best': best[['group4','year','count','ema']].to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fWoBdtfzvtfpAqHtYQJx12kq': ['publicationinfo'], 'var_call_FbjtCBIZZrwEZlCxa83XVd3o': ['cpc_definition'], 'var_call_Q5ZzXOqmTPXaIkbz0AfsetRY': [], 'var_call_RiCRSu3nJsBDToOCdy52cLia': 'file_storage/call_RiCRSu3nJsBDToOCdy52cLia.json'}

exec(code, env_args)

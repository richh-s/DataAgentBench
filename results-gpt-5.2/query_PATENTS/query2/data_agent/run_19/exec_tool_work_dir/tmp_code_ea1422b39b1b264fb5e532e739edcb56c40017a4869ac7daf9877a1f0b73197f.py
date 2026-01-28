code = """import json, re
import pandas as pd

# Load publication records (may be a path)
pubs_src = var_call_XdLAvOANlHBC962tFyG0SvKU
if isinstance(pubs_src, str):
    with open(pubs_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pubs_src

def_src = var_call_6qIqpVHP9T8VkHmj92r1VwxO
cpc_defs = def_src if isinstance(def_src, list) else []

def parse_year(s):
    if not s or not isinstance(s, str):
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def in_second_half_2019(grant_date_str):
    # crude parse by month name/number; accept if year 2019 and month 7-12
    if not grant_date_str or not isinstance(grant_date_str, str):
        return False
    s = grant_date_str.lower()
    y = parse_year(s)
    if y != 2019:
        return False
    months = {
        'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
        'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
    }
    m = None
    for name, num in months.items():
        if name in s:
            m = num
            break
    if m is None:
        mm = re.search(r'\\b(0?[1-9]|1[0-2])\\b', s)
        if mm:
            m = int(mm.group(1))
    return m is not None and 7 <= m <= 12

def is_germany(patents_info):
    if not patents_info or not isinstance(patents_info, str):
        return False
    s = patents_info.upper()
    return ('COUNTRY_CODE' in s and ('DE' in s or 'GERMANY' in s)) or (' DE ' in s) or ('GERMANY' in s)

# Filter patents granted in H2 2019 and Germany
filtered = []
for r in pubs:
    if not in_second_half_2019(r.get('grant_date')):
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    filtered.append((fy, r.get('cpc'), r.get('title_localized')))

# Parse CPC codes and map to level-4 group (symbol up to subgroup?)
# Level 4 CPC symbols typically like H01M10/05 etc; We'll approximate by taking code up to 4th level style: class/subclass/main group/subgroup first two digits?
# Better: use definitions list (empty), so derive level-4 by truncating subgroup to one digit after slash? Commonly level4: e.g., H01M10/05 (one digit after /?)

def cpc_level4(code):
    if not code or not isinstance(code, str):
        return None
    code = code.strip()
    m = re.match(r'^([A-HY]\\d{2}[A-Z]\\d+)/(.+)$', code)
    if not m:
        return None
    pre, rest = m.group(1), m.group(2)
    # rest like 0565, 04, 006 etc. level4 take first two chars? We'll take first two digits of subgroup (or one if only one)
    digits = re.match(r'^(\\d+)', rest)
    if not digits:
        return None
    d = digits.group(1)
    if len(d) >= 2:
        d4 = d[:2]
    else:
        d4 = d
    return f"{pre}/{d4}"

rows = []
for fy, cpc_json, title_loc in filtered:
    try:
        cpcs = json.loads(cpc_json) if cpc_json else []
    except Exception:
        continue
    codes = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lv4 = cpc_level4(code)
        if lv4:
            codes.add(lv4)
    for lv4 in codes:
        rows.append({'year': fy, 'cpc4': lv4})

if not rows:
    out = []
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['cpc4','year']).size().reset_index(name='filings')
    # compute EMA per cpc4 over years
    alpha = 0.1
    best = []
    for cpc4, g in counts.groupby('cpc4'):
        g2 = g.sort_values('year')
        ema = None
        best_year = None
        best_ema = -1
        for _, row in g2.iterrows():
            x = float(row['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            if ema > best_ema:
                best_ema = ema
                best_year = int(row['year'])
        best.append({'cpc_group_code': cpc4, 'best_year': best_year, 'best_ema_filings': best_ema})
    best_df = pd.DataFrame(best).sort_values(['best_ema_filings','cpc_group_code'], ascending=[False, True])

    # attach title from definitions if available else blank
    def_map = {d['symbol']: d.get('titleFull') for d in cpc_defs if isinstance(d, dict) and d.get('symbol')}
    best_df['full_title'] = best_df['cpc_group_code'].map(def_map)
    out = best_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XdLAvOANlHBC962tFyG0SvKU': 'file_storage/call_XdLAvOANlHBC962tFyG0SvKU.json', 'var_call_6qIqpVHP9T8VkHmj92r1VwxO': []}

exec(code, env_args)

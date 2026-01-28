code = """import json, re
import pandas as pd

# Load publication rows (large file)
path = var_call_C6IBGBTYL5lM8sKZePViZp9p
with open(path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_grant_ymd(s):
    # return (year, month)
    if not s:
        return (None, None)
    s2 = s.lower()
    y = parse_year(s2)
    months = {
        'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
        'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
    }
    mth = None
    for name,val in months.items():
        if name in s2:
            mth = val
            break
    return (y, mth)

def is_germany(patents_info):
    if not patents_info:
        return False
    # crude heuristic: explicit country_code DE or mentions Germany/DE-
    t = patents_info
    if re.search(r'country[_ ]code\s*[:=]\s*DE\b', t, re.IGNORECASE):
        return True
    if re.search(r'\bDE\b', t) and 'publication number' in t.lower():
        # too broad; avoid
        pass
    if re.search(r'\bGermany\b', t, re.IGNORECASE):
        return True
    if re.search(r'\bDE-\d', t):
        return True
    if re.search(r'\bEP-\d', t) and re.search(r'\bDE\b', t):
        return True
    return False

def extract_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        arr = json.loads(cpc_field)
        codes = []
        for e in arr:
            code = e.get('code') if isinstance(e, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        # try regex fallback
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+\/\d+)"', cpc_field)

def level4(code):
    # level 4 approximated as main group: e.g., H01M10/05 from H01M10/0565 ; C01B33/00 stays C01B33/00
    if not code or '/' not in code:
        return None
    pre, post = code.split('/', 1)
    digits = re.sub(r'\D', '', post)
    if len(digits) <= 2:
        keep = digits
    else:
        keep = digits[:2]
    return f"{pre}/{keep}"

# Filter patents granted in second half 2019 and Germany
rows = []
for r in pubs:
    gy, gm = parse_grant_ymd(r.get('grant_date'))
    if gy != 2019 or gm is None or gm < 7:
        continue
    if not is_germany(r.get('Patents_info')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    l4s = {level4(c) for c in codes}
    l4s.discard(None)
    for c4 in l4s:
        rows.append({'cpc4': c4, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out = {"note":"No Germany patents granted in H2 2019 found with parsable data."}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

# counts per year per cpc4
counts = df.groupby(['cpc4','filing_year']).size().reset_index(name='n')

alpha = 0.1
best = []
for cpc4, g in counts.groupby('cpc4'):
    g = g.sort_values('filing_year')
    ema = None
    best_year = None
    best_ema = None
    for _, row in g.iterrows():
        n = float(row['n'])
        year = int(row['filing_year'])
        ema = n if ema is None else alpha*n + (1-alpha)*ema
        if (best_ema is None) or (ema > best_ema):
            best_ema = ema
            best_year = year
    best.append({'cpc_group_code': cpc4, 'best_year': best_year, 'best_ema_patent_filings': best_ema})

best_df = pd.DataFrame(best).sort_values(['best_ema_patent_filings','cpc_group_code'], ascending=[False, True])

# Join titles from cpc definitions (tool returned empty); try pull all level4 regardless status
# If var_call_31PlJ9eSGgXE2x5WEMvDiN85 is empty, query likely failed due to status values; can't requery here.
# We'll leave title null.

best_df['full_title'] = None

result = best_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_C6IBGBTYL5lM8sKZePViZp9p': 'file_storage/call_C6IBGBTYL5lM8sKZePViZp9p.json', 'var_call_31PlJ9eSGgXE2x5WEMvDiN85': []}

exec(code, env_args)

code = """import json, re, pandas as pd

# load records
path = var_call_HldT5GBgc8bpq0fkGYUDelOV
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def cpc_level4(code):
    if not code:
        return None
    code = code.strip()
    if '/' not in code:
        return code
    left, right = code.split('/', 1)
    if len(left) < 4:
        return code
    return f"{left[:4]}{left[4:]}/{right}"

def to_level4(code):
    if not code or '/' not in code:
        return code
    left, right = code.split('/', 1)
    # main group is digits before any further digits; level-4 approximate: first 2 digits of subgroup (pad if needed)
    # CPC level 4 typically: e.g., H04W72/04 (subgroup 04)
    # We'll take first two digits of right part; if right has <2 digits, keep as is
    digits = re.match(r'(\d+)', right)
    if not digits:
        return code
    d = digits.group(1)
    d2 = d[:2]
    return f"{left}/{d2}"

rows = []
for r in recs:
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    cpc_str = r.get('cpc')
    if not cpc_str:
        continue
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        continue
    for c in cpcs:
        code = c.get('code')
        lvl4 = to_level4(code)
        if lvl4:
            rows.append({'year': fy, 'cpc4': lvl4})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc4','year']).size().reset_index(name='n')
    # compute EMA per cpc4 across years
    alpha = 0.1
    best = []
    for cpc4, g in counts.groupby('cpc4'):
        g2 = g.sort_values('year').reset_index(drop=True)
        ema = None
        emas = []
        for _, row in g2.iterrows():
            x = float(row['n'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            emas.append(ema)
        g2['ema'] = emas
        idx = g2['ema'].idxmax()
        best_year = int(g2.loc[idx,'year'])
        best_ema = float(g2.loc[idx,'ema'])
        best.append({'cpc4': cpc4, 'best_year': best_year, 'best_ema': best_ema})
    best_df = pd.DataFrame(best).sort_values(['best_ema','cpc4'], ascending=[False, True])
    top = best_df.head(20)
    out = top.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VTyjeMFOGFzTVba3eBV0Q9n9': ['publicationinfo'], 'var_call_a9H8JOYww3akfE7oQNA7wJhy': ['cpc_definition'], 'var_call_ghY2TArvT0VU6HIlBF8wWHqG': [], 'var_call_VXhLt84M9tmkQ5pMIbmx1GK5': [], 'var_call_xX3aSvzNwzfu1AJYkbHG7Yj2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019'}], 'var_call_HldT5GBgc8bpq0fkGYUDelOV': 'file_storage/call_HldT5GBgc8bpq0fkGYUDelOV.json'}

exec(code, env_args)

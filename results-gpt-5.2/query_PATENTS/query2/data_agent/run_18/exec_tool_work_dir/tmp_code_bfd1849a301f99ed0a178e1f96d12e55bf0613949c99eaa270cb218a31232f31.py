code = """import json, re, pandas as pd
from datetime import datetime

# load publication rows
p = var_call_EyN6r6klcUZG1Btf6sCsB1Iu
if isinstance(p, str):
    with open(p, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = p

# load level-4 CPC definitions
cpc_defs = var_call_N4ZpwlEg23CDRuclG03fH1gX
cpc_def_map = {r['symbol']: r.get('titleFull') for r in cpc_defs}

months = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12,
          'jan':1,'feb':2,'mar':3,'apr':4,'jun':6,'jul':7,'aug':8,'sep':9,'sept':9,'oct':10,'nov':11,'dec':12}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_grant_date(s):
    if not s: return None
    s2 = s.strip()
    m = re.search(r'\b(' + '|'.join(months.keys()) + r')\b', s2.lower())
    y = parse_year(s2)
    if not m or not y: return None
    mo = months[m.group(1)]
    return (y, mo)

def cpc_level4(code):
    if not code: return None
    code = code.strip()
    # Level-4 in this dataset corresponds to 3-char subclass without slash (e.g., B04, G06)
    m = re.match(r'^([A-HY]\d{2})', code)
    return m.group(1) if m else None

rows = []
for r in pubs:
    gi = r.get('Patents_info') or ''
    # Germany filter: look for ' DE ' markers; best effort
    if not re.search(r'\bDE\b', gi):
        continue

    gd = r.get('grant_date')
    g = parse_grant_date(gd)
    if not g: 
        continue
    gy, gm = g
    if gy != 2019 or gm < 7 or gm > 12:
        continue

    fy = parse_year(r.get('filing_date') or '')
    if not fy:
        continue

    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if isinstance(cpc_raw, str) else (cpc_raw or [])
    except Exception:
        cpcs = []
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lv4 = cpc_level4(code)
        if not lv4:
            continue
        rows.append({'cpc4': lv4, 'filing_year': fy})

if not rows:
    out = {'error':'No Germany patents granted H2 2019 found with parsable filing_year/CPC in this dataset.'}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df = pd.DataFrame(rows).drop_duplicates()  # dedupe per patent-row per cpc4? we lost patent id; approximate by unique (cpc4, filing_year) counts would be wrong
# Better: keep duplicates? can't without patent id. We'll approximate by counting rows occurrences (may overcount). We'll dedupe on (cpc4, filing_year, row_index)

# re-build with row_index for dedupe
rows2=[]
idx=0
for r in pubs:
    gi = r.get('Patents_info') or ''
    if not re.search(r'\bDE\b', gi):
        continue
    g = parse_grant_date(r.get('grant_date'))
    if not g: continue
    gy, gm = g
    if gy != 2019 or gm < 7 or gm > 12:
        continue
    fy = parse_year(r.get('filing_date') or '')
    if not fy: continue
    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if isinstance(cpc_raw, str) else (cpc_raw or [])
    except Exception:
        cpcs = []
    cpc4s=set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lv4 = cpc_level4(code)
        if lv4:
            cpc4s.add(lv4)
    for lv4 in cpc4s:
        rows2.append({'patent_idx': idx, 'cpc4': lv4, 'filing_year': fy})
    idx += 1

df = pd.DataFrame(rows2)
counts = df.groupby(['cpc4','filing_year'])['patent_idx'].nunique().reset_index(name='n_filings')

alpha = 0.1
results=[]
for cpc4, g in counts.groupby('cpc4'):
    g2 = g.sort_values('filing_year')
    ema=None
    best=None
    for _, row in g2.iterrows():
        x = float(row['n_filings'])
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        if (best is None) or (ema > best['ema']):
            best={'year': int(row['filing_year']), 'ema': float(ema)}
    results.append({'cpc4': cpc4, 'best_year': best['year'], 'best_ema': best['ema'], 'titleFull': cpc_def_map.get(cpc4)})

res_df = pd.DataFrame(results).sort_values(['best_ema','cpc4'], ascending=[False, True])
res = res_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_WYZxMAQx6vS4CMVmVtPildxr': [], 'var_call_mvcxzCXnTPenOzrNnrNyDu0A': [], 'var_call_r23cU7QLqXZsYjrH9TrXuAga': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'grant_date': '3rd August 2021'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'grant_date': 'dated 6th October 2020'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'grant_date': '21st of September, 2021'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'grant_date': 'on April 7th, 2020'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'grant_date': 'Mar 23rd, 2021'}], 'var_call_rp7FDVAnRcgYRrp4kQm8W2hb': [{'status': 'published', 'n': '260587'}, {'status': 'frozen', 'n': '221'}], 'var_call_W3lys1a2gmMzcCW28alXKLi2': [{'n': '277813', 'like_de': '23985'}], 'var_call_PPahaM8JrcxcgqIFkGgsD2Hh': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine', 'level': '9.0', 'status': 'published'}], 'var_call_N4ZpwlEg23CDRuclG03fH1gX': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_call_EyN6r6klcUZG1Btf6sCsB1Iu': 'file_storage/call_EyN6r6klcUZG1Btf6sCsB1Iu.json'}

exec(code, env_args)

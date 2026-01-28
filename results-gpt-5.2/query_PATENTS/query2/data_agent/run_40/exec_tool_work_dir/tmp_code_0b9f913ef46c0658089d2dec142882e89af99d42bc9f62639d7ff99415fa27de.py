code = """import json, re, pandas as pd
from datetime import datetime

# Load publication rows
pub_src = var_call_QmZdLLzJ3jtg4qmmLZUtFP9N
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pub_rows = json.load(f)
else:
    pub_rows = pub_src

# Load CPC level-4 definitions
cpc_src = var_call_u2afkkFbotuS5MHXmkaiWGUO
if isinstance(cpc_src, str):
    with open(cpc_src, 'r', encoding='utf-8') as f:
        cpc_rows = json.load(f)
else:
    cpc_rows = cpc_src

cpc4 = {r['symbol']: r.get('titleFull') for r in cpc_rows}

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_nl_date(s):
    if not s:
        return None
    s = str(s).strip()
    # remove commas
    s2 = re.sub(r',', ' ', s)
    s2 = re.sub(r'\s+', ' ', s2)
    # find month name
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', s2, re.I)
    if not m:
        return None
    month = month_map[m.group(1).lower()]
    # look for day near month (before or after)
    # patterns like '5th March 2019' or 'March the 18th 2019' or '21st of September 2021'
    year_m = re.search(r'\b(19\d{2}|20\d{2})\b', s2)
    if not year_m:
        return None
    year = int(year_m.group(1))
    # day: first 1-2 digit number that is not part of year and close
    # remove year then search
    tmp = re.sub(r'\b(19\d{2}|20\d{2})\b', '', s2)
    day_m = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', tmp)
    if not day_m:
        return None
    day = int(day_m.group(1))
    try:
        return datetime(year, month, day)
    except:
        return None

def extract_country(patents_info):
    if not patents_info:
        return None
    s = str(patents_info)
    m = re.search(r'\bcountry_code\s*[:=]\s*([A-Z]{2})\b', s)
    if m:
        return m.group(1)
    # sometimes might include 'In DE' etc; attempt find 'In Germany' or 'In DE'
    if re.search(r'\bGermany\b', s, re.I):
        return 'DE'
    return None

def cpc_to_level4(code):
    if not code:
        return None
    # remove spaces
    code = code.strip()
    # If already in cpc4 dict, keep
    if code in cpc4:
        return code
    # If contains '/', try progressively trim after slash to match level4
    if '/' in code:
        base, rest = code.split('/',1)
        digits = re.sub(r'\D','', rest)
        # try 2 digits then 1 then none
        for k in [2,1,0]:
            cand = base + '/' + digits[:k]
            if cand in cpc4:
                return cand
    # fallback: first 3 chars? (like H01M) but our cpc4 seems include subclasses too, e.g., F16
    # Return first 3? Not.
    return None

records = []
for r in pub_rows:
    country = extract_country(r.get('Patents_info'))
    if country != 'DE':
        continue
    gd = parse_nl_date(r.get('grant_date'))
    fd = parse_nl_date(r.get('filing_date'))
    if not gd or not fd:
        continue
    if not (gd.year == 2019 and 7 <= gd.month <= 12):
        continue
    cpc_text = r.get('cpc')
    if not cpc_text:
        continue
    try:
        cpcs = json.loads(cpc_text)
    except:
        continue
    filing_year = fd.year
    seen = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lvl4 = cpc_to_level4(code) if code else None
        if not lvl4 or lvl4 in seen:
            continue
        seen.add(lvl4)
        records.append({'symbol': lvl4, 'filing_year': filing_year})

if not records:
    out = {"error":"No DE patents granted in H2 2019 found with parsable filing_date and CPC."}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df = pd.DataFrame(records)
counts = df.groupby(['symbol','filing_year']).size().reset_index(name='filings')

alpha = 0.1
results = []
for sym, g in counts.groupby('symbol'):
    g2 = g.sort_values('filing_year')
    years = g2['filing_year'].tolist()
    vals = g2['filings'].tolist()
    ema = []
    prev = None
    for v in vals:
        prev = v if prev is None else (alpha*v + (1-alpha)*prev)
        ema.append(prev)
    max_ema = max(ema)
    best_year = years[ema.index(max_ema)]
    results.append({'symbol': sym, 'titleFull': cpc4.get(sym), 'best_year': int(best_year), 'max_ema': float(max_ema)})

res_df = pd.DataFrame(results).sort_values(['max_ema','symbol'], ascending=[False, True])
# highest EMA areas (could be ties)
max_overall = res_df['max_ema'].max()
res_top = res_df[res_df['max_ema'] == max_overall].copy()
res_top = res_top.sort_values('symbol')

answer_records = res_top[['titleFull','symbol','best_year','max_ema']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer_records))"""

env_args = {'var_call_QmZdLLzJ3jtg4qmmLZUtFP9N': 'file_storage/call_QmZdLLzJ3jtg4qmmLZUtFP9N.json', 'var_call_u2afkkFbotuS5MHXmkaiWGUO': 'file_storage/call_u2afkkFbotuS5MHXmkaiWGUO.json'}

exec(code, env_args)

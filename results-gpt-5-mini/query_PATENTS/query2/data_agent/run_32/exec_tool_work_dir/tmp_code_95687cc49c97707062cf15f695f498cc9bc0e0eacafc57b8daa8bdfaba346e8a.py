code = """import json
import re
from collections import defaultdict, OrderedDict

# Load data from previous query results stored in files
with open(var_call_QnBzlecy9XiFQwzoWleSSCyH, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_A6BU9c4LpR6l1Vrv8zeVMcMC, 'r', encoding='utf-8') as f:
    level4_defs = json.load(f)

# Build level4 symbol -> title mapping
level4_map = {d['symbol']: d.get('titleFull') for d in level4_defs}
# Sort symbols by length descending for longest-prefix matching
level4_symbols = sorted(level4_map.keys(), key=lambda s: -len(s))

# Month name to number mapping (short and long forms)
months = {
    'jan':1,'january':1,'feb':2,'february':2,'mar':3,'march':3,'apr':4,'april':4,
    'may':5,'jun':6,'june':6,'jul':7,'july':7,'aug':8,'august':8,'sep':9,'september':9,
    'oct':10,'october':10,'nov':11,'november':11,'dec':12,'december':12
}

alpha = 0.1

# Helper to detect Germany in Patents_info
def is_germany(s):
    if not s: return False
    s_up = s.upper()
    # check common patterns
    if ' FROM DE' in s_up or ' DE,' in s_up or ' DE ' in s_up or 'DE-' in s_up:
        # exclude cases where DE is part of word like 'DEVELOPMENT' -> ensure word boundary or DE- or DE,
        if re.search(r'\bDE\b', s_up) or 'DE-' in s_up or ',DE' in s_up or ' FROM DE' in s_up:
            return True
    return False

# Helper to get month number from grant_date string
def extract_month_year(s):
    if not s: return (None, None)
    s_low = s.lower()
    # find month name
    m = None
    for name, num in months.items():
        if name in s_low:
            m = num
            break
    # find year
    y_match = re.search(r"(19|20)\d{2}", s)
    y = int(y_match.group(0)) if y_match else None
    return m, y

# Helper to extract filing year
def extract_filing_year(s):
    if not s: return None
    m = re.search(r"(19|20)\d{2}", s)
    return int(m.group(0)) if m else None

# Helper to parse cpc string into list of codes
def parse_cpc(cpc_field):
    if not cpc_field: return []
    try:
        arr = json.loads(cpc_field)
        codes = []
        for item in arr:
            if isinstance(item, dict) and 'code' in item:
                codes.append(item['code'])
        return codes
    except Exception:
        # fallback: try to extract patterns like X00Y... using regex
        return re.findall(r"[A-Z]\d{2}[A-Z]\d*/?\d*", cpc_field)

# Filter patents: Germany and grant in second half of 2019 (months 7-12)
filtered = []
for p in pubs:
    info = p.get('Patents_info','')
    if not is_germany(info):
        continue
    grant = p.get('grant_date','')
    month, year = extract_month_year(grant)
    if year == 2019 and month and month >=7 and month <=12:
        filing_year = extract_filing_year(p.get('filing_date',''))
        if filing_year is None:
            # try to extract from Patents_info as fallback
            filing_year = extract_filing_year(info)
        codes = parse_cpc(p.get('cpc',''))
        filtered.append({'patents_info': info, 'grant_date': grant, 'filing_year': filing_year, 'codes': codes})

# Aggregate counts per level4 symbol per filing year
counts = defaultdict(lambda: defaultdict(int))  # symbol -> year -> count
for p in filtered:
    fy = p['filing_year']
    if fy is None:
        continue
    codes = p['codes']
    for code in codes:
        code_clean = code.split('/')[0]  # take part before slash
        matched = None
        for sym in level4_symbols:
            if code_clean.startswith(sym):
                matched = sym
                break
        if matched:
            counts[matched][fy] += 1

# For each symbol, compute EMA across years (sorted ascending)
results = []
for sym, year_counts in counts.items():
    # build sorted years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts.get(y,0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1-alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda kv: kv[1])[0]
    best_ema = ema_by_year[best_year]
    results.append({'symbol': sym, 'titleFull': level4_map.get(sym), 'best_year': best_year, 'best_year_ema': best_ema})

# Sort results by best_year_ema descending
results_sorted = sorted(results, key=lambda d: -d['best_year_ema'])

# Prepare JSON serializable output
out = []
for r in results_sorted:
    out.append({'cpc_group_code': r['symbol'], 'titleFull': r['titleFull'], 'best_year': r['best_year']})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_cOEOHjRW5B9oZBs8GlPaVSac': 'file_storage/call_cOEOHjRW5B9oZBs8GlPaVSac.json', 'var_call_A6BU9c4LpR6l1Vrv8zeVMcMC': 'file_storage/call_A6BU9c4LpR6l1Vrv8zeVMcMC.json', 'var_call_QnBzlecy9XiFQwzoWleSSCyH': 'file_storage/call_QnBzlecy9XiFQwzoWleSSCyH.json'}

exec(code, env_args)

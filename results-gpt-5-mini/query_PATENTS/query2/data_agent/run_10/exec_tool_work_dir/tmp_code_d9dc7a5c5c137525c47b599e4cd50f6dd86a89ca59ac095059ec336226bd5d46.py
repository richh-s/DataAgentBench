code = """import json
import re
from collections import defaultdict

# Load data from previous query results
path_pub = var_call_mWfqF5ieb7K31PkYRCuzr1kf
path_cpc = var_call_rZiaCM41mZGaFJJuv82Jy5p9

with open(path_pub, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(path_cpc, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from symbol to titleFull
symbol_title = {entry['symbol']: entry.get('titleFull') for entry in cpc_defs}

# Helper to detect Germany in Patents_info
def is_germany(patents_info):
    if not patents_info:
        return False
    s = patents_info
    if 'Germany' in s or 'GERMANY' in s:
        return True
    # word-boundary DE
    if re.search(r'\bDE\b', s):
        return True
    if re.search(r'\bDE-', s):
        return True
    return False

# Helper to parse grant_date and return (year, month) or (None,None)
month_map = {
    'jan':1,'january':1,'feb':2,'february':2,'mar':3,'march':3,'apr':4,'april':4,'may':5,'jun':6,'june':6,
    'jul':7,'july':7,'aug':8,'august':8,'sep':9,'sept':9,'september':9,'oct':10,'october':10,'nov':11,'november':11,'dec':12,'december':12
}

def parse_grant_date(s):
    if not s:
        return (None, None)
    s_low = s.lower()
    # find year
    y_match = re.search(r'(20\d{2}|19\d{2})', s_low)
    year = int(y_match.group(1)) if y_match else None
    # find month by name
    m = None
    for name, num in month_map.items():
        if name in s_low:
            m = num
            break
    return (year, m)

# Helper to parse filing_date year
def parse_filing_year(s):
    if not s:
        return None
    m = re.search(r'(20\d{2}|19\d{2})', s)
    return int(m.group(1)) if m else None

# Helper to parse cpc JSON string
def parse_cpc_field(s):
    if not s:
        return []
    try:
        arr = json.loads(s)
    except Exception:
        # try to fix single quotes
        try:
            arr = json.loads(s.replace("'", '"'))
        except Exception:
            return []
    codes = []
    for item in arr:
        if isinstance(item, dict) and 'code' in item:
            codes.append(item['code'])
    return codes

# Filter patents: grant_date in second half of 2019 and Germany
filtered = []
for p in pubs:
    pi = p.get('Patents_info', '')
    if not is_germany(pi):
        continue
    grant = p.get('grant_date','')
    year, month = parse_grant_date(grant)
    if year == 2019 and month and month >= 7:
        filtered.append(p)

# Aggregate counts by group and filing year
counts = defaultdict(lambda: defaultdict(int))  # counts[group][year]=count

for p in filtered:
    cpc_field = p.get('cpc','')
    codes = parse_cpc_field(cpc_field)
    # derive groups as first 3 chars (letter + 2 digits) or first 3 when letters + digits
    groups = set()
    for code in codes:
        if not code or len(code) < 3:
            continue
        # remove leading/trailing spaces
        code_clean = code.strip()
        # group = first 3 characters
        grp = code_clean[:3]
        # Ensure grp matches pattern like Letter+2digits or Y02 etc
        if re.match(r'^[A-Z]\d{2}$', grp):
            groups.add(grp)
        else:
            # try first 3 anyway
            groups.add(grp)
    filing_year = parse_filing_year(p.get('filing_date',''))
    if filing_year is None:
        continue
    for g in groups:
        counts[g][filing_year] += 1

# Compute EMA per group across sorted years with alpha=0.1
alpha = 0.1
results = []
for g, year_dict in counts.items():
    # sort years ascending
    years = sorted(year_dict.keys())
    if not years:
        continue
    emas = {}
    prev_ema = None
    for y in years:
        c = year_dict[y]
        if prev_ema is None:
            ema = c
        else:
            ema = alpha * c + (1-alpha) * prev_ema
        emas[y] = ema
        prev_ema = ema
    # find year with max ema
    best_year = max(emas.items(), key=lambda kv: kv[1])[0]
    max_ema = emas[best_year]
    results.append({'symbol': g, 'titleFull': symbol_title.get(g), 'best_year': int(best_year), 'max_ema': float(max_ema)})

# Sort results by max_ema descending
results_sorted = sorted(results, key=lambda x: x['max_ema'], reverse=True)

# Prepare final output: include only symbol, titleFull, best_year
final = [{'symbol': r['symbol'], 'titleFull': r['titleFull'], 'best_year': r['best_year']} for r in results_sorted]

import json
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_mWfqF5ieb7K31PkYRCuzr1kf': 'file_storage/call_mWfqF5ieb7K31PkYRCuzr1kf.json', 'var_call_rZiaCM41mZGaFJJuv82Jy5p9': 'file_storage/call_rZiaCM41mZGaFJJuv82Jy5p9.json'}

exec(code, env_args)

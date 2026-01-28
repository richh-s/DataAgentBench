code = """import json, re
from collections import defaultdict, OrderedDict

# Load data from provided storage file paths
with open(var_call_5rHtrHNCXLAWFEXzgsUP2BJs, 'r', encoding='utf-8') as f:
    records = json.load(f)
with open(var_call_NsvNsGurGkwfOEmVn6LEFA53, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping for CPC definitions: symbol -> titleFull
cpc_title = {rec.get('symbol'): rec.get('titleFull') for rec in cpc_defs if rec.get('symbol')}

# Month name to number
months = {m.lower(): i for i,m in enumerate(['', 'January','February','March','April','May','June','July','August','September','October','November','December'])}
# also short forms
shorts = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'sept':9,'oct':10,'nov':11,'dec':12}

# Helper to extract country from Patents_info
country_re_patterns = [r'from\s+([A-Z]{2})\b', r'In\s+([A-Z]{2})\b', r'\(no\.\s*([A-Z]{2})-', r'\bID\s*([A-Z]{2})-', r'\bapplication\s*\(no\.\s*([A-Z]{2})-']

def extract_country(s):
    for pat in country_re_patterns:
        m = re.search(pat, s)
        if m:
            return m.group(1)
    return None

# Helper to extract year and month from date string

def extract_year_month(s):
    if not s or not isinstance(s, str):
        return None, None
    # year
    y_match = re.search(r'(20\d{2})', s)
    year = int(y_match.group(1)) if y_match else None
    # month
    # look for month name
    m = None
    mm = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', s)
    if mm:
        m = months[mm.group(1).lower()]
    else:
        mm2 = re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b', s)
        if mm2:
            m = shorts[mm2.group(1).lower()]
    return year, m

# Helper to extract filing year
def extract_filing_year(s):
    if not s or not isinstance(s, str):
        return None
    m = re.search(r'(20\d{2})', s)
    return int(m.group(1)) if m else None

# Helper to parse cpc field which is JSON-like

def parse_cpc_field(s):
    if not s or not isinstance(s, str):
        return []
    try:
        arr = json.loads(s)
        codes = []
        for it in arr:
            code = it.get('code') if isinstance(it, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        # try to find all code-like patterns e.g., uppercase letters/digits + maybe slash
        return re.findall(r'([A-Z]\d+[A-Z]?\d*/?\d*)', s)

# Collect counts per level4 CPC group by filing year for DE patents granted in H2 2019
counts = defaultdict(lambda: defaultdict(int))

for rec in records:
    info = rec.get('Patents_info') or ''
    country = extract_country(info) or ''
    if country != 'DE':
        # also try to detect 'DE' occurrence like 'DE-' before number
        if re.search(r'\bDE[- ]', info):
            country = 'DE'
        else:
            continue
    # parse grant date
    grant = rec.get('grant_date') or ''
    g_year, g_month = extract_year_month(grant)
    if g_year != 2019:
        continue
    if not g_month or g_month < 7:
        continue
    # parse filing year
    filing = rec.get('filing_date') or ''
    f_year = extract_filing_year(filing)
    if not f_year:
        continue
    # parse cpc
    cpc_field = rec.get('cpc') or ''
    codes = parse_cpc_field(cpc_field)
    # For each code, extract level4 = first 4 alnum chars (letters+digits)
    for code in codes:
        if not code or not isinstance(code, str):
            continue
        code = code.strip()
        # remove leading/trailing punctuation
        code = code.strip('"')
        # find first part before slash
        left = code.split('/')[0]
        # take first 4 chars (letters and digits)
        lvl4 = left[:4]
        if len(lvl4) < 2:
            continue
        counts[lvl4][f_year] += 1

# Now compute EMA per group across years sorted
alpha = 0.1
results = []
for grp, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    best_ema = None
    best_year = None
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_year = y
    title = cpc_title.get(grp)
    results.append({'symbol': grp, 'titleFull': title, 'best_year': best_year, 'best_ema': round(best_ema,4) if best_ema is not None else None})

# Sort results by best_ema descending
results.sort(key=lambda x: (x['best_ema'] if x['best_ema'] is not None else -1), reverse=True)

# Output JSON
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_aotf5Uc4J2te04vTC8sI8JrG': ['publicationinfo'], 'var_call_IVHWtrdfXTmXDR9hUhfcqliw': ['cpc_definition'], 'var_call_pmiPwWzDql1MApaUfscIR8R0': 'file_storage/call_pmiPwWzDql1MApaUfscIR8R0.json', 'var_call_96ynt5c54hdqWNWAPK3VhPur': 'file_storage/call_96ynt5c54hdqWNWAPK3VhPur.json', 'var_call_NsvNsGurGkwfOEmVn6LEFA53': 'file_storage/call_NsvNsGurGkwfOEmVn6LEFA53.json', 'var_call_5rHtrHNCXLAWFEXzgsUP2BJs': 'file_storage/call_5rHtrHNCXLAWFEXzgsUP2BJs.json'}

exec(code, env_args)

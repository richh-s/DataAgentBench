code = """import json
import re
from collections import defaultdict

# Load publication query results
pub_path = var_call_EHbEMYKo074Zv2sTuPTXuM7R
with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Load CPC level-4 definitions
cpc_path = var_call_Kv5tC1VzLFwmfHnaIbS69gBH
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build level4 symbol->title mapping
symbol_title = {d['symbol']: d.get('titleFull','') for d in cpc_defs}
symbols = list(symbol_title.keys())
# Sort symbols by length desc for longest-prefix matching
symbols_sorted = sorted(symbols, key=lambda s: -len(s))

# Months for second half
months = ['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

# Helper to check Germany in Patents_info
def is_germany(text):
    if not text:
        return False
    t = text.lower()
    if 'germany' in t:
        return True
    # word boundary DE
    if re.search(r'\bDE\b', text):
        return True
    return False

# Helper to parse year from filing_date
def extract_year(text):
    if not text:
        return None
    m = re.search(r'(20\d{2}|19\d{2})', text)
    if m:
        return int(m.group(1))
    return None

# Helper to check if grant_date in H2 2019
def grant_in_h2_2019(text):
    if not text:
        return False
    t = text.lower()
    if '2019' not in t:
        return False
    return any(m in t for m in months)

# Helper to parse cpc codes from cpc field (JSON-like string)
def parse_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        arr = json.loads(cpc_field)
        codes = []
        for obj in arr:
            if isinstance(obj, dict) and 'code' in obj:
                codes.append(obj['code'].strip())
        return codes
    except Exception:
        # fallback: find patterns like "code": "..."
        codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
        return [c.strip() for c in codes]

# Aggregate counts per symbol per filing year
counts = defaultdict(lambda: defaultdict(int))  # symbol -> year -> count

for rec in pubs:
    pat_info = rec.get('Patents_info','') or ''
    grant = rec.get('grant_date','') or ''
    if not is_germany(pat_info):
        continue
    if not grant_in_h2_2019(grant):
        continue
    filing = rec.get('filing_date','') or ''
    year = extract_year(filing)
    if not year:
        continue
    cpc_field = rec.get('cpc','') or ''
    codes = parse_cpc_codes(cpc_field)
    # for each code, map to level4 symbol
    matched_symbols = set()
    for code in codes:
        for sym in symbols_sorted:
            if code.upper().startswith(sym.upper()):
                matched_symbols.add(sym)
                break
    for sym in matched_symbols:
        counts[sym][year] += 1

# Compute EMA (alpha=0.1) for each symbol across its years
alpha = 0.1
results = []
for sym, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    emas = {}
    # initialize ema to first year's count
    first_year = years[0]
    ema_prev = float(year_counts[first_year])
    emas[first_year] = ema_prev
    for y in years[1:]:
        x = float(year_counts[y])
        ema = alpha * x + (1-alpha) * ema_prev
        emas[y] = ema
        ema_prev = ema
    # find year with max ema
    best_year = max(emas.items(), key=lambda kv: kv[1])[0]
    max_ema = emas[best_year]
    results.append({'symbol': sym, 'titleFull': symbol_title.get(sym,''), 'best_year': best_year, 'max_ema': round(max_ema,6)})

# Sort results by max_ema desc
results_sorted = sorted(results, key=lambda r: -r['max_ema'])

# Output results
import json as _json
print("__RESULT__:")
print(_json.dumps(results_sorted))"""

env_args = {'var_call_oVJinBQXekJbtIDjcApMQnfR': ['publicationinfo'], 'var_call_0p2XknMQHwo1OKFNmwyPa8OC': ['cpc_definition'], 'var_call_EHbEMYKo074Zv2sTuPTXuM7R': 'file_storage/call_EHbEMYKo074Zv2sTuPTXuM7R.json', 'var_call_Kv5tC1VzLFwmfHnaIbS69gBH': 'file_storage/call_Kv5tC1VzLFwmfHnaIbS69gBH.json'}

exec(code, env_args)

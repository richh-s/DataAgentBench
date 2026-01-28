code = """import json, re

# Load the query results from the provided storage variables

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to json
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

var_78 = load_var(var_call_78J2tSPm8BIZqgaFNhNJazrN)
var_all_de_like = load_var(var_call_2On6o6E6Imrt4icb3Ix1jYtW)
var_cpc_level4 = load_var(var_call_9NnpQYkGSgTbvBm4y1UpP7X3)

# Build a set of valid level-4 symbols from cpc_definition
level4_symbols = {rec['symbol']: rec.get('titleFull') for rec in var_cpc_level4}

# helper to detect Germany in Patents_info
re_de_dash = re.compile(r'\bDE-', re.IGNORECASE)
re_germany = re.compile(r'germany', re.IGNORECASE)
re_in_de = re.compile(r'\bin\s+DE\b', re.IGNORECASE)
re_from_de = re.compile(r'from\s+DE\b', re.IGNORECASE)
re_the_de = re.compile(r'\bthe\s+DE\b', re.IGNORECASE)

def is_germany(pi):
    if not pi or not isinstance(pi, str):
        return False
    if re_de_dash.search(pi):
        return True
    if re_germany.search(pi):
        return True
    if re_in_de.search(pi):
        return True
    if re_from_de.search(pi):
        return True
    if re_the_de.search(pi):
        return True
    # also patterns like "In DE, the"
    if re.search(r'\bDE\b', pi):
        # last resort: ensure there's 'patent' or 'application' near it
        if re.search(r'DE[-\s]\d|DE[-\s]|DE\b.*application|DE\b.*patent', pi, re.IGNORECASE):
            return True
    return False

# parse cpc field which is JSON-like string
def parse_cpc_field(cpc_field):
    if not cpc_field:
        return []
    if isinstance(cpc_field, list):
        entries = cpc_field
    else:
        try:
            entries = json.loads(cpc_field)
        except Exception:
            # try to fix single quotes etc
            try:
                entries = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                return []
    codes = []
    for e in entries:
        if isinstance(e, dict) and 'code' in e:
            codes.append(e['code'])
        elif isinstance(e, str):
            codes.append(e)
    return codes

# map a CPC code to a level-4 symbol: take first 3 chars (letter + two digits) or up to first letter+2digits
def get_level4_symbol(code):
    if not code or not isinstance(code, str):
        return None
    # remove leading/trailing whitespace
    code = code.strip()
    # match letter + 2 digits
    m = re.match(r'([A-Z]\d{2})', code, re.I)
    if m:
        sym = m.group(1).upper()
        # sometimes symbols in cpc_definition have 3 chars like 'B23' or 'A61'
        return sym
    # fallback: take first 3 chars
    return code[:3].upper()

# Step 1: find level4 symbols that appear among patents granted in H2 2019 in Germany
h2_2019_germany_symbols = set()
for rec in var_78:
    pi = rec.get('Patents_info')
    if is_germany(pi):
        cpc_field = rec.get('cpc')
        codes = parse_cpc_field(cpc_field)
        for code in codes:
            sym = get_level4_symbol(code)
            if sym in level4_symbols:
                h2_2019_germany_symbols.add(sym)

# If none found in var_78 (possible), try scanning the broader DE-like set for grant_date in H2 2019
if not h2_2019_germany_symbols:
    for rec in var_all_de_like:
        grant = rec.get('grant_date','')
        if not grant or '2019' not in grant:
            continue
        # month check
        if any(m in grant.lower() for m in ['jul','aug','sep','oct','nov','dec']):
            if is_germany(rec.get('Patents_info')):
                codes = parse_cpc_field(rec.get('cpc'))
                for code in codes:
                    sym = get_level4_symbol(code)
                    if sym in level4_symbols:
                        h2_2019_germany_symbols.add(sym)

# Step 2: Build yearly filing counts for Germany for all years from the DE-like broader set
# We'll parse filing_date year and aggregate counts per symbol per year
counts = {}  # counts[symbol][year] = int
for rec in var_all_de_like:
    if not is_germany(rec.get('Patents_info')):
        continue
    filing = rec.get('filing_date','')
    if not filing or not isinstance(filing, str):
        continue
    ymatch = re.search(r'(19|20)\d{2}', filing)
    if not ymatch:
        continue
    year = int(ymatch.group(0))
    codes = parse_cpc_field(rec.get('cpc'))
    if not codes:
        continue
    for code in codes:
        sym = get_level4_symbol(code)
        if sym not in level4_symbols:
            continue
        counts.setdefault(sym, {}).setdefault(year, 0)
        counts[sym][year] += 1

# For each symbol that appeared in H2 2019 Germany grants, compute EMA across years and find best year
alpha = 0.1
results = []
for sym in sorted(h2_2019_germany_symbols):
    year_counts = counts.get(sym, {})
    if not year_counts:
        continue
    years = sorted(year_counts.keys())
    # compute EMA
    ema_by_year = {}
    ema = None
    for y in years:
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    title = level4_symbols.get(sym) or None
    results.append({'titleFull': title, 'symbol': sym, 'best_year': best_year})

# If results empty, respond with a short explanatory message
if not results:
    out = json.dumps({'error': 'No CPC level-4 groups in Germany found for patents granted in H2 2019 with available filing-year history.'})
else:
    out = json.dumps(results)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_78J2tSPm8BIZqgaFNhNJazrN': 'file_storage/call_78J2tSPm8BIZqgaFNhNJazrN.json', 'var_call_7FRmjLdhCCKQXfy789TZK3JW': 'file_storage/call_7FRmjLdhCCKQXfy789TZK3JW.json', 'var_call_9NnpQYkGSgTbvBm4y1UpP7X3': 'file_storage/call_9NnpQYkGSgTbvBm4y1UpP7X3.json', 'var_call_2On6o6E6Imrt4icb3Ix1jYtW': 'file_storage/call_2On6o6E6Imrt4icb3Ix1jYtW.json'}

exec(code, env_args)

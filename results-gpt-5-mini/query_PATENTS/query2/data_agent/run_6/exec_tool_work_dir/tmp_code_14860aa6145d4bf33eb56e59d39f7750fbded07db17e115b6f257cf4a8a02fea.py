code = """import json, re
from collections import defaultdict, Counter

# Load data from previous tool results (may be file paths or lists)
try:
    data_defs = var_call_6mTGXgy1qHzn6xIgI85G9bPw
except NameError:
    data_defs = None
try:
    data_pubs = var_call_Ic3cQgWXWHzjgXbINo2CYtV0
except NameError:
    data_pubs = None

def load_maybe_path(obj):
    if isinstance(obj, str):
        # assume it's a path to json
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

cpc_defs = load_maybe_path(data_defs)
pubs = load_maybe_path(data_pubs)

# Build level-4 symbol -> titleFull map
level4 = {}
for r in cpc_defs:
    sym = r.get('symbol')
    title = r.get('titleFull')
    if sym:
        level4[sym.upper()] = title

# helper to parse month from natural-language grant_date
months = {
    'jan':1,'january':1,
    'feb':2,'february':2,
    'mar':3,'march':3,
    'apr':4,'april':4,
    'may':5,
    'jun':6,'june':6,
    'jul':7,'july':7,
    'aug':8,'august':8,
    'sep':9,'sept':9,'september':9,
    'oct':10,'october':10,
    'nov':11,'november':11,
    'dec':12,'december':12
}

month_regex = re.compile(r'(' + '|'.join(months.keys()) + r')', re.IGNORECASE)

def extract_month(grant_text):
    if not grant_text:
        return None
    txt = grant_text.lower()
    if '2019' not in txt:
        return None
    m = month_regex.search(txt)
    if m:
        return months[m.group(1).lower()]
    # try numeric month
    m2 = re.search(r'2019\D*(\d{1,2})', grant_text)
    if m2:
        val = int(m2.group(1))
        if 1 <= val <= 12:
            return val
    return None

# helper to extract filing year
year_regex = re.compile(r'\b(19|20)\d{2}\b')

def extract_year(text):
    if not text:
        return None
    m = year_regex.search(text)
    if m:
        return int(m.group(0))
    return None

# Build mapping of level4 symbols list for prefix matching, sorted by length desc
level4_symbols = sorted(level4.keys(), key=lambda x: -len(x))

# Aggregate counts of filing years per level4 group for German patents granted in H2 2019
counts = defaultdict(Counter)

for rec in pubs:
    try:
        pat_info = rec.get('Patents_info','') or ''
        grant_date = rec.get('grant_date','') or ''
        # ensure Germany reference
        if not re.search(r'\bDE\b', pat_info, re.IGNORECASE):
            continue
        # ensure grant in 2019 and month in Jul-Dec
        month = extract_month(grant_date)
        if month is None or month < 7 or month > 12:
            continue
        # extract filing year
        filing_year = extract_year(rec.get('filing_date','') or '')
        if filing_year is None:
            continue
        # parse cpc field (JSON-like string)
        cpc_field = rec.get('cpc','') or ''
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            # try to fix single quotes
            try:
                cpc_list = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                continue
        # collect codes
        codes = []
        if isinstance(cpc_list, list):
            for entry in cpc_list:
                if isinstance(entry, dict):
                    code = entry.get('code')
                    if code:
                        codes.append(code.upper())
                elif isinstance(entry, str):
                    codes.append(entry.upper())
        # for each code, find best matching level4 symbol (longest prefix)
        matched_syms = set()
        for code in codes:
            code_norm = code.replace(' ', '')
            for sym in level4_symbols:
                if code_norm.startswith(sym):
                    matched_syms.add(sym)
                    break
        # if no matched syms, skip
        for sym in matched_syms:
            counts[sym][filing_year] += 1
    except Exception:
        continue

# For each group, compute EMA with alpha=0.1 across chronological years and find year with max EMA
alpha = 0.1
results = []
for sym, counter in counts.items():
    # build sorted years
    years = sorted(counter.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        val = counter[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with highest EMA
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    results.append({
        'symbol': sym,
        'titleFull': level4.get(sym),
        'best_year': int(best_year)
    })

# Sort results by symbol
results = sorted(results, key=lambda x: x['symbol'])

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_6mTGXgy1qHzn6xIgI85G9bPw': 'file_storage/call_6mTGXgy1qHzn6xIgI85G9bPw.json', 'var_call_Ic3cQgWXWHzjgXbINo2CYtV0': 'file_storage/call_Ic3cQgWXWHzjgXbINo2CYtV0.json'}

exec(code, env_args)

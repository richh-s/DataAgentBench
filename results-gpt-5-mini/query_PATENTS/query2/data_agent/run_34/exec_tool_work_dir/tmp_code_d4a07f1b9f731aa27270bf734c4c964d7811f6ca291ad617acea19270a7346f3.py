code = """import json
import re
from collections import defaultdict, Counter

# Load the large query results from files
with open(var_call_CUGasJKitqvVEKnfiZgLkLEm, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_hSBjej5rYMKyiHbwfXmsLUYe, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build map of level-4 symbols to titleFull
symbol_to_title = {row['symbol']: row.get('titleFull') for row in cpc_defs}

# Helper: extract year from a text
def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    m = re.search(r'(20\d{2}|19\d{2})', text)
    return int(m.group(1)) if m else None

# Helper: extract month number from text (1-12)
month_map = {name.lower(): i for i, name in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}
full_months = {m.lower(): i for i, m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def extract_month(text):
    if not text or not isinstance(text, str):
        return None
    # look for full month names
    for name, num in full_months.items():
        if name in text.lower():
            return num
    # look for short names
    m = re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\b', text, re.I)
    if m:
        return month_map[m.group(1)[:3].capitalize().lower().title().lower()] if False else ( {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}[m.group(1)[:3].lower()] )
    return None

# More robust DE detection in Patents_info
def is_germany(info):
    if not info or not isinstance(info, str):
        return False
    info_l = info.lower()
    if 'germany' in info_l:
        return True
    if 'de-' in info or ' de ' in info_l or ' from de' in info_l or ' in de' in info_l or re.search(r'\bde\b', info):
        return True
    return False

# Prepare set of level4 symbols
level4_symbols = set(symbol_to_title.keys())

# Counters per symbol per filing year
counts = defaultdict(Counter)

for rec in pubs:
    try:
        info = rec.get('Patents_info', '')
        if not is_germany(info):
            continue
        grant = rec.get('grant_date', '')
        year = extract_year(grant)
        if year != 2019:
            continue
        month = extract_month(grant)
        if month is None:
            # If month not found, skip unless grant string indicates 'second half' - but skip
            continue
        if month < 7:
            continue
        # extract filing year
        filing_year = extract_year(rec.get('filing_date',''))
        if filing_year is None:
            continue
        # parse cpc field
        cpc_field = rec.get('cpc', '')
        try:
            cpcs = json.loads(cpc_field)
        except Exception:
            # try to fix single quotes
            try:
                cpcs = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                continue
        for c in cpcs:
            code = c.get('code') if isinstance(c, dict) else None
            if not code or not isinstance(code, str):
                continue
            code = code.strip()
            # Try matching level4 symbols by prefix
            matched = False
            for sym in level4_symbols:
                if code.startswith(sym):
                    counts[sym][filing_year] += 1
                    matched = True
                    # don't break: a code could potentially match multiple? but prefix matching unique
                    break
    except Exception:
        continue

# Compute EMA per symbol across sorted years
alpha = 0.1
results = []
for sym, counter in counts.items():
    # need at least one year
    years = sorted(counter.keys())
    if not years:
        continue
    ema_vals = {}
    prev_ema = None
    for y in years:
        c = counter[y]
        if prev_ema is None:
            ema = float(c)
        else:
            ema = alpha * c + (1 - alpha) * prev_ema
        ema_vals[y] = ema
        prev_ema = ema
    # find year with max ema
    best_year = max(ema_vals.items(), key=lambda x: (x[1], x[0]))[0]
    best_ema = ema_vals[best_year]
    results.append({'symbol': sym, 'titleFull': symbol_to_title.get(sym), 'best_year': int(best_year), 'best_ema': float(best_ema)})

# Sort results by symbol
results_sorted = sorted(results, key=lambda x: x['symbol'])

import json
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_CUGasJKitqvVEKnfiZgLkLEm': 'file_storage/call_CUGasJKitqvVEKnfiZgLkLEm.json', 'var_call_hSBjej5rYMKyiHbwfXmsLUYe': 'file_storage/call_hSBjej5rYMKyiHbwfXmsLUYe.json'}

exec(code, env_args)

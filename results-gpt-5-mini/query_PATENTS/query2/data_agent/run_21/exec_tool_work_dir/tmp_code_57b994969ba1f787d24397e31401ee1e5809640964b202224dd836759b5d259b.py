code = """import json, re, math
from collections import defaultdict, OrderedDict

# Load data from storage-provided file paths
with open(var_call_SrJxyn2Ain576q0BL3OGPsTK, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_UTyGFRAIQHxjDMnqQAKmiibR, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping for level4 symbol -> titleFull
title_map = {row.get('symbol'): row.get('titleFull') for row in cpc_defs}

# Helper to detect Germany in Patents_info
def is_germany(text):
    if not text:
        return False
    t = text
    patterns = [r'\bGermany\b', r'\bDeutschland\b', r'country_code:\s*DE', r'\bDE\b', r'\bGmbH\b', r'\bAG\b']
    for p in patterns:
        if re.search(p, t, flags=re.IGNORECASE):
            return True
    return False

# Helper to extract filing year
def extract_year(text):
    if not text:
        return None
    m = re.search(r'(20\d{2}|19\d{2})', text)
    return int(m.group(1)) if m else None

# Helper to parse cpc codes from the cpc field
def extract_level4_symbols(cpc_field):
    if not cpc_field:
        return []
    try:
        items = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            items = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            return []
    symbols = set()
    for it in items:
        code = it.get('code') if isinstance(it, dict) else None
        if not code and isinstance(it, str):
            code = it
        if not code:
            continue
        # find level4 prefix: letter + two digits
        m = re.match(r'([A-Z]\d{2})', code)
        if m:
            symbols.add(m.group(1))
    return list(symbols)

# Aggregate counts by level4 symbol and filing year for German patents
counts = defaultdict(lambda: defaultdict(int))  # symbol -> year -> count
all_years = set()
for rec in pubs:
    info = rec.get('Patents_info') or ''
    if not is_germany(info):
        continue
    filing = rec.get('filing_date') or ''
    year = extract_year(filing)
    if not year:
        continue
    symbols = extract_level4_symbols(rec.get('cpc'))
    if not symbols:
        continue
    for s in symbols:
        counts[s][year] += 1
        all_years.add(year)

if not counts:
    result = []
else:
    # For consistent ordering, consider full span of years present
    years_sorted = sorted(all_years)
    alpha = 0.1
    ema_by_symbol = {}
    best_year_by_symbol = {}
    for s, year_counts in counts.items():
        # build ordered list of counts for all years (missing years -> 0)
        counts_list = [year_counts.get(y, 0) for y in years_sorted]
        ema = None
        ema_series = []
        for c in counts_list:
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1 - alpha) * ema
            ema_series.append(ema)
        # record final ema (last year)
        ema_by_symbol[s] = ema_series[-1]
        # best year is the year with max ema value
        max_idx = max(range(len(ema_series)), key=lambda i: ema_series[i])
        best_year_by_symbol[s] = {'year': years_sorted[max_idx], 'ema': ema_series[max_idx]}

    # prepare top 10 symbols by final EMA
    top = sorted(ema_by_symbol.items(), key=lambda x: x[1], reverse=True)[:10]
    result = []
    for sym, final_ema in top:
        title = title_map.get(sym) or None
        by = best_year_by_symbol.get(sym, {})
        result.append({'cpc_group': sym, 'titleFull': title, 'final_ema': final_ema, 'best_year': by.get('year'), 'best_year_ema': by.get('ema')})

# Ensure JSON serializable and print
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NEH1yFBaIfUrTYB2Ry124pro': ['publicationinfo'], 'var_call_gCc9bxyZ4HV0nwz0pby4NUUT': ['cpc_definition'], 'var_call_SrJxyn2Ain576q0BL3OGPsTK': 'file_storage/call_SrJxyn2Ain576q0BL3OGPsTK.json', 'var_call_UTyGFRAIQHxjDMnqQAKmiibR': 'file_storage/call_UTyGFRAIQHxjDMnqQAKmiibR.json'}

exec(code, env_args)

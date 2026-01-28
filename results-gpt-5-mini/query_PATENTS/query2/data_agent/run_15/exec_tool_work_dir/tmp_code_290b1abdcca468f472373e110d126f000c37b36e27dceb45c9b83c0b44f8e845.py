code = """import json
import re

# Load the large JSON results from previous query_db calls
with open(var_call_5vp79vJD4mKYJKIDq2qtWdjM, 'r', encoding='utf-8') as f:
    patents = json.load(f)
with open(var_call_4w4xhU9QPi1H6q5mMMdgR7Sn, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build list of level-4 symbols
symbols = [d.get('symbol','').upper() for d in cpc_defs if d.get('symbol')]
# Sort symbols by length descending to prefer longest prefix match
symbols_sorted = sorted(symbols, key=lambda s: len(s), reverse=True)
symbol_to_title = {d.get('symbol','').upper(): d.get('titleFull','') for d in cpc_defs}

# Helper to parse CPC JSON-like field
def parse_cpc_field(cpc_field):
    if not cpc_field:
        return []
    try:
        parsed = json.loads(cpc_field)
        codes = [entry.get('code','').upper() for entry in parsed if isinstance(entry, dict) and entry.get('code')]
        return codes
    except Exception:
        # attempt to extract codes with regex
        return re.findall(r'"code"\s*:\s*"([A-Z0-9/]+)"', cpc_field.upper())

# Helper to find best matching level-4 symbol for a CPC code
def match_symbol(code):
    code_u = code.upper()
    for sym in symbols_sorted:
        if code_u.startswith(sym):
            return sym
    # fallback: try first 3 chars (e.g., 'H01')
    return code_u[:3]

# Extract filing year
year_re = re.compile(r'(19|20)\d{2}')

group_year_counts = {}  # symbol -> {year: count}

for rec in patents:
    cpc_field = rec.get('cpc')
    codes = parse_cpc_field(cpc_field)
    filing_date = rec.get('filing_date','') or ''
    # find year
    m = year_re.search(filing_date)
    if not m:
        # try in Patents_info
        m = year_re.search(rec.get('Patents_info',''))
    if not m:
        # skip if cannot determine filing year
        continue
    year = int(m.group(0))
    # For each code, map to symbol and count
    for code in codes:
        sym = match_symbol(code)
        if not sym:
            continue
        group_year_counts.setdefault(sym, {})
        group_year_counts[sym][year] = group_year_counts[sym].get(year, 0) + 1

# Compute EMA per group per year (alpha=0.1)
alpha = 0.1
results = []
for sym, year_counts in group_year_counts.items():
    # sort years
    years_sorted = sorted(year_counts.keys())
    if not years_sorted:
        continue
    ema_by_year = {}
    prev_ema = None
    for y in years_sorted:
        cnt = year_counts.get(y, 0)
        if prev_ema is None:
            ema = float(cnt)
        else:
            ema = alpha * cnt + (1 - alpha) * prev_ema
        ema_by_year[y] = ema
        prev_ema = ema
    # find year with max ema; if tie choose latest year
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    best_ema = ema_by_year[best_year]
    title = symbol_to_title.get(sym, '')
    results.append({
        'symbol': sym,
        'titleFull': title,
        'best_year': best_year,
        'best_ema': round(best_ema, 6)
    })

# Sort results by best_ema descending
results_sorted = sorted(results, key=lambda r: r['best_ema'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_ybfd6wuFIFGSc0F1GALXr3TZ': 'file_storage/call_ybfd6wuFIFGSc0F1GALXr3TZ.json', 'var_call_5vp79vJD4mKYJKIDq2qtWdjM': 'file_storage/call_5vp79vJD4mKYJKIDq2qtWdjM.json', 'var_call_4w4xhU9QPi1H6q5mMMdgR7Sn': 'file_storage/call_4w4xhU9QPi1H6q5mMMdgR7Sn.json'}

exec(code, env_args)

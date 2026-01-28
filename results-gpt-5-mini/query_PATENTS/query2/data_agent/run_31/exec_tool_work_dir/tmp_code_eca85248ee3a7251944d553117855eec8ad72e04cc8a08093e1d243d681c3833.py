code = """import json
from collections import defaultdict

# Load query results and CPC definitions from storage files
with open(var_call_uZa1YAddL2G235QwVR1W5aTE, 'r', encoding='utf-8') as f:
    records = json.load(f)

with open(var_call_8LtSxg1YgzD2it7B98AppNeW, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from symbol to titleFull for level 4 CPCs
cpc_title = {r['symbol']: r.get('titleFull') for r in cpc_defs}

# Helper to detect German patents in Patents_info
def is_germany(text):
    if not text:
        return False
    t = text.replace(chr(10), ' ').lower()
    checks = [' from de', ' de-', ' de,', ' in de', 'country code de', 'germany']
    for c in checks:
        if c in t:
            return True
    return False

# Helper to extract year from a text by finding first 4-digit number starting with 19 or 20
def extract_year(text):
    if not text:
        return None
    s = text
    n = len(s)
    for i in range(n-3):
        sub = s[i:i+4]
        if sub.isdigit() and (sub.startswith('19') or sub.startswith('20')):
            return int(sub)
    return None

# Helper to parse cpc JSON-like field without using regex
def parse_cpc_field(cpc_field):
    if not cpc_field:
        return []
    try:
        lst = json.loads(cpc_field)
        codes = []
        for entry in lst:
            if isinstance(entry, dict):
                code = entry.get('code')
                if code:
                    codes.append(code)
        return codes
    except Exception:
        s = cpc_field
        codes = []
        key = '"code"'
        idx = 0
        while True:
            i = s.find(key, idx)
            if i == -1:
                break
            colon = s.find(':', i)
            if colon == -1:
                break
            first_q = s.find('"', colon)
            if first_q == -1:
                break
            second_q = s.find('"', first_q+1)
            if second_q == -1:
                break
            val = s[first_q+1:second_q]
            codes.append(val)
            idx = second_q+1
        return codes

# Aggregate counts per CPC level-4 symbol by filing year for German patents granted in H2 2019
alpha = 0.1
counts = defaultdict(lambda: defaultdict(int))

for rec in records:
    info = rec.get('Patents_info', '')
    if not is_germany(info):
        continue
    cpc_field = rec.get('cpc') or rec.get('CPC') or ''
    filing = rec.get('filing_date') or rec.get('Filing_date') or ''
    year = extract_year(filing)
    if year is None:
        year = extract_year(rec.get('grant_date') or '')
    if year is None:
        continue
    codes = parse_cpc_field(cpc_field)
    for code in codes:
        if not code or len(code) < 3:
            continue
        symbol = code[0:3].upper()
        # validate symbol like Letter + 2 digits
        if len(symbol) != 3 or not symbol[0].isalpha() or not symbol[1:].isdigit():
            continue
        counts[symbol][year] += 1

# For each symbol that is present and in level-4 definitions, compute EMA across years and find best year
results = []
for symbol, year_counts in counts.items():
    if symbol not in cpc_title:
        continue
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    first_year = years[0]
    ema = float(year_counts[first_year])
    ema_by_year[first_year] = ema
    for y in years[1:]:
        c = float(year_counts[y])
        ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    best_ema = ema_by_year[best_year]
    results.append({
        'cpc_group_code': symbol,
        'titleFull': cpc_title.get(symbol),
        'best_year': int(best_year),
        'best_ema': round(best_ema, 4)
    })

results.sort(key=lambda x: (-x['best_ema'], x['cpc_group_code']))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_EfRBax6hzCx2UiC0ghQYhdkm': ['publicationinfo'], 'var_call_QR3UjU0wikjaXaQBZgfcgCRB': ['cpc_definition'], 'var_call_G6o6GvXBMro9WbS516sSZ442': 'file_storage/call_G6o6GvXBMro9WbS516sSZ442.json', 'var_call_8LtSxg1YgzD2it7B98AppNeW': 'file_storage/call_8LtSxg1YgzD2it7B98AppNeW.json', 'var_call_uZa1YAddL2G235QwVR1W5aTE': 'file_storage/call_uZa1YAddL2G235QwVR1W5aTE.json'}

exec(code, env_args)

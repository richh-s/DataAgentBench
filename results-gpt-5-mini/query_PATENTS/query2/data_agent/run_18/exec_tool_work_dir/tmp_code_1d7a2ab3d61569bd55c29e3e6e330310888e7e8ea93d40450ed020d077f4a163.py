code = """import json, re
from collections import defaultdict

# Load data
with open('file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open('file_storage/call_iWKlRsPXFz8VehE93rIAy156.json', 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build level-4 mapping
level4_map = {}
for rec in cpc_defs:
    sym = rec.get('symbol')
    lvl_raw = rec.get('level')
    try:
        lvl = int(float(lvl_raw))
    except Exception:
        continue
    if lvl == 4 and sym:
        level4_map[sym] = rec.get('titleFull')

# Helpers
month_map = {
    'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'sept':9,'oct':10,'nov':11,'dec':12
}

def is_germany(pi):
    if not pi:
        return False
    if 'from DE' in pi or 'DE-' in pi:
        return True
    if re.search(r"\bDE\b", pi):
        return True
    return False

def parse_grant_date(s):
    if not s:
        return None
    s_low = s.lower()
    y = re.search(r'(20\d{2})', s_low)
    if not y:
        return None
    year = int(y.group(1))
    m = re.search(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*', s_low)
    month = None
    if m:
        month = month_map.get(m.group(1)[:3])
    num = re.search(r'(\b[0-9]{1,2})\s*(?:st|nd|rd|th)?\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)', s_low)
    if num and not month:
        month = month_map.get(num.group(2)[:3])
    return (year, month)

def parse_year_from_str(s):
    if not s:
        return None
    m = re.search(r'(20\d{2}|19\d{2})', s)
    return int(m.group(1)) if m else None

# Filter pubs: Germany and grant_date in H2 2019
filtered = []
for rec in pubs:
    pi = rec.get('Patents_info','')
    if not is_germany(pi):
        continue
    gd = rec.get('grant_date','')
    parsed = parse_grant_date(gd)
    if not parsed:
        continue
    y, m = parsed
    if y == 2019 and m and 7 <= m <= 12:
        filtered.append(rec)

# Aggregate counts per level-4 CPC per filing year
counts = defaultdict(lambda: defaultdict(int))
for rec in filtered:
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # parse cpc field
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'","\""))
        except Exception:
            continue
    filing_year = parse_year_from_str(rec.get('filing_date','') or rec.get('publication_date',''))
    if not filing_year:
        continue
    for ent in cpcs:
        if isinstance(ent, dict):
            code = ent.get('code')
        else:
            code = None
        if not code:
            continue
        m = re.match(r'([A-Z]\d{2})', code)
        if not m:
            # try first 3 chars
            if len(code) >= 3:
                lvl4 = code[:3]
            else:
                continue
        else:
            lvl4 = m.group(1)
        if lvl4 in level4_map:
            counts[lvl4][filing_year] += 1

# Compute EMA per group (alpha=0.1) and determine best year
alpha = 0.1
results = []
for sym, yc in counts.items():
    years = sorted(yc.keys())
    if not years:
        continue
    ema = None
    emavalues = {}
    for y in years:
        val = yc[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1-alpha) * ema
        emavalues[y] = ema
    best_year = max(emavalues.keys(), key=lambda yy: emavalues[yy])
    results.append({
        'symbol': sym,
        'titleFull': level4_map.get(sym),
        'best_year': int(best_year),
        'peak_ema': round(float(emavalues[best_year]), 4),
        'year_counts': {str(y): int(yc[y]) for y in years}
    })

# Sort by peak_ema desc
results_sorted = sorted(results, key=lambda r: r['peak_ema'], reverse=True)

# Print result JSON
print('__RESULT__:')
print(json.dumps(results_sorted, ensure_ascii=False))"""

env_args = {'var_call_JuYIc5TDnDtRd8TtislB5SI8': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var_call_iWKlRsPXFz8VehE93rIAy156': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json', 'var_call_HJBw0WnBcgg79MIUSqCfldCG': {'var1': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var2': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json'}}

exec(code, env_args)

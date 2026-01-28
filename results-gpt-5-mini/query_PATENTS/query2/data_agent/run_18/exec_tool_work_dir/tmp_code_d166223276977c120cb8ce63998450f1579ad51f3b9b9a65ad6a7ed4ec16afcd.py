code = """import json
import re
from collections import defaultdict, OrderedDict

# Load data from storage paths
with open(var_call_JuYIc5TDnDtRd8TtislB5SI8, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_iWKlRsPXFz8VehE93rIAy156, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build level-4 mapping: symbol -> titleFull
level4_map = {}
for rec in cpc_defs:
    sym = rec.get('symbol')
    try:
        lvl = float(rec.get('level'))
    except Exception:
        try:
            lvl = float(str(rec.get('level')))
        except Exception:
            continue
    if int(lvl) == 4:
        level4_map[sym] = rec.get('titleFull')

# Helper to detect Germany in Patents_info
def is_germany(patents_info):
    if not patents_info:
        return False
    # search for 'DE' as country or 'from DE' or 'DE-' patterns
    if re.search(r"\bDE\b", patents_info):
        return True
    if 'DE-' in patents_info:
        return True
    if 'from DE' in patents_info:
        return True
    return False

# Helper to parse grant_date and return (year, month)
month_map = {
    'jan':1,'january':1,'feb':2,'february':2,'mar':3,'march':3,'apr':4,'april':4,'may':5,'jun':6,'june':6,
    'jul':7,'july':7,'aug':8,'august':8,'sep':9,'sept':9,'september':9,'oct':10,'october':10,'nov':11,'november':11,'dec':12,'december':12
}

def parse_grant_date(s):
    if not s:
        return None
    s_low = s.lower()
    # find year
    myear = re.search(r'(20\d{2})', s)
    if not myear:
        return None
    year = int(myear.group(1))
    # find month name
    mmonth = re.search(r'(?:(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*)', s_low)
    if mmonth:
        month = month_map.get(mmonth.group(1)[:3], None)
    else:
        # try numeric month
        mnum = re.search(r'/(\d{1,2})/(\d{2,4})', s)
        if mnum:
            month = int(mnum.group(1))
        else:
            # no month
            month = None
    return (year, month)

# Helper to parse filing_date year
def parse_filing_year(s):
    if not s:
        return None
    myear = re.search(r'(20\d{2}|19\d{2})', s)
    if myear:
        return int(myear.group(1))
    return None

# Process publications: filter Germany and grant_date in H2 2019 (July-Dec 2019)
filtered = []
for rec in pubs:
    pi = rec.get('Patents_info','')
    if not is_germany(pi):
        continue
    gd = rec.get('grant_date','')
    parsed = parse_grant_date(gd)
    if not parsed:
        continue
    year, month = parsed
    if year == 2019 and month is not None and month >= 7 and month <= 12:
        filtered.append(rec)

# Aggregate counts per level-4 CPC symbol per filing year
counts = defaultdict(lambda: defaultdict(int))
for rec in filtered:
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # parse cpc JSON
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpcs = json.loads(cpc_field.replace("'","\""))
        except Exception:
            continue
    filing_year = parse_filing_year(rec.get('filing_date','') or rec.get('publication_date',''))
    if filing_year is None:
        continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        # level-4 symbol is first 3 chars (letter + two digits)
        m = re.match(r'([A-Z]\d{2})', code)
        if not m:
            continue
        lvl4 = m.group(1)
        # only consider if lvl4 in level4_map
        if lvl4 in level4_map:
            counts[lvl4][filing_year] += 1

# For each group compute EMA across years
alpha = 0.1
results = []
for sym, year_counts in counts.items():
    # sort years asc
    years = sorted(year_counts.keys())
    if not years:
        continue
    emavalues = {}
    ema = None
    for y in years:
        val = year_counts[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1-alpha) * ema
        emavalues[y] = ema
    # find year with max ema
    best_year = max(emavalues.keys(), key=lambda yy: emavalues[yy])
    peak_ema = emavalues[best_year]
    results.append({
        'symbol': sym,
        'titleFull': level4_map.get(sym),
        'best_year': int(best_year),
        'peak_ema': round(float(peak_ema), 4),
        'years': {str(y): int(year_counts[y]) for y in years}
    })

# Sort results by peak_ema descending
results_sorted = sorted(results, key=lambda r: r['peak_ema'], reverse=True)

# Output JSON string
out = json.dumps(results_sorted, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_JuYIc5TDnDtRd8TtislB5SI8': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var_call_iWKlRsPXFz8VehE93rIAy156': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json'}

exec(code, env_args)

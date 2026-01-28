code = """import json
import re
from collections import defaultdict

# Load data from storage files
pub_path = var_call_ntCBtWEpc82CqtOSe20HUEFm
cpcdef_path = var_call_klpZTbzFCPMJk9CaIW0AMgp3
with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(cpcdef_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build set and mapping for level-4 CPC symbols to titleFull
level4_map = {rec['symbol']: rec.get('titleFull','') for rec in cpc_defs}
level4_symbols = sorted(level4_map.keys(), key=lambda x: -len(x))  # sort by length desc for matching

# Month mapping
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'sept':9,'oct':10,'nov':11,'dec':12}

# Helper to extract year and month
def extract_year_month(date_str):
    if not date_str or not isinstance(date_str, str):
        return None, None
    s = date_str.lower()
    # year
    y_match = re.search(r'(20\d{2}|19\d{2})', s)
    year = int(y_match.group(0)) if y_match else None
    # month
    m = None
    for k,v in months.items():
        if k in s:
            m = v
            break
    return year, m

# Helper to find country code in Patents_info (look for ' from XX' or '\bXX\b')
def has_country_de(info):
    if not info or not isinstance(info, str):
        return False
    if re.search(r'\bDE\b', info):
        return True
    if 'from de' in info.lower():
        return True
    return False

# Helper to parse cpc JSON string
def parse_cpc(cpc_field):
    if not cpc_field or not isinstance(cpc_field, str):
        return []
    try:
        arr = json.loads(cpc_field)
        codes = [entry.get('code') for entry in arr if isinstance(entry, dict) and entry.get('code')]
        return codes
    except Exception:
        # try to find codes via regex
        return re.findall(r'"code"\s*:\s*"([A-Z0-9/]+)"', cpc_field)

# Filter patents: granted in H2 2019 and in Germany
filtered = []
for rec in pubs:
    grant = rec.get('grant_date','')
    gy, gm = extract_year_month(grant)
    if gy != 2019 or (gm is None) or gm < 7:
        continue
    if not has_country_de(rec.get('Patents_info','')):
        continue
    filtered.append(rec)

# Aggregate counts by level-4 symbol and filing year
counts = defaultdict(lambda: defaultdict(int))  # counts[symbol][year]=count
for rec in filtered:
    cpc_codes = parse_cpc(rec.get('cpc',''))
    # filing year
    fy, _ = extract_year_month(rec.get('filing_date',''))
    if fy is None:
        continue
    for code in cpc_codes:
        if not code: 
            continue
        # normalize code: remove leading/trailing spaces
        code = code.strip()
        matched = None
        for sym in level4_symbols:
            if code.startswith(sym):
                matched = sym
                break
        if not matched:
            # fallback: take prefix up to first non-alphanum or slash
            m = re.match(r'([A-Z]\d{1,2}[A-Z]?)', code)
            if m:
                matched = m.group(1)
            else:
                matched = code.split('/')[0]
        counts[matched][fy] += 1

# Compute EMA for each symbol across years
alpha = 0.1
results = []
for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    miny, maxy = years[0], years[-1]
    # build full series from miny to maxy
    series_years = list(range(miny, maxy+1))
    series_counts = [year_counts.get(y, 0) for y in series_years]
    # compute EMA
    emas = []
    ema = series_counts[0]
    emas.append(ema)
    for x in series_counts[1:]:
        ema = alpha * x + (1 - alpha) * ema
        emas.append(ema)
    # find year with max ema
    max_idx = max(range(len(emas)), key=lambda i: emas[i])
    best_year = series_years[max_idx]
    max_ema = emas[max_idx]
    title = level4_map.get(sym, '')
    # prepare per-year details
    per_year = [{'year': y, 'count': year_counts.get(y,0), 'ema': round(emas[i],6)} for i,y in enumerate(series_years)]
    results.append({'symbol': sym, 'titleFull': title, 'best_year': best_year, 'max_ema': round(max_ema,6), 'series': per_year})

# Sort results by max_ema descending
results = sorted(results, key=lambda r: r['max_ema'], reverse=True)

# Output JSON-serializable string
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_ntCBtWEpc82CqtOSe20HUEFm': 'file_storage/call_ntCBtWEpc82CqtOSe20HUEFm.json', 'var_call_klpZTbzFCPMJk9CaIW0AMgp3': 'file_storage/call_klpZTbzFCPMJk9CaIW0AMgp3.json'}

exec(code, env_args)

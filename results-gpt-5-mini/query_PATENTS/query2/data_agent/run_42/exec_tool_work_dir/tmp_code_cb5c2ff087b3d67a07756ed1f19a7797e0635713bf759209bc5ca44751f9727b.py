code = """import json
import re
from collections import defaultdict

# Load data from stored JSON files
with open(var_call_jxd71DdOVzdJ2O10XjcH3bnt, 'r') as f:
    pubs = json.load(f)
with open(var_call_mieqchfCaxujLt1RPfRt1CIg, 'r') as f:
    cpc_defs = json.load(f)

# Build mapping from symbol to titleFull for level 4
cpc_title = {}
for d in cpc_defs:
    sym = d.get('symbol')
    title = d.get('titleFull')
    lvl = d.get('level')
    # Normalize level to str and check startswith '4'
    if sym and title and str(lvl).startswith('4'):
        cpc_title[sym] = title

# helper to detect DE in Patents_info
def is_germany(patents_info):
    if not patents_info:
        return False
    s = patents_info.upper()
    # look for patterns like 'FROM DE', 'DE-', 'DE,' or '(NO. DE-' etc.
    if ' FROM DE' in s or ' DE,' in s or ' DE)' in s or 'DE-' in s or ' COUNTRY CODE: DE' in s:
        return True
    # also check for 'ASSIGNED TO ... (DE)'
    if re.search(r'\bDE\b', s):
        return True
    return False

# month mapping
months = {
    'JAN':1,'JANUARY':1,
    'FEB':2,'FEBRUARY':2,
    'MAR':3,'MARCH':3,
    'APR':4,'APRIL':4,
    'MAY':5,
    'JUN':6,'JUNE':6,
    'JUL':7,'JULY':7,
    'AUG':8,'AUGUST':8,
    'SEP':9,'SEPT':9,'SEPTEMBER':9,
    'OCT':10,'OCTOBER':10,
    'NOV':11,'NOVEMBER':11,
    'DEC':12,'DECEMBER':12
}

# function to extract month number from grant_date text
def extract_month(grant_date):
    if not grant_date:
        return None
    s = grant_date.upper()
    for name, num in months.items():
        if name in s:
            return num
    # try numeric month
    m = re.search(r"(\d{1,2})[stndrth]*\s+(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)", s)
    if m:
        return months.get(m.group(2), None)
    return None

# parse cpc field (JSON-like)
def parse_cpc_field(cpc_text):
    if not cpc_text:
        return []
    try:
        arr = json.loads(cpc_text)
        codes = [item.get('code') for item in arr if item.get('code')]
        return codes
    except Exception:
        # try to extract codes by regex
        codes = re.findall(r'"([A-Z]\d{2}[A-Z]?)\d*/?[^\",\s]*', cpc_text)
        return codes

# Iterate over publications, filter for Germany and grant_date in second half of 2019
filtered = []
for p in pubs:
    pi = p.get('Patents_info','')
    if not is_germany(pi):
        continue
    gd = p.get('grant_date','')
    if '2019' not in str(gd):
        continue
    month = extract_month(gd)
    if not month:
        continue
    if month < 7 or month > 12:
        continue
    # parse filing year
    fd = p.get('filing_date','')
    m = re.search(r"(19|20)\d{2}", str(fd))
    if not m:
        continue
    filing_year = int(m.group(0))
    # parse cpc codes
    codes = parse_cpc_field(p.get('cpc'))
    if not codes:
        continue
    filtered.append({'filing_year': filing_year, 'cpc_codes': codes, 'Patents_info': pi})

# Build counts per level4 code per year
counts = defaultdict(lambda: defaultdict(int))
for rec in filtered:
    year = rec['filing_year']
    codes = rec['cpc_codes']
    # Use unique codes per patent to avoid double counting same code twice
    unique_codes = set(codes)
    for code in unique_codes:
        if not code or len(code) < 3:
            continue
        lvl4 = code[:3]
        counts[lvl4][year] += 1

# Compute EMA per year for each lvl4 with alpha=0.1
alpha = 0.1
results = []
for lvl4, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    ema = None
    for y in years:
        val = year_counts[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    peak_ema = ema_by_year[best_year]
    results.append({
        'cpc_group': lvl4,
        'titleFull': cpc_title.get(lvl4, None),
        'best_year': int(best_year),
        'peak_ema': round(float(peak_ema), 4)
    })

# sort results by peak_ema descending
results_sorted = sorted(results, key=lambda x: x['peak_ema'], reverse=True)

# Print required result in the exact print format
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_YrJ4PmtDIGn8fm5wgvUyHZ5p': ['publicationinfo'], 'var_call_8bEC03tRx1pXPiWaQ3SwWAR2': ['cpc_definition'], 'var_call_mieqchfCaxujLt1RPfRt1CIg': 'file_storage/call_mieqchfCaxujLt1RPfRt1CIg.json', 'var_call_jxd71DdOVzdJ2O10XjcH3bnt': 'file_storage/call_jxd71DdOVzdJ2O10XjcH3bnt.json'}

exec(code, env_args)

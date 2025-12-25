code = """import json
import re
from datetime import datetime

# Load data
file_path = locals()['var_function-call-18415164886367726200']
with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str: return None
    # normalize
    s = date_str.lower().replace(',', '').replace('dated', '').replace('on', '').replace('the', '').strip()
    # Remove ordinal suffixes (st, nd, rd, th)
    s = re.sub(r'(?<=\d)(st|nd|rd|th)', '', s)
    
    # Formats to try:
    # "14 mar 2019", "2019 jul 12", "6 october 2020", "2013 june 17"
    formats = [
        "%d %b %Y", "%Y %b %d", "%d %B %Y", "%Y %B %d"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None

def is_h2_2019(d):
    if not d: return False
    return d.year == 2019 and d.month >= 7

valid_patents = []
for p in data:
    # Filter Country
    # Check Patents_info for DE
    # "Patent application ... from DE..." or "DE-..."
    # The SQL filter was broad. Let's look for country code indicators.
    info = p.get('Patents_info', '')
    # Check if 'DE' is the country code. Usually "from DE" or "Application ... from DE" or publication starting with "DE"
    # Or "Patent application (no. DE-..."
    is_de = False
    if 'from DE' in info or 'assigned to' in info: # 'from DE' is a good indicator
        pass
    
    # Let's rely on regex for Country Code
    # Looking for patterns like "from DE", "application ... DE-..."
    if re.search(r'\bfrom DE\b', info) or re.search(r'application \(no\. DE-', info) or re.search(r'publication (no\.|number) DE-', info):
        is_de = True
    
    if not is_de:
        continue

    # Filter Grant Date
    g_date = parse_date(p.get('grant_date'))
    if not is_h2_2019(g_date):
        continue
    
    # Get Filing Year
    f_date = parse_date(p.get('filing_date'))
    if not f_date:
        continue
    
    # Get CPCs
    cpc_json = p.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
    
    codes = set()
    for item in cpcs:
        code = item.get('code', '')
        if len(code) >= 3:
            codes.add(code[:3]) # Level 4 is 3 chars (e.g. A01)
            
    if codes:
        valid_patents.append({
            'year': f_date.year,
            'cpcs': list(codes)
        })

# Aggregate
counts = {} # {cpc: {year: count}}
all_years = set()

for p in valid_patents:
    y = p['year']
    all_years.add(y)
    for c in p['cpcs']:
        if c not in counts:
            counts[c] = {}
        counts[c][y] = counts[c].get(y, 0) + 1

if not counts:
    print('__RESULT__:')
    print(json.dumps([]))
    exit()

min_year = min(all_years)
max_year = max(all_years)
sorted_years = sorted(range(min_year, max_year + 1))

# Calculate EMA
# Alpha = 0.1
# For each CPC, calculate EMA series.
alpha = 0.1
cpc_emas = {} # {cpc: {year: ema}}

for cpc, year_counts in counts.items():
    ema_series = {}
    previous_ema = None
    
    # We need to iterate through all years to maintain the series?
    # Or just start from the first year the CPC appears?
    # Usually EMA is continuous. If a year has 0 filings, it pulls the EMA down.
    # So we iterate from min_year (or first year of CPC?) to max_year.
    # Let's iterate from min_year of the whole dataset to max_year.
    
    # To avoid dragging near-zero values from long ago, maybe start from the first year *any* patent in the set was filed?
    # Yes, sorted_years covers the range of the dataset.
    
    # Optimization: Find first year for this CPC?
    # If we start from global min_year, and CPC has 0, EMA stays 0.
    # If we start from first appearance, it's different.
    # "highest exponential moving average of patent filings each year" implies comparing CPCs in a given year.
    # So they should be comparable. 
    # Let's assume 0 for years before first appearance? Or iterate global range.
    
    # Logic:
    # EMA_t = alpha * Count_t + (1-alpha) * EMA_{t-1}
    # For t=0 (first year in range), EMA_0 = Count_0 (if we assume EMA_{-1} is 0 or undefined, typically initialized to first observation).
    
    current_ema = None
    for y in sorted_years:
        cnt = year_counts.get(y, 0)
        if current_ema is None:
            # Check if we should start?
            # If we strictly follow the formula and initialize with first value:
            # If cnt is 0 and we haven't started, EMA is 0.
            current_ema = cnt
        else:
            current_ema = alpha * cnt + (1 - alpha) * current_ema
        
        ema_series[y] = current_ema
    
    cpc_emas[cpc] = ema_series

# Find highest EMA each year
# We want to identify CPCs that are "winners" in at least one year.
# But we also want "the best year for each CPC group".
# The query phrasing "Find the CPC ... with the highest ... each year"
# probably means:
# Return the list of CPCs which had the highest EMA in at least one year.
# For each of those, show its best year.

winners = set()
for y in sorted_years:
    # Find max EMA in year y
    best_cpc = None
    max_val = -1
    for cpc, series in cpc_emas.items():
        val = series.get(y, 0)
        if val > max_val:
            max_val = val
            best_cpc = cpc
    
    if best_cpc:
        winners.add(best_cpc)

# Prepare result info
# We need to return the codes so we can query titles.
# Also return their best year.

final_list = []
for cpc in winners:
    # Find best year for this CPC
    series = cpc_emas[cpc]
    best_y = None
    max_v = -1
    for y, v in series.items():
        if v > max_v:
            max_v = v
            best_y = y
    
    final_list.append({
        "code": cpc,
        "best_year": best_y,
        "max_ema": max_v # informative
    })

print('__RESULT__:')
print(json.dumps(final_list))"""

env_args = {'var_function-call-13721774658737760568': 'file_storage/function-call-13721774658737760568.json', 'var_function-call-9307426392161200507': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_function-call-18415164886367725303': [{'symbol': 'B99', 'level': '4.0'}, {'symbol': 'B29', 'level': '4.0'}, {'symbol': 'B33', 'level': '4.0'}, {'symbol': 'C22', 'level': '4.0'}, {'symbol': 'D99', 'level': '4.0'}, {'symbol': 'F28', 'level': '4.0'}, {'symbol': 'B', 'level': '2.0'}, {'symbol': 'H', 'level': '2.0'}, {'symbol': 'Y', 'level': '2.0'}, {'symbol': 'D', 'level': '2.0'}, {'symbol': 'F', 'level': '2.0'}, {'symbol': 'E', 'level': '2.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'G', 'level': '2.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A45', 'level': '4.0'}, {'symbol': 'A24', 'level': '4.0'}, {'symbol': 'A61', 'level': '4.0'}, {'symbol': 'A63', 'level': '4.0'}, {'symbol': 'A22', 'level': '4.0'}], 'var_function-call-18415164886367726200': 'file_storage/function-call-18415164886367726200.json'}

exec(code, env_args)

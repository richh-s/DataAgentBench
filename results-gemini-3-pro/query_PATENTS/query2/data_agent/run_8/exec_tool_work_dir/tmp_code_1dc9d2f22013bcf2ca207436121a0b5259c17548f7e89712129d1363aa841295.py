code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data
file_path = locals()['var_function-call-16013154277933524664']
with open(file_path, 'r') as f:
    data = json.load(f)

# Helper to parse date
def parse_date(date_str):
    if not date_str:
        return None
    # Try generic parsing logic using regex for years and months
    # Formats: "14th Mar 2019", "2019 on Jul 12th", "dated 8th October 2019", "March the 18th, 2019"
    # Extract year
    year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Extract month
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    month = 1 # default
    lower_str = date_str.lower()
    for m, num in months.items():
        if m in lower_str:
            month = num
            break
            
    # Extract day
    day_match = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', date_str)
    day = int(day_match.group(1)) if day_match else 1
    
    try:
        return datetime(year, month, day)
    except:
        return None

# Filter
filtered_patents = []
for p in data:
    # Grant Date
    g_date = parse_date(p.get('grant_date', ''))
    if not g_date:
        continue
    if not (datetime(2019, 7, 1) <= g_date <= datetime(2019, 12, 31)):
        continue
        
    # Country: Germany
    # Check Patents_info
    p_info = p.get('Patents_info', '')
    # Logic: Look for DE indicators
    # Examples: "from DE", "DE patent", "DE-..."
    is_de = False
    if re.search(r'\bfrom DE\b', p_info, re.IGNORECASE):
        is_de = True
    elif re.search(r'\bDE patent\b', p_info, re.IGNORECASE):
        is_de = True
    elif re.search(r'DE-\d+', p_info):
        is_de = True
    elif 'assigned to' in p_info and 'DE' in p_info: # Heuristic
        # "Patent application ... from DE, assigned to IBM" -> Handled by "from DE"
        pass
        
    if not is_de:
        continue
        
    # Filing Date
    f_date = parse_date(p.get('filing_date', ''))
    if not f_date:
        continue
    filing_year = f_date.year
    
    # CPC
    cpc_json = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract Level 4 codes (Classes, 3 chars)
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            # Level 4 is usually the Class (e.g., A01)
            codes.add(code[:3])
            
    filtered_patents.append({
        'filing_year': filing_year,
        'cpc_codes': list(codes)
    })

# Aggregation: Count filings per CPC per Year
# Counts: {cpc: {year: count}}
counts = {}
for p in filtered_patents:
    yr = p['filing_year']
    for code in p['cpc_codes']:
        if code not in counts:
            counts[code] = {}
        counts[code][yr] = counts[code].get(yr, 0) + 1

# Calculate EMA
results = []
smoothing_factor = 0.1

for code, year_counts in counts.items():
    if not year_counts:
        continue
    years = sorted(year_counts.keys())
    # Fill missing years? 
    # Usually EMA is time-series. If no filings in a year, count is 0.
    # We should cover the range from min_year to max_year.
    min_year = years[0]
    max_year = years[-1]
    
    ema = None
    best_ema = -1
    best_year = None
    
    # Iterate through all years in range
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        if ema is None:
            ema = val
        else:
            ema = val * smoothing_factor + ema * (1 - smoothing_factor)
            
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    results.append({
        'cpc_code': code,
        'best_ema': best_ema,
        'best_year': best_year
    })

# Sort by best_ema descending
results.sort(key=lambda x: x['best_ema'], reverse=True)

# Output top results (Top 20 to be safe, then I'll query titles)
top_results = results[:20]

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-7596832698006438446': 'file_storage/function-call-7596832698006438446.json', 'var_function-call-15018955197929013117': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-10909241304662770037': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-9645515799168749745': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-857415788462902268': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}], 'var_function-call-16013154277933524664': 'file_storage/function-call-16013154277933524664.json'}

exec(code, env_args)

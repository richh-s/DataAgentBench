code = """import json
import re
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-14548752436024943433'], 'r') as f:
    data = json.load(f)

# Helper to parse date
month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_date(date_str):
    if not date_str or date_str.lower() == 'none date':
        return None
    # Find year
    year_match = re.search(r'\d{4}', date_str)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Find month
    month = 1
    lower_str = date_str.lower()
    for m_name, m_val in month_map.items():
        if m_name in lower_str:
            month = m_val
            break
            
    # Find day (optional, default 1)
    day = 1
    # specific case like "3rd August"
    # regex for day
    day_match = re.search(r'(\d{1,2})(st|nd|rd|th)?', lower_str)
    if day_match:
        # Avoid matching the year digits if they appear first without context, 
        # but usually dates are like "3rd August 2021"
        # We need to be careful not to pick "20" from "2021".
        # Let's iterate matches and pick one that is <= 31 and not part of year
        pass 
        # Simplified: just use month/year for filtering 2nd half 2019
    
    return year, month

# Filter and Extract
cpc_years = {} # {cpc_code: [year1, year2, ...]}

for row in data:
    g_date = row.get('grant_date')
    if not g_date: continue
    parsed_g = parse_date(g_date)
    if not parsed_g: continue
    gy, gm = parsed_g
    
    # Filter 2nd half 2019
    # July (7) to Dec (12) 2019
    if not (gy == 2019 and 7 <= gm <= 12):
        continue
        
    # Extract Filing Year
    f_date = row.get('filing_date')
    if not f_date: continue
    parsed_f = parse_date(f_date)
    if not parsed_f: continue
    fy, _ = parsed_f
    
    # Extract CPCs
    cpc_json = row.get('cpc')
    if not cpc_json: continue
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    for item in cpc_list:
        code = item.get('code')
        if not code: continue
        # Truncate to Level 4 (Class: first 3 chars, e.g., A01)
        # Verify if length >= 3
        if len(code) >= 3:
            class_code = code[:3]
            if class_code not in cpc_years:
                cpc_years[class_code] = []
            cpc_years[class_code].append(fy)

# Calculate EMA
results = []
alpha = 0.1

for code, years in cpc_years.items():
    if not years: continue
    years.sort()
    min_y = years[0]
    max_y = years[-1]
    
    # Create time series
    timeline = range(min_y, max_y + 1)
    counts = {y: 0 for y in timeline}
    for y in years:
        counts[y] += 1
        
    # Calculate EMA
    ema = 0
    max_ema = -1
    best_year = -1
    
    # Initialize EMA with the first year count (or 0?)
    # Usually EMA_0 = x_0
    
    first_year = True
    for y in timeline:
        val = counts[y]
        if first_year:
            ema = val
            first_year = False
        else:
            ema = alpha * val + (1 - alpha) * ema
            
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({
        "code": code,
        "max_ema": max_ema,
        "best_year": best_year
    })

# Sort by Max EMA descending
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Top 10
top_results = results[:10]
print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-2642235068750226614': 'file_storage/function-call-2642235068750226614.json', 'var_function-call-13383852175064337644': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'grant_date': 'None Date'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'grant_date': 'September the 6th, 2012'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'grant_date': 'None Date'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.', 'grant_date': '16th Mar 2017'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.', 'grant_date': 'None Date'}], 'var_function-call-13383852175064337963': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-15737899095710788599': [{'level': '5.0', 'symbol': 'A01B'}, {'level': '7.0', 'symbol': 'A01B59/00'}, {'level': '7.0', 'symbol': 'A01B19/00'}, {'level': '7.0', 'symbol': 'A01B35/00'}, {'level': '7.0', 'symbol': 'A01B13/00'}, {'level': '7.0', 'symbol': 'A01B67/00'}, {'level': '7.0', 'symbol': 'A01B76/00'}, {'level': '7.0', 'symbol': 'A01B37/00'}, {'level': '7.0', 'symbol': 'A01B47/00'}, {'level': '7.0', 'symbol': 'A01B79/00'}], 'var_function-call-15737899095710786440': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-10037366570945794187': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}], 'var_function-call-14548752436024943433': 'file_storage/function-call-14548752436024943433.json'}

exec(code, env_args)

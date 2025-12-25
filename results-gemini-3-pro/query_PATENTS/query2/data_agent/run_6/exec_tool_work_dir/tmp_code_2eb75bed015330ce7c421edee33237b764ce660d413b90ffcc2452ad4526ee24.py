code = """import json
import re
import datetime

# Load the data
filename = locals()['var_function-call-8428725844076895982']
with open(filename, 'r') as f:
    data = json.load(f)

# Date parser
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
    'Sept': 9
}

def parse_date(date_str):
    if not date_str or date_str == "None Date":
        return None
    
    s = date_str.lower().replace(',', ' ').replace('dated', '').replace(' on ', ' ').replace(' of ', ' ').replace(' the ', ' ')
    
    # Year
    year_match = re.search(r'\b(19|20)\d{2}\b', s)
    if not year_match:
        return None
    year = int(year_match.group(0))
    
    # Month
    month = None
    for m_name, m_val in month_map.items():
        if m_name.lower() in s:
            month = m_val
            break
    if not month:
        return None
        
    # Day
    day_match = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', s)
    day = 1
    if day_match:
        d_cand = int(day_match.group(1))
        if d_cand <= 31:
            day = d_cand
            
    try:
        return datetime.date(year, month, day)
    except:
        return None

# Process
target_cpcs = set()
cpc_years = {} # {cpc: {year: count}}

for row in data:
    g_date = parse_date(row.get('grant_date'))
    f_date = parse_date(row.get('filing_date'))
    
    # Check if grant date in H2 2019 (2019-07-01 to 2019-12-31)
    is_target = False
    if g_date and g_date.year == 2019 and g_date.month >= 7:
        is_target = True
        
    # Extract CPCs
    try:
        cpc_list = json.loads(row.get('cpc', '[]'))
    except:
        cpc_list = []
        
    current_cpcs = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            lvl4 = code[:3]
            current_cpcs.add(lvl4)
            
    if is_target:
        target_cpcs.update(current_cpcs)
        
    if f_date:
        yr = f_date.year
        for c in current_cpcs:
            if c not in cpc_years:
                cpc_years[c] = {}
            cpc_years[c][yr] = cpc_years[c].get(yr, 0) + 1

# Calculate EMA
results_list = []
alpha = 0.1

for cpc in target_cpcs:
    if cpc not in cpc_years:
        continue
        
    years = sorted(cpc_years[cpc].keys())
    if not years:
        continue
        
    min_year = years[0]
    max_year = years[-1]
    
    ema = 0
    max_ema = -1
    best_year = -1
    
    # S_0 = first data point
    current_ema = cpc_years[cpc].get(min_year, 0)
    if current_ema > max_ema:
        max_ema = current_ema
        best_year = min_year
        
    for y in range(min_year + 1, max_year + 1):
        count = cpc_years[cpc].get(y, 0)
        current_ema = alpha * count + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    results_list.append({
        "cpc": cpc,
        "max_ema": max_ema,
        "best_year": best_year
    })

results_list.sort(key=lambda x: x['max_ema'], reverse=True)
top_results = results_list[:15] # Get top 15

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-1888771270792040030': ['publicationinfo'], 'var_function-call-6434570943978445363': 'file_storage/function-call-6434570943978445363.json', 'var_function-call-15179652926461999085': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-10764568967162063911': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}], 'var_function-call-8139530506660812023': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'grant_date': 'None Date'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'grant_date': 'September the 6th, 2012'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'grant_date': 'None Date'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.', 'grant_date': '16th Mar 2017'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.', 'grant_date': 'None Date'}], 'var_function-call-4097148127731783155': [{'symbol': 'H04', 'level': '4.0'}], 'var_function-call-1604636425446054396': [{'COUNT(*)': '277813'}], 'var_function-call-8428725844076895982': 'file_storage/function-call-8428725844076895982.json'}

exec(code, env_args)

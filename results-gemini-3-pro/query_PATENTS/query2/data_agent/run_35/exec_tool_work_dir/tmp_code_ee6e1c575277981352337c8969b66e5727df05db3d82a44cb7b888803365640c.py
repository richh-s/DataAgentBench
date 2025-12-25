code = """import pandas as pd
import json
import re

# Load data
file_path = locals()['var_function-call-10259991882588028232']
with open(file_path, 'r') as f:
    data = json.load(f)

# Helper to parse date
def parse_date(date_str):
    if not date_str:
        return None
    # Remove common prefixes
    s = date_str.lower()
    s = s.replace("dated ", "").replace("on ", "").replace("of ", "").replace("the ", "").replace(",", " ")
    # Remove ordinals: 1st, 2nd, 3rd, 4th... 
    # Regex to remove st, nd, rd, th following a digit
    s = re.sub(r'(?<=\d)(st|nd|rd|th)', '', s)
    try:
        dt = pd.to_datetime(s)
        return dt
    except:
        return None

# Filter and aggregate
cpc_filings = {} # {cpc: {year: count}}

filtered_count = 0

for row in data:
    g_date = parse_date(row.get('grant_date'))
    f_date = parse_date(row.get('filing_date'))
    
    if g_date is None or f_date is None:
        continue
        
    # Filter H2 2019 (July 1 to Dec 31)
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue
    
    # Country check (redundant if SQL was correct, but good to ensure)
    p_info = row.get('Patents_info', '')
    if not ('DE-' in p_info or 'Germany' in p_info or 'In DE' in p_info or 'from DE' in p_info):
        continue

    filtered_count += 1
    
    f_year = f_date.year
    
    # CPC processing
    cpc_json = row.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
        
    # Get Level 4 codes (first 3 chars)
    # Use a set to avoid double counting same patent for same group
    groups = set()
    for c in cpcs:
        code = c.get('code', '')
        if len(code) >= 3:
            groups.add(code[:3])
            
    for g in groups:
        if g not in cpc_filings:
            cpc_filings[g] = {}
        cpc_filings[g][f_year] = cpc_filings[g].get(f_year, 0) + 1

# Calculate EMA
alpha = 0.1
results = []

for cpc, year_counts in cpc_filings.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # Fill gaps with 0
    full_years = range(min_year, max_year + 1)
    
    ema = 0
    # Initialize with first data point? Or 0?
    # Standard EMA definition often starts with SMA or first value.
    # "S_1 = Y_1"
    
    first = True
    max_ema = -1
    best_year = -1
    
    current_ema = 0
    
    for y in full_years:
        count = year_counts.get(y, 0)
        if first:
            current_ema = count # Initialize with first value
            first = False
        else:
            current_ema = alpha * count + (1 - alpha) * current_ema
            
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    results.append({
        "cpc": cpc,
        "max_ema": max_ema,
        "best_year": best_year,
        "filings_count": sum(year_counts.values()) # Total filings in this set
    })

# Sort by max_ema desc
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Top 10
top_results = results[:10]

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-5268517143288070947': 'file_storage/function-call-5268517143288070947.json', 'var_function-call-11072829234895583322': ['publicationinfo'], 'var_function-call-3335259452664848175': ['cpc_definition'], 'var_function-call-17082653395440709490': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-5081634979425652625': [{'count(*)': '68'}], 'var_function-call-826692456356397778': [{'count(*)': '277813'}], 'var_function-call-15036074897345034399': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-12066266825491602075': [{'count(*)': '4833'}], 'var_function-call-10259991882588028232': 'file_storage/function-call-10259991882588028232.json', 'var_function-call-17735670244887518063': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-9041763067788198491': [{'symbol': 'B', 'level': '2.0'}, {'symbol': 'B04B', 'level': '5.0'}, {'symbol': 'B04B1/00', 'level': '7.0'}, {'symbol': 'B04', 'level': '4.0'}], 'var_function-call-7284749001237528506': [{'symbol': 'G06', 'level': '4.0'}]}

exec(code, env_args)

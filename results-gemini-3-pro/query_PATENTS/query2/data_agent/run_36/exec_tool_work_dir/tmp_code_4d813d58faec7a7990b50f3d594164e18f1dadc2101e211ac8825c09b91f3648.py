code = """import json
import pandas as pd
import re

# Load data
with open('var_function-call-2682890762204433757.json', 'r') as f:
    data = json.load(f)

def parse_date(d_str):
    if not isinstance(d_str, str): return None
    # Remove common prefixes
    clean = re.sub(r'(?i)\b(?:dated|on|of|the)\b', '', d_str)
    # Remove ordinal suffixes
    clean = re.sub(r'(\d+)(?:st|nd|rd|th)', r'\1', clean)
    # Remove extra spaces and commas
    clean = clean.replace(',', ' ').strip()
    # Normalize spaces
    clean = re.sub(r'\s+', ' ', clean)
    try:
        return pd.to_datetime(clean)
    except:
        return None

cpc_years = {}

for row in data:
    g_date = parse_date(row.get('grant_date'))
    if g_date is None: continue
    
    # Filter H2 2019 (July 1 to Dec 31)
    if g_date.year != 2019 or g_date.month < 7:
        continue
        
    f_date = parse_date(row.get('filing_date'))
    if f_date is None: continue
    year = f_date.year
    
    cpc_json = row.get('cpc')
    if not cpc_json: continue
    try:
        cpcs = json.loads(cpc_json)
        # Unique Level 4 codes (first 3 chars)
        codes = set()
        for c in cpcs:
            code = c.get('code', '')
            if len(code) >= 3:
                codes.add(code[:3])
        
        for code in codes:
            if code not in cpc_years:
                cpc_years[code] = {}
            cpc_years[code][year] = cpc_years[code].get(year, 0) + 1
            
    except:
        continue

results = []

for cpc, year_counts in cpc_years.items():
    years = sorted(year_counts.keys())
    if not years: continue
    
    min_y = years[0]
    max_y = years[-1]
    
    ema = 0
    max_ema = -1
    best_year = None
    
    first = True
    for y in range(min_y, max_y + 1):
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = 0.1 * count + 0.9 * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({
        'cpc_group': cpc,
        'best_year': best_year,
        'max_ema': max_ema
    })

# Sort by max_ema descending
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Keep top results. 
# There might be many with similar values.
# Let's keep top 10.
top_results = results[:10]

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-2465763669392206693': 'file_storage/function-call-2465763669392206693.json', 'var_function-call-10552974933409371808': [{'count(*)': '277813'}], 'var_function-call-12947090445961145540': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-7723433747525131136': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-5457342836447626573': [{'level': '2.0', 'symbol': 'A'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}, {'level': '4.0', 'symbol': 'A47'}, {'level': '4.0', 'symbol': 'A61'}, {'level': '4.0', 'symbol': 'A62'}, {'level': '4.0', 'symbol': 'A63'}, {'level': '4.0', 'symbol': 'A99'}, {'level': '5.0', 'symbol': 'A01B'}, {'level': '5.0', 'symbol': 'A01C'}, {'level': '5.0', 'symbol': 'A01D'}], 'var_function-call-8858317480294281354': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-2682890762204433757': 'file_storage/function-call-2682890762204433757.json'}

exec(code, env_args)

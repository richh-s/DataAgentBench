code = """import json
import pandas as pd
import re

filename = locals()['var_function-call-2682890762204433757']
with open(filename, 'r') as f:
    data = json.load(f)

def clean_date_str(d_str):
    if not isinstance(d_str, str): return ""
    s = re.sub(r'(\d+)(?:st|nd|rd|th)', lambda m: m.group(1), d_str, flags=re.IGNORECASE)
    s = re.sub(r'(?i)\b(dated|on|of|the)\b', '', s)
    s = s.replace(',', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

cpc_years = {}

for row in data:
    g_raw = row.get('grant_date')
    g_clean = clean_date_str(g_raw)
    try:
        g_date = pd.to_datetime(g_clean)
    except:
        continue
        
    if g_date.year != 2019 or g_date.month < 7:
        continue
    
    f_raw = row.get('filing_date')
    f_clean = clean_date_str(f_raw)
    try:
        f_date = pd.to_datetime(f_clean)
        year = f_date.year
    except:
        continue

    cpc_json = row.get('cpc')
    if not cpc_json: continue
    try:
        cpcs = json.loads(cpc_json)
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
            
    results.append({'cpc_group': cpc, 'best_year': best_year, 'max_ema': max_ema})

results.sort(key=lambda x: x['max_ema'], reverse=True)
top_results = results[:20]

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-2465763669392206693': 'file_storage/function-call-2465763669392206693.json', 'var_function-call-10552974933409371808': [{'count(*)': '277813'}], 'var_function-call-12947090445961145540': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-7723433747525131136': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-5457342836447626573': [{'level': '2.0', 'symbol': 'A'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}, {'level': '4.0', 'symbol': 'A47'}, {'level': '4.0', 'symbol': 'A61'}, {'level': '4.0', 'symbol': 'A62'}, {'level': '4.0', 'symbol': 'A63'}, {'level': '4.0', 'symbol': 'A99'}, {'level': '5.0', 'symbol': 'A01B'}, {'level': '5.0', 'symbol': 'A01C'}, {'level': '5.0', 'symbol': 'A01D'}], 'var_function-call-8858317480294281354': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-2682890762204433757': 'file_storage/function-call-2682890762204433757.json', 'var_function-call-8840751192597969666': [], 'var_function-call-4859995573037014798': 'Done', 'var_function-call-9227348669350318438': {'total_records': 50, 'passed_grant_filter': 0, 'sample_grant_dates': [{'orig': '14th Mar 2019', 'parsed': 'None'}, {'orig': 'dated 21st November 2019', 'parsed': 'None'}, {'orig': 'Mar 21st, 2019', 'parsed': 'None'}, {'orig': '5th of December, 2019', 'parsed': 'None'}, {'orig': '22nd of August, 2019', 'parsed': 'None'}, {'orig': 'September the 19th, 2019', 'parsed': 'None'}, {'orig': 'on March 14th, 2019', 'parsed': 'None'}, {'orig': '28th Feb 2019', 'parsed': 'None'}, {'orig': '17th of October, 2019', 'parsed': 'None'}, {'orig': 'on March 21st, 2019', 'parsed': 'None'}]}, 'var_function-call-8971964726265482523': [{'orig': '14th Mar 2019', 'result': 'Error: Unknown datetime string format, unable to parse: \x01 Mar 2019, at position 0, Cleaned: \x01 Mar 2019'}, {'orig': 'dated 21st November 2019', 'result': 'Error: Unknown datetime string format, unable to parse: dated \x01 November 2019, at position 0, Cleaned: dated \x01 November 2019'}, {'orig': 'Mar 21st, 2019', 'result': 'Error: Unknown datetime string format, unable to parse: Mar \x01 2019, at position 0, Cleaned: Mar \x01 2019'}, {'orig': '5th of December, 2019', 'result': 'Error: Unknown datetime string format, unable to parse: \x01 of December 2019, at position 0, Cleaned: \x01 of December 2019'}, {'orig': '22nd of August, 2019', 'result': 'Error: Unknown datetime string format, unable to parse: \x01 of August 2019, at position 0, Cleaned: \x01 of August 2019'}], 'var_function-call-17399902918482807540': [{'count(*)': '50'}]}

exec(code, env_args)

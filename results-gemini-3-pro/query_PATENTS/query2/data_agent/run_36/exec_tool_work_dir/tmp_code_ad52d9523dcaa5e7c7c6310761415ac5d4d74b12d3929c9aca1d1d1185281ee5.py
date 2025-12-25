code = """import json
import pandas as pd
import re

filename = locals()['var_function-call-2682890762204433757']
with open(filename, 'r') as f:
    data = json.load(f)

def parse_date(d_str):
    if not isinstance(d_str, str): return None
    clean = re.sub(r'(?i)\b(?:dated|on|of|the)\b', '', d_str)
    clean = re.sub(r'(\d+)(?:st|nd|rd|th)', r'\1', clean)
    clean = clean.replace(',', ' ').strip()
    clean = re.sub(r'\s+', ' ', clean)
    try:
        return pd.to_datetime(clean)
    except:
        return None

debug_info = {}
debug_info['total_records'] = len(data)

passed_grant_filter = 0
sample_grant_dates = []

for i, row in enumerate(data):
    g_date_str = row.get('grant_date')
    g_date = parse_date(g_date_str)
    if i < 10:
        sample_grant_dates.append({'orig': g_date_str, 'parsed': str(g_date)})
    
    if g_date and g_date.year == 2019 and g_date.month >= 7:
        passed_grant_filter += 1

debug_info['passed_grant_filter'] = passed_grant_filter
debug_info['sample_grant_dates'] = sample_grant_dates

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-2465763669392206693': 'file_storage/function-call-2465763669392206693.json', 'var_function-call-10552974933409371808': [{'count(*)': '277813'}], 'var_function-call-12947090445961145540': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-7723433747525131136': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-5457342836447626573': [{'level': '2.0', 'symbol': 'A'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}, {'level': '4.0', 'symbol': 'A47'}, {'level': '4.0', 'symbol': 'A61'}, {'level': '4.0', 'symbol': 'A62'}, {'level': '4.0', 'symbol': 'A63'}, {'level': '4.0', 'symbol': 'A99'}, {'level': '5.0', 'symbol': 'A01B'}, {'level': '5.0', 'symbol': 'A01C'}, {'level': '5.0', 'symbol': 'A01D'}], 'var_function-call-8858317480294281354': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-2682890762204433757': 'file_storage/function-call-2682890762204433757.json', 'var_function-call-8840751192597969666': [], 'var_function-call-4859995573037014798': 'Done'}

exec(code, env_args)

code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-12461863306711792077'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
debug = {}
debug['count_raw'] = len(df)
debug['sample_raw_grant'] = df['grant_date'].head(5).tolist()

def parse_date(date_str):
    if not isinstance(date_str, str):
        return pd.NaT
    s = re.sub(r'(?<=\d)(st|nd|rd|th)\b', '', date_str)
    s = re.sub(r'\b(on|dated|of|the)\b', '', s, flags=re.IGNORECASE)
    s = s.replace(',', ' ')
    s = s.strip()
    try:
        dt = pd.to_datetime(s, errors='coerce')
        return dt
    except:
        return pd.NaT

df['grant_dt'] = df['grant_date'].apply(parse_date)
debug['sample_parsed_grant'] = df['grant_dt'].head(5).astype(str).tolist()

mask = (df['grant_dt'] >= '2019-07-01') & (df['grant_dt'] <= '2019-12-31')
debug['count_filtered'] = mask.sum()
debug['count_filtered_int'] = int(mask.sum())

print("__RESULT__:")
print(json.dumps({"debug": debug}))"""

env_args = {'var_function-call-864177832263507867': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-864177832263504362': 'file_storage/function-call-864177832263504362.json', 'var_function-call-4079124224651373343': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-4079124224651374308': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-12461863306711792077': 'file_storage/function-call-12461863306711792077.json', 'var_function-call-8204491127097861937': {'top_results': [], 'all_codes': []}, 'var_function-call-4322196525132722940': 'Debug Info Printed', 'var_function-call-7056566880538965638': {'top_results': [], 'all_codes': []}}

exec(code, env_args)

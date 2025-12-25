code = """import json
import pandas as pd
from datetime import datetime

file_path = locals()['var_function-call-8210490788658783622']
with open(file_path, 'r') as f:
    records = json.load(f)

print(f"Total records loaded: {len(records)}")

def parse_date(date_str):
    if not date_str:
        return None
    clean = date_str.replace('dated ', '').replace('on ', '').replace('of ', '').replace(',', '').strip()
    for suffix in ['st', 'nd', 'rd', 'th']:
        clean = clean.replace(suffix, '')
    formats = [
        "%d %B %Y", "%B %d %Y", "%Y %B %d", 
        "%d %b %Y", "%b %d %Y", "%Y %b %d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(clean, fmt)
        except ValueError:
            continue
    return None

parsed_grant_dates = 0
h2_2019 = 0
filing_dates = 0
cpc_parsed = 0

for r in records:
    g_date = parse_date(r['grant_date'])
    if g_date:
        parsed_grant_dates += 1
        if g_date.year == 2019 and g_date.month >= 7:
            h2_2019 += 1
            f_date = parse_date(r['filing_date'])
            if f_date:
                filing_dates += 1
                try:
                    cpc_list = json.loads(r['cpc'])
                    cpc_parsed += 1
                except:
                    pass

print(f"Parsed Grant Dates: {parsed_grant_dates}")
print(f"H2 2019 Grants: {h2_2019}")
print(f"With Filing Date: {filing_dates}")
print(f"With CPC: {cpc_parsed}")

print("__RESULT__:")
print(json.dumps({"status": "debug complete"}))"""

env_args = {'var_function-call-9349135532436099927': 'file_storage/function-call-9349135532436099927.json', 'var_function-call-7996704792418014537': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-135606811111269997': [{'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B59/00', 'level': '7.0', 'titleFull': 'Devices specially adapted for connection between animals or tractors and agricultural machines or implements'}, {'symbol': 'A01B19/00', 'level': '7.0', 'titleFull': 'Harrows with non-rotating tools'}, {'symbol': 'A01B35/00', 'level': '7.0', 'titleFull': 'Other machines for working soil not specially adapted for working soil on which crops are growing'}, {'symbol': 'A01B13/00', 'level': '7.0', 'titleFull': 'Ploughs or like machines for special purposes ; Ditch diggers, trench ploughs, forestry ploughs, ploughs for land or marsh reclamation'}], 'var_function-call-14112593806741946107': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-18427524461417541909': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-8210490788658783622': 'file_storage/function-call-8210490788658783622.json', 'var_function-call-16513184790929394189': [{'cpc_group': 'B41', 'best_year': 2007, 'max_ema': 1.0}]}

exec(code, env_args)

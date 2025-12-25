code = """import json
import pandas as pd
import re
import datetime

with open(locals()['var_function-call-14777437780010198130'], 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str:
        return None
    s = str(date_str).lower()
    s = re.sub(r'(st|nd|rd|th)', '', s)
    s = re.sub(r'\b(on|dated|of|the)\b', '', s)
    s = re.sub(r'[,]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    try:
        return pd.to_datetime(s)
    except:
        return None

matches = []
for entry in data:
    g_raw = entry.get('grant_date')
    g_date = parse_date(g_raw)
    
    if g_date and (datetime.datetime(2019, 7, 1) <= g_date <= datetime.datetime(2019, 12, 31)):
        matches.append((g_raw, str(g_date)))

print("__RESULT__:")
print(json.dumps({"matches_count": len(matches), "sample": matches[:10]}))"""

env_args = {'var_function-call-4980740479115432120': 'file_storage/function-call-4980740479115432120.json', 'var_function-call-885587414874800350': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-885587414874803867': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}], 'var_function-call-4189893605340898872': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4189893605340900237': 'file_storage/function-call-4189893605340900237.json', 'var_function-call-13165109459917276818': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A23', 'level': '4.0', 'titleFull': 'FOODS OR FOODSTUFFS; TREATMENT THEREOF, NOT COVERED BY OTHER CLASSES'}, {'symbol': 'A23N', 'level': '5.0', 'titleFull': 'MACHINES OR APPARATUS FOR TREATING HARVESTED FRUIT, VEGETABLES OR FLOWER BULBS IN BULK, NOT OTHERWISE PROVIDED FOR; PEELING VEGETABLES OR FRUIT IN BULK; APPARATUS FOR PREPARING ANIMAL FEEDING- STUFFS'}, {'symbol': 'A23N12/00', 'level': '7.0', 'titleFull': 'Machines for cleaning, blanching, drying or roasting fruits or vegetables, e.g. coffee, cocoa, nuts'}, {'symbol': 'A23N12/10', 'level': '9.0', 'titleFull': 'Rotary roasters'}], 'var_function-call-5077132125135892078': 'file_storage/function-call-5077132125135892078.json', 'var_function-call-17810397091798378241': [], 'var_function-call-16513327143657409192': 'Done', 'var_function-call-12766764133723906386': {'total': 14, 'date_ok': 2, 'country_ok': 2, 'cpc_ok': 2, 'dates_sample': [['28th Feb 2019', '2019-02-28 00:00:00'], ['26th September 2019', '2019-09-26 00:00:00'], ['21st of February, 2019', '2019-02-21 00:00:00'], ['August the 14th, 2019', 'None'], ['2019 on Mar 14th', '2019-03-14 00:00:00']]}, 'var_function-call-427749757161139328': [{'count(*)': '1932'}], 'var_function-call-14777437780010198130': 'file_storage/function-call-14777437780010198130.json', 'var_function-call-12050010611306653012': []}

exec(code, env_args)

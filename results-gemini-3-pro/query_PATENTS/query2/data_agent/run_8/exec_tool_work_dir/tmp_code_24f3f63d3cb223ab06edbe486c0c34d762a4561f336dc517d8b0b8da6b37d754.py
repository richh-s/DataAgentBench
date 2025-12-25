code = """import json
import re
from datetime import datetime

file_path = locals()['var_function-call-16013154277933524664']
with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str:
        return None
    year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if not year_match:
        return None
    year = int(year_match.group(0))
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
        'july': 7, 'june': 6, 'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    month = 1
    lower_str = date_str.lower()
    found_month = False
    for m, num in months.items():
        if m in lower_str:
            month = num
            found_month = True
            break
    if not found_month:
        # Default to 1 if not found? Or fail?
        pass

    day_match = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', date_str)
    day = int(day_match.group(1)) if day_match else 1
    
    return datetime(year, month, day)

debug_results = []
for p in data:
    info = p.get('Patents_info', '')
    g_date_str = p.get('grant_date', '')
    g_date = parse_date(g_date_str)
    
    is_de = False
    if re.search(r'\bfrom DE\b', info, re.IGNORECASE):
        is_de = True
    elif re.search(r'\bDE patent\b', info, re.IGNORECASE):
        is_de = True
    elif re.search(r'DE-\d+', info):
        is_de = True
        
    is_h2_2019 = False
    if g_date and datetime(2019, 7, 1) <= g_date <= datetime(2019, 12, 31):
        is_h2_2019 = True
        
    if is_de:
        debug_results.append({
            "info": info[:50],
            "g_date_str": g_date_str,
            "g_date": str(g_date),
            "is_h2_2019": is_h2_2019
        })

print("__RESULT__:")
print(json.dumps(debug_results[:10]))"""

env_args = {'var_function-call-7596832698006438446': 'file_storage/function-call-7596832698006438446.json', 'var_function-call-15018955197929013117': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-10909241304662770037': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-9645515799168749745': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-857415788462902268': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}], 'var_function-call-16013154277933524664': 'file_storage/function-call-16013154277933524664.json', 'var_function-call-6280867316487424436': [], 'var_function-call-4520269633117553141': {'total_records': 216, 'sample_grant_dates': ['14th Mar 2019', '2019 on Jul 12th', 'on October 31st, 2019', 'on November 5th, 2019', '8th Jan 2019'], 'sample_patents_info': ['Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.'], 'sample_cpc': ['[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]']}}

exec(code, env_args)

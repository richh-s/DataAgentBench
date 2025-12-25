code = """import json
import pandas as pd
from datetime import datetime
import re

# Load results
with open(locals()['var_function-call-9850245990308066574'], 'r') as f:
    patents = json.load(f)

debug_info = {}
debug_info['total_loaded'] = len(patents)

def parse_date(date_str):
    if not date_str:
        return None
    date_str = date_str.lower().replace("dated", "").replace("on", "").replace("of", "").replace(",", "").replace(".", "").strip()
    date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    
    formats = [
        "%d %B %Y", "%B %d %Y", "%Y %B %d",
        "%d %b %Y", "%b %d %Y",
        "%Y-%m-%d"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

sample_dates = []
for i in range(min(5, len(patents))):
    d = patents[i].get('grant_date')
    parsed = parse_date(d)
    sample_dates.append(f"Raw: {d} -> Parsed: {parsed}")
debug_info['samples'] = sample_dates

cnt_h2 = 0
cnt_filed = 0
cnt_cpc = 0

for p in patents:
    dt = parse_date(p.get('grant_date'))
    if dt and dt.year == 2019 and dt.month >= 7:
        cnt_h2 += 1
        
        f_dt = parse_date(p.get('filing_date'))
        if f_dt:
            cnt_filed += 1
            
            cpc_json = p.get('cpc')
            if cpc_json:
                cnt_cpc += 1

debug_info['h2_2019_count'] = cnt_h2
debug_info['filed_date_count'] = cnt_filed
debug_info['cpc_count'] = cnt_cpc

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-13186560279327223649': 'file_storage/function-call-13186560279327223649.json', 'var_function-call-13186560279327220156': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-14970819546333422104': [{'symbol': 'C', 'level': '2.0', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-14970819546333424263': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-445264303235556503': [{'level': '4.0', 'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'level': '4.0', 'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'level': '4.0', 'symbol': 'B30', 'titleFull': 'PRESSES'}, {'level': '4.0', 'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'level': '4.0', 'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'level': '4.0', 'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '4.0', 'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'level': '4.0', 'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'level': '4.0', 'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'level': '4.0', 'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_function-call-9850245990308066574': 'file_storage/function-call-9850245990308066574.json', 'var_function-call-9850245990308067851': 'file_storage/function-call-9850245990308067851.json', 'var_function-call-6965286784776120888': [], 'var_function-call-10976782815900498646': 'DEBUG_DONE'}

exec(code, env_args)

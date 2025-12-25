code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-9850245990308066574'], 'r') as f:
    patents = json.load(f)

def clean_date_str(date_str):
    if not date_str:
        return None
    s = date_str.lower()
    for w in ["dated", "on", "of", ",", "."]:
        s = s.replace(w, " ")
    s = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', s)
    return s.strip().title() # Title Case

log = []
h2_count = 0
valid_dates = 0

for i, p in enumerate(patents):
    raw = p.get('grant_date')
    clean = clean_date_str(raw)
    try:
        dt = pd.to_datetime(clean)
    except:
        dt = None
    
    if i < 10:
        log.append(f"Raw: {raw} | Clean: {clean} | DT: {str(dt)}")
        
    if dt is not None and dt is not pd.NaT:
        valid_dates += 1
        if dt.year == 2019 and dt.month >= 7:
            h2_count += 1

result = {
    "h2_count": h2_count,
    "valid_dates": valid_dates,
    "samples": log
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13186560279327223649': 'file_storage/function-call-13186560279327223649.json', 'var_function-call-13186560279327220156': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-14970819546333422104': [{'symbol': 'C', 'level': '2.0', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-14970819546333424263': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.'}], 'var_function-call-445264303235556503': [{'level': '4.0', 'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'level': '4.0', 'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'level': '4.0', 'symbol': 'B30', 'titleFull': 'PRESSES'}, {'level': '4.0', 'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'level': '4.0', 'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'level': '4.0', 'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'level': '4.0', 'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'level': '4.0', 'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'level': '4.0', 'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'level': '4.0', 'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_function-call-9850245990308066574': 'file_storage/function-call-9850245990308066574.json', 'var_function-call-9850245990308067851': 'file_storage/function-call-9850245990308067851.json', 'var_function-call-6965286784776120888': [], 'var_function-call-10976782815900498646': 'DEBUG_DONE', 'var_function-call-323488862480341926': {'total_loaded': 73, 'samples': ['Raw: 14th Mar 2019 -> Parsed: None', 'Raw: dated 21st November 2019 -> Parsed: None', 'Raw: Mar 21st, 2019 -> Parsed: None', 'Raw: 5th of December, 2019 -> Parsed: None', 'Raw: 22nd of August, 2019 -> Parsed: None'], 'h2_2019_count': 0, 'filed_date_count': 0, 'cpc_count': 0}, 'var_function-call-4369416132552219087': [], 'var_function-call-15346973558814915037': 'DONE'}

exec(code, env_args)

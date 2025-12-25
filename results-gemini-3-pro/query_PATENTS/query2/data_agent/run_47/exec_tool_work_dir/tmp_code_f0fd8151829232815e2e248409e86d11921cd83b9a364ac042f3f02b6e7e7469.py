code = """import json
import re

patents_file = locals()['var_function-call-2170997591860169165']
with open(patents_file, 'r') as f:
    patents = json.load(f)

def parse_date(date_str):
    if not isinstance(date_str, str): return None, None
    months = {
        'january': 1, 'jan': 1, 'february': 2, 'feb': 2, 'march': 3, 'mar': 3,
        'april': 4, 'apr': 4, 'may': 5, 'june': 6, 'jun': 6, 'july': 7, 'jul': 7,
        'august': 8, 'aug': 8, 'september': 9, 'sep': 9, 'sept': 9, 'october': 10, 'oct': 10,
        'november': 11, 'nov': 11, 'december': 12, 'dec': 12
    }
    date_str_lower = date_str.lower()
    year_match = re.search(r'\b(20\d{2}|19\d{2})\b', date_str)
    year = int(year_match.group(1)) if year_match else None
    month = None
    for m_name, m_num in months.items():
        if m_name in date_str_lower:
            month = m_num
            break
    return year, month

print("__RESULT__:")
debug_info = []
for i, p in enumerate(patents[:5]):
    info = {"index": i}
    p_info = p.get('Patents_info', '')
    g_str = p.get('grant_date', '')
    f_str = p.get('filing_date', '')
    
    info['DE_check'] = "DE-" in p_info
    
    gy, gm = parse_date(g_str)
    info['grant_parsed'] = (gy, gm)
    info['grant_pass'] = (gy == 2019 and gm is not None and gm >= 7)
    
    fy, fm = parse_date(f_str)
    info['filing_parsed'] = (fy, fm)
    
    debug_info.append(info)

print(json.dumps(debug_info))"""

env_args = {'var_function-call-16467411643082778983': 'file_storage/function-call-16467411643082778983.json', 'var_function-call-16467411643082777012': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}], 'var_function-call-2220453102059421347': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-2220453102059421236': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-10017610776034245005': [{'symbol': 'C', 'level': '2.0', 'titleFull': 'CHEMISTRY; METALLURGY'}, {'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-10017610776034245172': [{'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.'}, {'Patents_info': 'The DE patent application (no. DE-10134061-A) is belonging to MOSMATIC AG NECKER and has publication number DE-10134061-B4.'}], 'var_function-call-13762917742806902705': [{'len': '3', 'cnt': '137'}], 'var_function-call-2170997591860169165': 'file_storage/function-call-2170997591860169165.json', 'var_function-call-5891586721883316256': 'file_storage/function-call-5891586721883316256.json', 'var_function-call-16313897181570839081': []}

exec(code, env_args)

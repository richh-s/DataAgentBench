code = """import json
import re

patents_file = locals()['var_function-call-7275035853467232807']
with open(patents_file, 'r') as f:
    patents = json.load(f)

month_map = {
    'january': 1, 'jan': 1, 'february': 2, 'feb': 2, 'march': 3, 'mar': 3,
    'april': 4, 'apr': 4, 'may': 5, 'june': 6, 'jun': 6,
    'july': 7, 'jul': 7, 'august': 8, 'aug': 8, 'september': 9, 'sep': 9, 'sept': 9,
    'october': 10, 'oct': 10, 'november': 11, 'nov': 11, 'december': 12, 'dec': 12
}

def parse_debug(date_str):
    if not isinstance(date_str, str): return f"NotStr: {date_str}"
    s = date_str.lower()
    s = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', s)
    s = re.sub(r'\b(on|dated|the|of)\b', ' ', s)
    s = s.replace(',', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    
    debug_str = f"Cleaned: '{s}'"
    
    m1 = re.match(r'^(\d{1,2})\s+([a-z]+)\s+(\d{4})$', s)
    if m1:
        d, m_str, y = m1.groups()
        debug_str += f" | M1 Match: d={d}, m={m_str}, y={y}"
        if m_str in month_map:
            return f"Success M1: {y}-{month_map[m_str]}-{d}"
        else:
            return debug_str + f" | M1 Month fail: {m_str}"
            
    m2 = re.match(r'^([a-z]+)\s+(\d{1,2})\s+(\d{4})$', s)
    if m2:
        m_str, d, y = m2.groups()
        debug_str += f" | M2 Match: m={m_str}, d={d}, y={y}"
        if m_str in month_map:
            return f"Success M2: {y}-{month_map[m_str]}-{d}"
        else:
            return debug_str + f" | M2 Month fail: {m_str}"

    m3 = re.match(r'^(\d{4})\s+([a-z]+)\s+(\d{1,2})$', s)
    if m3:
        y, m_str, d = m3.groups()
        debug_str += f" | M3 Match: y={y}, m={m_str}, d={d}"
        if m_str in month_map:
            return f"Success M3: {y}-{month_map[m_str]}-{d}"
        else:
            return debug_str + f" | M3 Month fail: {m_str}"

    return debug_str + " | No Regex Match"

log = []
for p in patents:
    info = p.get('Patents_info', '')
    if 'from DE' in info or 'no. DE-' in info or 'number DE-' in info:
        gd_raw = p.get('grant_date')
        res = parse_debug(gd_raw)
        log.append({"raw": gd_raw, "debug": res})
        if len(log) > 5: break

print("__RESULT__:")
print(json.dumps(log))"""

env_args = {'var_function-call-7351366711499102361': 'file_storage/function-call-7351366711499102361.json', 'var_function-call-11515452664161874980': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-11515452664161874233': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '14th Mar 2019', 'filing_date': '2013, June 17th'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 19th, 2019', 'filing_date': 'on December 4th, 2017'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 12th, 2019', 'filing_date': '2018 on Feb 15th'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Jul 12th', 'filing_date': '23rd May 2018'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'on March 14th, 2019', 'filing_date': 'Jan 26th, 2015'}], 'var_function-call-1416837484132766701': [{'symbol': 'G06', 'level': '4.0'}, {'symbol': 'G06F', 'level': '5.0'}, {'symbol': 'G06F9/45533', 'level': '11.0'}], 'var_function-call-4145452741131447632': 'file_storage/function-call-4145452741131447632.json', 'var_function-call-7275035853467232807': 'file_storage/function-call-7275035853467232807.json', 'var_function-call-6193105334250981051': [], 'var_function-call-9778875351287087866': {'total_patents': 211, 'de_filtered': 68, 'h2_2019_filtered': 0, 'filing_date_ok': 0, 'cpc_ok': 0, 'samples': [{'info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}, {'info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019'}]}, 'var_function-call-2227501644259941897': [{'raw': '14th Mar 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': 'dated 21st November 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': 'Mar 21st, 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': '5th of December, 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': '22nd of August, 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': 'September the 19th, 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': 'on March 14th, 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': '28th Feb 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': '17th of October, 2019', 'parsed': 'None', 'status': 'Fail Parse'}, {'raw': 'on March 21st, 2019', 'parsed': 'None', 'status': 'Fail Parse'}], 'var_function-call-13283183169301218823': [], 'var_function-call-5323841888133694780': [{'info': 'Patent application (no. DE-102013211266-A) from DE', 'grant_raw': '14th Mar 2019', 'grant_parsed': None}, {'info': 'In DE, the application (number DE-102007032978-A) ', 'grant_raw': 'dated 21st November 2019', 'grant_parsed': None}, {'info': 'The DE application (number DE-102009046500-A) is o', 'grant_raw': 'Mar 21st, 2019', 'grant_parsed': None}, {'info': 'The DE patent application (no. DE-102010042467-A) ', 'grant_raw': '5th of December, 2019', 'grant_parsed': None}, {'info': 'In DE, the patent filing (application no. DE-11201', 'grant_raw': '22nd of August, 2019', 'grant_parsed': None}, {'info': 'In DE, the patent filing (application number DE-10', 'grant_raw': 'September the 19th, 2019', 'grant_parsed': None}, {'info': 'DIEFFENBACHER GMBH MASCHINEN holds the DE patent a', 'grant_raw': 'on March 14th, 2019', 'grant_parsed': None}, {'info': 'The DE patent filing (application number DE-102018', 'grant_raw': '28th Feb 2019', 'grant_parsed': None}, {'info': 'The DE application (number DE-102014111322-A) is o', 'grant_raw': '17th of October, 2019', 'grant_parsed': None}, {'info': 'In DE, the patent application (no. DE-102014209298', 'grant_raw': 'on March 21st, 2019', 'grant_parsed': None}, {'info': 'SCHNEIDER KUNSTSTOFFWERKE GMBH holds the DE patent', 'grant_raw': '7th March 2019', 'grant_parsed': None}, {'info': 'BRUKER BIOSPIN GMBH holds the DE application (numb', 'grant_raw': 'February 28th, 2019', 'grant_parsed': None}, {'info': 'Application (no. DE-112015005888-T) from DE, belon', 'grant_raw': 'August the 29th, 2019', 'grant_parsed': None}, {'info': 'The DE application (ID DE-102016102746-A) is belon', 'grant_raw': 'dated 4th July 2019', 'grant_parsed': None}, {'info': 'FORD GLOBAL TECH LLC holds the DE application (num', 'grant_raw': '28th March 2019', 'grant_parsed': None}, {'info': 'Patent application (number DE-102017201883-A) from', 'grant_raw': '2019 on Mar 28th', 'grant_parsed': None}, {'info': 'The DE patent filing (application no. DE-102018213', 'grant_raw': '26th September 2019', 'grant_parsed': None}, {'info': 'In DE, the patent application (number DE-102011108', 'grant_raw': '2019, December 24th', 'grant_parsed': None}, {'info': 'The DE patent filing (application no. DE-102014012', 'grant_raw': '21st of February, 2019', 'grant_parsed': None}, {'info': 'The DE application (number DE-102015121777-A) is h', 'grant_raw': '2nd Oct 2019', 'grant_parsed': None}, {'info': 'Patent filing (app. number DE-102016108055-A) from', 'grant_raw': 'December 24th, 2019', 'grant_parsed': None}]}

exec(code, env_args)

code = """import json
import re
import pandas as pd
import datetime

patents_file = locals()['var_function-call-7275035853467232807']
with open(patents_file, 'r') as f:
    patents = json.load(f)

def parse_date(date_str):
    if not isinstance(date_str, str): return None
    # Remove ordinal suffixes
    clean_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    # Remove filler words
    clean_str = re.sub(r'\b(on|dated|the|of)\b', '', clean_str, flags=re.IGNORECASE)
    # Remove commas
    clean_str = clean_str.replace(',', ' ').strip()
    # Normalize spaces
    clean_str = re.sub(r'\s+', ' ', clean_str)
    
    try:
        dt = pd.to_datetime(clean_str, errors='coerce')
        if pd.notnull(dt):
            return dt
    except:
        pass
    return None

test_str = "dated 21st November 2019"
parsed_test = parse_date(test_str)
print(f"Test parse '{test_str}': {parsed_test}")

log = []
count_pass = 0

for p in patents:
    info = p.get('Patents_info', '')
    is_de = False
    if 'from DE' in info or 'no. DE-' in info or 'number DE-' in info or 'publication no. DE-' in info or 'publication number DE-' in info:
        is_de = True
    
    if is_de:
        raw_grant = p.get('grant_date')
        g_date = parse_date(raw_grant)
        status = "Fail"
        if g_date:
            if g_date.year == 2019:
                if g_date.month >= 7:
                    status = "Pass"
                    count_pass += 1
                else:
                    status = "Fail Month"
            else:
                status = f"Fail Year {g_date.year}"
        else:
            status = "Fail Parse"
        
        if len(log) < 10:
            log.append({"raw": raw_grant, "parsed": str(g_date), "status": status})

print(f"Total Pass H2 2019: {count_pass}")
print("__RESULT__:")
print(json.dumps(log))"""

env_args = {'var_function-call-7351366711499102361': 'file_storage/function-call-7351366711499102361.json', 'var_function-call-11515452664161874980': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-11515452664161874233': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '14th Mar 2019', 'filing_date': '2013, June 17th'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 19th, 2019', 'filing_date': 'on December 4th, 2017'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 12th, 2019', 'filing_date': '2018 on Feb 15th'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Jul 12th', 'filing_date': '23rd May 2018'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'on March 14th, 2019', 'filing_date': 'Jan 26th, 2015'}], 'var_function-call-1416837484132766701': [{'symbol': 'G06', 'level': '4.0'}, {'symbol': 'G06F', 'level': '5.0'}, {'symbol': 'G06F9/45533', 'level': '11.0'}], 'var_function-call-4145452741131447632': 'file_storage/function-call-4145452741131447632.json', 'var_function-call-7275035853467232807': 'file_storage/function-call-7275035853467232807.json', 'var_function-call-6193105334250981051': [], 'var_function-call-9778875351287087866': {'total_patents': 211, 'de_filtered': 68, 'h2_2019_filtered': 0, 'filing_date_ok': 0, 'cpc_ok': 0, 'samples': [{'info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}, {'info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019'}]}}

exec(code, env_args)

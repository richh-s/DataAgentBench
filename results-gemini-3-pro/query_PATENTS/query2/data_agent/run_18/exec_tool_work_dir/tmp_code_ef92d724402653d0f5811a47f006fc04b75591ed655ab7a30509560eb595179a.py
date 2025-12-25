code = """import json
import re
from datetime import datetime

file_path = locals()['var_function-call-6383820464758651535']
with open(file_path, 'r') as f:
    records = json.load(f)

print("Total records:", len(records))

cnt = 0
for r in records[:50]:
    p_info = r.get('Patents_info', '')
    g_date_str = r.get('grant_date', '')
    
    # Check simple DE filter
    if 'DE' not in p_info and 'Germany' not in p_info:
        continue

    cnt += 1
    # print raw
    print(f"Record: {p_info[:50]}... Date: {g_date_str}")

    clean = re.sub(r'(?i)\b(on|dated|the|of)\b', '', g_date_str)
    clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', clean)
    clean = clean.replace(',', ' ').strip()
    # Replace multiple spaces
    clean = re.sub(r'\s+', ' ', clean)
    
    print(f"  Clean Date: '{clean}'")
    
    parsed = None
    for fmt in ["%d %b %Y", "%Y %b %d", "%B %d %Y", "%d %B %Y", "%Y %B %d", "%b %d %Y"]:
        try:
            parsed = datetime.strptime(clean, fmt)
            break
        except:
            pass
    
    print(f"  Parsed: {parsed}")
    if cnt > 10:
        break

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-4575975267135224610': 'file_storage/function-call-4575975267135224610.json', 'var_function-call-3559050311259836928': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-9512409107012440047': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A01B1/22', 'level': '8.0'}, {'symbol': 'A01B1/16', 'level': '8.0'}, {'symbol': 'A01B1/20', 'level': '8.0'}, {'symbol': 'A01B1/06', 'level': '8.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01B1/24', 'level': '8.0'}], 'var_function-call-13552412906166802932': [{'count(*)': '277813'}], 'var_function-call-11062304279063144868': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_function-call-16421393693204446287': [{'avg(length(cpc))': '903.0832322461512'}], 'var_function-call-6383820464758651535': 'file_storage/function-call-6383820464758651535.json', 'var_function-call-13717256898465498863': []}

exec(code, env_args)

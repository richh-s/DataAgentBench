code = """import json
import re

# Access the data from the file path stored in var_functions.query_db:0
patent_data = var_functions.query_db:0

# Read the JSON file
with open(patent_data, 'r') as f:
    all_patents = json.load(f)

print('Total patents loaded:', len(all_patents))

# Now filter for German patents in second half of 2019
german_patents = []

for patent in all_patents:
    # Check German marker
    if 'from DE' not in patent['Patents_info']:
        continue
    
    # Check 2019
    grant_date = patent['grant_date']
    if '2019' not in grant_date:
        continue
    
    # Check second half (Jul-Dec)
    date_upper = grant_date.upper()
    has_second_half_month = any(m in date_upper for m in ['JUL','AUG','SEP','OCT','NOV','DEC'])
    
    # Also check full month names
    if not has_second_half_month:
        has_second_half_month = any(m in grant_date for m in ['July','August','September','October','November','December'])
    
    if has_second_half_month:
        german_patents.append(patent)

print('German patents in H2 2019:', len(german_patents))

# Display a few samples
for i in range(min(5, len(german_patents))):
    p = german_patents[i]
    print(f"\nSample {i+1}:")
    print('Info:', p['Patents_info'][:80] + '...' if len(p['Patents_info']) > 80 else p['Patents_info'])
    print('Grant:', p['grant_date'])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

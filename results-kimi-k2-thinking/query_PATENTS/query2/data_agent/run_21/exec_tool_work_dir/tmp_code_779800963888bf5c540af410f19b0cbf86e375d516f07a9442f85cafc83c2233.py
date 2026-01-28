code = """import json
import os

# Get the file path from the storage variable
file_info = var_functions.query_db:62

# Load patent data
if isinstance(file_info, str) and os.path.exists(file_info):
    with open(file_info, 'r') as f:
        patents_data = json.load(f)
else:
    # If it's already a list, use it directly
    patents_data = file_info

print('Total patents in dataset:', len(patents_data))
print('First patent info:', patents_data[0]['Patents_info'][:80] + '...')
print('First patent grant date:', patents_data[0]['grant_date'])

# Identify German patents in second half of 2019
german_h2_2019 = []

for patent in patents_data:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check if German patent
    is_german = False
    german_markers = ['from DE', 'In DE,', 'DE application', 'DE patent', 'DE-']
    for marker in german_markers:
        if marker in patents_info:
            is_german = True
            break
    
    if not is_german:
        continue
    
    # Check if 2019
    if '2019' not in grant_date:
        continue
    
    # Check if second half (July-December)
    second_half_months = ['July', 'August', 'September', 'October', 'November', 'December',
                         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    in_second_half = False
    for month in second_half_months:
        if month in grant_date:
            in_second_half = True
            break
    
    if in_second_half:
        german_h2_2019.append(patent)

print('German patents in second half 2019:', len(german_h2_2019))

# Show a few examples
for i in range(min(3, len(german_h2_2019))):
    p = german_h2_2019[i]
    print(f"\nExample {i+1}:")
    print('Info:', p['Patents_info'][:80] + '...' if len(p['Patents_info']) > 80 else p['Patents_info'])
    print('Grant:', p['grant_date'])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)

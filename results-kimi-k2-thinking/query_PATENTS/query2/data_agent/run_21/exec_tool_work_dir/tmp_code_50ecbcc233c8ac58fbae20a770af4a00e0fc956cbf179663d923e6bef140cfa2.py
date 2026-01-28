code = """import json
from collections import defaultdict

# Load the data
file_path = var_functions.query_db:156
with open(file_path, 'r') as f:
    patents = json.load(f)

print('Total patents loaded: ' + str(len(patents)))

# Filter for German patents in second half 2019
german_h2_2019 = []
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for patent in patents:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check German
    if 'from DE' not in patents_info and 'In DE,' not in patents_info:
        continue
    
    # Check 2019
    if '2019' not in grant_date:
        continue
    
    # Check second half
    in_h2 = False
    for month in second_half_months:
        if month in grant_date:
            in_h2 = True
            break
    
    if in_h2:
        german_h2_2019.append(patent)

print('German patents in H2 2019: ' + str(len(german_h2_2019)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json', 'var_functions.query_db:96': [], 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:102': 'file_storage/functions.query_db:102.json', 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.query_db:128': 'file_storage/functions.query_db:128.json', 'var_functions.query_db:132': 'file_storage/functions.query_db:132.json', 'var_functions.query_db:134': 'file_storage/functions.query_db:134.json', 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json', 'var_functions.query_db:140': 'file_storage/functions.query_db:140.json', 'var_functions.query_db:142': 'file_storage/functions.query_db:142.json', 'var_functions.query_db:144': 'file_storage/functions.query_db:144.json', 'var_functions.query_db:148': 'file_storage/functions.query_db:148.json', 'var_functions.query_db:150': 'file_storage/functions.query_db:150.json', 'var_functions.query_db:152': 'file_storage/functions.query_db:152.json', 'var_functions.query_db:154': 'file_storage/functions.query_db:154.json', 'var_functions.query_db:156': 'file_storage/functions.query_db:156.json', 'var_functions.query_db:158': 'file_storage/functions.query_db:158.json'}

exec(code, env_args)

code = """import json

# Load the German patent data
with open('var_functions.query_db:116.json', 'r') as f:
    patents = json.load(f)

# Filter for German patents in second half of 2019
german_h2_2019 = []
second_half_months = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']

for p in patents:
    info = p['Patents_info']
    date = p['grant_date']
    
    # Check if German (from DE or In DE)
    if 'from DE' not in info and 'In DE' not in info:
        continue
    
    # Check if 2019 and second half
    if '2019' not in date:
        continue
    
    in_second_half = any(month in date for month in second_half_months)
    if not in_second_half:
        continue
    
    german_h2_2019.append(p)

print(f'German patents in H2 2019: {len(german_h2_2019)}')

# Show first 3 to verify
for i in range(min(3, len(german_h2_2019))):
    print(f"Sample {i+1}: {german_h2_2019[i]['Patents_info'][:80]}...")
    print(f"  Grant: {german_h2_2019[i]['grant_date']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json', 'var_functions.query_db:96': [], 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:102': 'file_storage/functions.query_db:102.json', 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json'}

exec(code, env_args)

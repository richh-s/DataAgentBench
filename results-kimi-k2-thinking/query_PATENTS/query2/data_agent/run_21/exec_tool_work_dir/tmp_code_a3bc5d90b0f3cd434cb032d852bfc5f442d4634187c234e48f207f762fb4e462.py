code = """import json, re, os
# Load the patent data
patent_file_path = 'var_functions.query_db:0.json'

# Open and parse the file
with open(patent_file_path, 'r') as f:
    patents_data = json.load(f)

print('Total patents in file:', len(patents_data))

# Find German patents granted in second half of 2019
german_h2_2019 = []

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    
    # Check if German patent
    if 'from DE' not in patents_info:
        continue
    
    # Check if in 2019
    if '2019' not in grant_date:
        continue
    
    # Check if second half (July-December)
    in_second_half = False
    # Check for second half months (full names)
    second_half_full = ['July', 'August', 'September', 'October', 'November', 'December']
    for month in second_half_full:
        if month in grant_date:
            in_second_half = True
            break
    
    # Check abbreviations if not found
    if not in_second_half:
        second_half_abbr = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for month in second_half_abbr:
            if month in grant_date:
                in_second_half = True
                break
    
    if in_second_half:
        german_h2_2019.append(patent)

print('German patents in H2 2019 counted:', len(german_h2_2019))

# Show examples from the filtered set
for i in range(min(3, len(german_h2_2019))):
    patent = german_h2_2019[i]
    print(f"\nExample {i+1}:")
    print('Patents_info:', patent['Patents_info'])
    print('Grant_date:', patent['grant_date'])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

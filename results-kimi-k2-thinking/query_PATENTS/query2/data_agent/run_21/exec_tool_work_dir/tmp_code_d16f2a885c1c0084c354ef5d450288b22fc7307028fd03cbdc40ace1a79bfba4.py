code = """import json

# Read the patent data file
patent_file = var_functions.query_db:0
print('Attempting to load file:', patent_file)

# Parse the JSON data
with open(patent_file, 'r', encoding='utf-8') as f:
    patents = json.load(f)

print('Loaded patents:', len(patents))

# Identify German patents in second half 2019
german_patents = []

# Patterns to identify months in second half
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
second_half_abbrs = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for patent in patents:
    # Check if German patent
    patents_info = patent['Patents_info']
    if 'from DE' not in patents_info:
        continue
    
    # Check if grant date is 2019
    grant_date = patent['grant_date']
    if '2019' not in grant_date:
        continue
    
    # Check if in second half
    in_second_half = False
    # Try full month names
    for month in second_half_months:
        if month in grant_date:
            in_second_half = True
            break
    
    # Try abbreviations if not found
    if not in_second_half:
        for month in second_half_abbrs:
            if month in grant_date:
                in_second_half = True
                break
    
    if in_second_half:
        german_patents.append(patent)

print('German patents in second half 2019:', len(german_patents))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

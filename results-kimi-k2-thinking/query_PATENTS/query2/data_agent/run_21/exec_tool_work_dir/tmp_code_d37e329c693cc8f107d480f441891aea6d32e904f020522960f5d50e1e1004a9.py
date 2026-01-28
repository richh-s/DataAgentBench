code = """import json

# Load the patent data from the query file
patent_data_file = 'var_functions.query_db:0.json'

with open(patent_data_file, 'r') as f:
    patents = json.load(f)

print('Total patents:', len(patents))

# Show structure of first record
first = patents[0]
print('\nFirst patent structure:')
print('Keys:', list(first.keys()))
print('Patents_info:', first['Patents_info'])
print('grant_date:', first['grant_date'])
print('cpc type:', type(first['cpc']))
print('cpc preview:', str(first['cpc'])[:200])

# Check for German patents in 2019 second half through patterns rather than parsing
print('\nChecking for German patterns and 2019 second half dates...')
german_count = 0
candidates = []

for i, p in enumerate(patents):
    info = p['Patents_info']
    date = p['grant_date']
    
    # Check German
    if 'from DE' not in info:
        continue
    
    # Check 2019 second half
    if '2019' not in date:
        continue
    
    # Check month (rough)
    second_half = False
    date_upper = date.upper()
    for m in ['JUL','AUG','SEP','OCT','NOV','DEC']:
        if m in date_upper:
            second_half = True
            break
    
    if not second_half:
        # Try full month names
        for m in ['July','August','September','October','November','December']:
            if m in date:
                second_half = True
                break
    
    if second_half:
        german_count += 1
        candidates.append(p)

print(f'Found {german_count} potential German patents in second half 2019')

# Show a few
for i in range(min(3, len(candidates))):
    print(f"\n{i+1}. {candidates[i]['Patents_info']}")
    print(f'   Date: {candidates[i]["grant_date"]}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

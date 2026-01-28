code = """# Load and examine the data structure carefully
import json

data_file = var_functions.query_db:0
with open(data_file, 'r') as f:
    all_patents = json.load(f)

print('Total patents:', len(all_patents))
print('\nFirst few patents:')
for i in range(min(5, len(all_patents))):
    p = all_patents[i]
    print(f"\n{i+1}. Info: {p.get('Patents_info', '')}")
    print(f"   Grant: {p.get('grant_date', '')}")
# Count German patents in second half 2019
count = 0
german_patents = []

for p in all_patents:
    info = p.get('Patents_info', '')
    grant = p.get('grant_date', '')
    cpc = p.get('cpc', '')
    
    # Check if German
    is_german = False
    if 'from DE' in info or 'DE-' in info:
        is_german = True
    # Check if second half 2019
    in_h2_2019 = False
    if '2019' in grant:
        grant_upper = grant.upper()
        if 'JUL' in grant_upper or 'AUG' in grant_upper or 'SEP' in grant_upper or 'OCT' in grant_upper or 'NOV' in grant_upper or 'DEC' in grant_upper:
            in_h2_2019 = True
        elif 'July' in grant or 'August' in grant or 'September' in grant or 'October' in grant or 'November' in grant or 'December' in grant:
            in_h2_2019 = True
    
    if is_german and in_h2_2019:
        count += 1
        german_patents.append({
            'info': info,
            'grant': grant,
            'cpc': cpc
        })

print(f'\nFound {count} German patents in second half 2019')

# Show some examples
for i in range(min(5, len(german_patents))):
    p = german_patents[i]
    print(f"\n{i+1}. {p['info']}")
    print(f"   Grant: {p['grant']}")
    print(f"   CPC (first 150 chars): {p['cpc'][:150]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

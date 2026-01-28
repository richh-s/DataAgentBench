code = """import json

# Access the patent data file
patent_data_path = 'var_functions.query_db:0.json'

# Load the data
with open(patent_data_path, 'r') as file:
    all_patents = json.load(file)

# Initialize counter and storage
german_patents_h2_2019 = []

# Define second half month indicators
second_half_indicators = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']

# Filter patents
for patent in all_patents:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    
    # Check for German patents
    if 'from DE' not in patents_info:
        continue
    
    # Check for 2019
    if '2019' not in grant_date:
        continue
    
    # Check for second half months
    has_second_half_month = any(month in grant_date for month in second_half_indicators)
    
    if has_second_half_month:
        german_patents_h2_2019.append(patent)

# Display results
result_text = 'German patents in second half 2019: ' + str(len(german_patents_h2_2019))
print(result_text)

# Show up to 3 samples
for i in range(min(3, len(german_patents_h2_2019))):
    print('\nSample ' + str(i+1) + ':')
    print('Info: ' + german_patents_h2_2019[i]['Patents_info'][:80])
    print('Date: ' + german_patents_h2_2019[i]['grant_date'])

print('\nFound ' + str(len(german_patents_h2_2019)) + ' matching patents')

# Prepare for next step: extract CPC codes
cpc_count = 0
for patent in german_patents_h2_2019:
    cpc_str = patent['cpc']
    if cpc_str and len(cpc_str) > 10:
        cpc_count += 1

print('CPC data available for ' + str(cpc_count) + ' patents')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

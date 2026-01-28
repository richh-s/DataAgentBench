code = """import json
import pandas as pd
import re

# Load the data from the previous queries
data_file1 = var_functions.query_db:0
data_file2 = var_functions.query_db:8

with open(data_file1, 'r') as f:
    patents_2019 = json.load(f)

print(f"Total patents in 2019 data: {len(patents_2019)}")

# Function to extract patent country from Patents_info
def extract_country(patents_info):
    country_patterns = [
        (r'from\s+DE', 'DE'),
        (r'from\s+Germany', 'DE'),
        (r'^In\s+DE,', 'DE'),
        (r'batch\s+DE-', 'DE'),
        (r'application\s+no\.\s+DE-', 'DE'),
    ]
    
    for pattern, country in country_patterns:
        if re.search(pattern, patents_info, re.IGNORECASE):
            return country
    
    # Default: try to extract after "from" or after ","
    from_match = re.search(r'from\s+([A-Z]{2})', patents_info)
    if from_match:
        return from_match.group(1)
    
    return None

# Function to extract month from grant_date
def extract_month(grant_date):
    month_patterns = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12,
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    
    for month_name, month_num in month_patterns.items():
        if month_name in grant_date:
            return month_num
    return None

# Filter for German patents in second half of 2019
german_2019_second_half = []

for patent in patents_2019:
    patents_info = patent['Patents_info']
    grant_date = patent['grant_date']
    cpc = patent['cpc']
    
    # Check if it's a German patent
    country = extract_country(patents_info)
    if country != 'DE':
        # Additional check for DE patterns
        if 'DE-' in patents_info and ('from DE' in patents_info or 'In DE,' in patents_info):
            pass
        elif not ('from DE' in patents_info or 'In DE,' in patents_info):
            continue
    
    # Check if grant_date is in 2019 and second half
    if '2019' not in grant_date:
        continue
    
    month = extract_month(grant_date)
    if month is None or month < 7:  # Before July
        continue
    
    german_2019_second_half.append({
        'patents_info': patents_info,
        'grant_date': grant_date,
        'cpc': cpc,
        'month': month
    })

print(f"Found {len(german_2019_second_half)} German patents in second half 2019")

# Show the filtered results
if german_2019_second_half:
    print("\nFiltered German patents in second half 2019:")
    for i, patent in enumerate(german_2019_second_half[:10]):
        print(f"\n{i+1}. {patent['patents_info']}")
        print(f"   Grant: {patent['grant_date']}")
        print(f"   Month: {patent['month']}")
        print(f"   CPC: {patent['cpc'][:150]}...")
else:
    print("No German patents found in second half 2019. Let's check all German patents first...")
    german_all_2019 = []
    for patent in patents_2019:
        patents_info = patent['Patents_info']
        country = extract_country(patents_info)
        if country == 'DE' or 'from DE' in patents_info or 'In DE,' in patents_info:
            if '2019' in patent['grant_date']:
                month = extract_month(patent['grant_date'])
                german_all_2019.append((patents_info, patent['grant_date'], month))
    
    print("\nAll German patents in 2019:")
    for info, date, month in german_all_2019:
        print(f"  - {info[:80]}...")
        print(f"    Date: {date}, Month: {month}")
        print()"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

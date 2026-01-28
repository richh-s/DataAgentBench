code = """import json
import pandas as pd
import re

# Load the data from the previous query
data_file = var_functions.query_db:0
with open(data_file, 'r') as f:
    patents_2019 = json.load(f)

print(f"Total patents in 2019 data: {len(patents_2019)}")

# Function to extract country from patents_info
def extract_country_from_info(patents_info):
    # Look for explicit country mentions
    if 'from DE' in patents_info:
        return 'DE'
    if 'Germany' in patents_info:
        return 'DE'
    if patents_info.startswith('In DE,'):
        return 'DE'
    
    # Try to extract pattern like "no. DE-"
    if 'no. DE-' in patents_info or 'DE-10' in patents_info:
        return 'DE'
    
    return None

# Function to extract month from grant_date string
def get_month_from_date(grant_date):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    month_abbrs = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    for i, month in enumerate(month_names, 1):
        if month in grant_date:
            return i
    
    for i, month in enumerate(month_abbrs, 1):
        if month in grant_date:
            # Adjust index since we started from 1
            if month in ['Jan', 'Feb', 'Mar', 'Apr', 'Jun']:
                return i
            elif month == 'Jul':
                return 7
            elif month == 'Aug':
                return 8
            elif month == 'Sep':
                return 9
            elif month == 'Oct':
                return 10
            elif month == 'Nov':
                return 11
            elif month == 'Dec':
                return 12
    
    return None

# Filter for German patents in second half of 2019
print("Filtering for German patents in second half 2019...")

german_patents = []
month_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

for patent in patents_2019:
    # Check if German
    country = extract_country_from_info(patent['Patents_info'])
    if country != 'DE':
        continue  # Skip non-German patents
    
    # Check if in 2019 and second half
    grant_date = patent['grant_date']
    if '2019' not in grant_date:
        continue
    
    month = get_month_from_date(grant_date)
    if month is None or month < 7:  # Not in second half
        continue
    
    german_patents.append({
        'patents_info': patent['Patents_info'],
        'grant_date': grant_date,
        'cpc_str': patent['cpc'],
        'month': month
    })
    month_counts[month] += 1

print(f"Found {len(german_patents)} German patents granted in second half 2019")
print("\nMonthly breakdown:")
for month, count in sorted(month_counts.items()):
    if count > 0:
        print(f"  Month {month}: {count} patents")

if german_patents:
    print("\nSample filtered patents:")
    for i, patent in enumerate(german_patents[:5]):
        print(f"\n{i+1}. {patent['patents_info']}")
        print(f"   Grant: {patent['grant_date']}")
        print(f"   Month: {patent['month']}")
        print(f"   CPC preview: {patent['cpc_str'][:150]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}]}

exec(code, env_args)

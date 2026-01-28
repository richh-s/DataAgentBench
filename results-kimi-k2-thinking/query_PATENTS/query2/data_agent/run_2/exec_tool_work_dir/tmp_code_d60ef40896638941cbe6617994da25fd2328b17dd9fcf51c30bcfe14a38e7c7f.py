code = """import json
import pandas as pd
import re
from collections import defaultdict
from datetime import datetime

# Load the data from the file
file_path = locals()['var_functions.query_db:14']

if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        patents_2019 = json.load(f)
else:
    patents_2019 = file_path

print(f"Total 2019 patents found: {len(patents_2019)}")

# Function to extract month from grant_date
def extract_month(grant_date):
    if not grant_date:
        return None
    # Common patterns: "14th Mar 2019", "2019 on Jul 12th", "July 8th, 2019", "on September 3rd, 2019"
    # Extract month using regex
    month_patterns = [
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*',
        r'(January|February|March|April|May|June|July|August|September|October|November|December)'
    ]
    for pattern in month_patterns:
        match = re.search(pattern, grant_date, re.IGNORECASE)
        if match:
            month_str = match.group(1).lower()
            # Map to month numbers
            month_map = {
                'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
                'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
                'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
            }
            return month_map.get(month_str)
    return None

# Function to check if grant date is in second half of 2019
def is_second_half_2019(grant_date):
    month = extract_month(grant_date)
    return month is not None and month >= 7  # July to December

# Filter for second half 2019 patents and Germany (DE)
de_patents_2019 = []
second_half_count = 0

for patent in patents_2019:
    grant_date = patent.get('grant_date', '')
    patents_info = patent.get('Patents_info', '')
    
    # Check if granted in second half of 2019
    if is_second_half_2019(grant_date):
        second_half_count += 1
        # Check if it's a Germany patent
        if 'DE-' in patents_info or 'from DE' in patents_info:
            de_patents_2019.append(patent)

print(f"Total patents granted in second half 2019: {second_half_count}")
print(f"German patents in second half 2019: {len(de_patents_2019)}")

if len(de_patents_2019) == 0:
    print("No German patents found in second half 2019")
    print("Sample grant_date formats:")
    for i, patent in enumerate(patents_2019[:10]):
        month = extract_month(patent.get('grant_date', ''))
        print(f"  {i+1}: {patent.get('grant_date', 'N/A')} -> Month: {month}")
    print("Sample Patents_info for DE:")
    for i, patent in enumerate(patents_2019):
        if 'DE-' in patent.get('Patents_info', '') or 'from DE' in patent.get('Patents_info', ''):
            print(f"  Grant date: {patent.get('grant_date', 'N/A')}")
            print(f"  Info: {patent.get('Patents_info', 'N/A')}")
            if i >= 5:
                break

# Also check for 'DE' in the patents_info more broadly
de_all = []
for patent in patents_2019:
    patents_info = patent.get('Patents_info', '')
    if 'DE' in patents_info:
        de_all.append(patent)

print(f"\nPatents mentioning 'DE': {len(de_all)}")
if de_all:
    print("Sample DE patents:")
    for i, patent in enumerate(de_all[:5]):
        print(f"  {i+1}: {patent.get('grant_date', 'N/A')} - {patent.get('Patents_info', 'N/A')}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

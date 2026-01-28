code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load the data from the file
file_path = locals()['var_functions.query_db:14']

if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        patents_2019 = json.load(f)
else:
    patents_2019 = file_path

print("Total 2019 patents found: " + str(len(patents_2019)))

# Function to extract month from grant_date
def extract_month(grant_date):
    if not grant_date:
        return None
    month_patterns = [
        r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*',
        r'(January|February|March|April|May|June|July|August|September|October|November|December)'
    ]
    for pattern in month_patterns:
        match = re.search(pattern, grant_date, re.IGNORECASE)
        if match:
            month_str = match.group(1).lower()
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
    return month is not None and month >= 7

# Filter for second half 2019 patents and Germany (DE)
de_patents_2019 = []
second_half_count = 0

for patent in patents_2019:
    grant_date = patent.get('grant_date', '')
    patents_info = patent.get('Patents_info', '')
    
    if is_second_half_2019(grant_date):
        second_half_count += 1
        if 'DE-' in patents_info or 'from DE' in patents_info:
            de_patents_2019.append(patent)

print("Total patents granted in second half 2019: " + str(second_half_count))
print("German patents in second half 2019: " + str(len(de_patents_2019)))

# Look for German patents differently if we didn't find any
if len(de_patents_2019) == 0:
    print("No German patents found with 'DE-' pattern, checking all patents with 'DE'...")
    de_all = []
    for patent in patents_2019:
        patents_info = patent.get('Patents_info', '')
        if is_second_half_2019(patent.get('grant_date', '')) and 'DE' in patents_info:
            de_all.append(patent)
    
    print("Patents in second half mentioning 'DE': " + str(len(de_all)))
    if de_all:
        print("Sample DE patents:")
        for i in range(min(5, len(de_all))):
            print("  " + str(i+1) + ": " + de_all[i].get('grant_date', 'N/A') + " - " + de_all[i].get('Patents_info', 'N/A'))
    
    # Try to manually find some examples
    print("\\nManual search examples:")
    de_examples = []
    for patent in patents_2019:
        info = patent.get('Patents_info', '')
        grant = patent.get('grant_date', '')
        month = extract_month(grant)
        if month and month >= 7:
            if 'from DE' in info or (info.startswith('Patent') and 'DE-' in info):
                de_examples.append(patent)
    
    print("Manual DE examples found: " + str(len(de_examples)))

# Check CPC codes manually to ensure we can parse them
print("\\nChecking CPC parsing:")
cmp = 0
for patent in patents_2019:
    cpc = patent.get('cpc', '')
    if cpc:
        print("CPC sample " + str(cmp) + ": " + cpc[:100])
        cmp += 1
        if cmp >= 3:
            break"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

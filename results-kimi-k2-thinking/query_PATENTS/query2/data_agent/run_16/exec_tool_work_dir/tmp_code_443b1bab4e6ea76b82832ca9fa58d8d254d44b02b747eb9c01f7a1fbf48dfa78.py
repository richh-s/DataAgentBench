code = """import json
import re
from datetime import datetime

# Load the data from file
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    data = json.load(f)

# Function to parse grant dates
def parse_grant_date(date_str):
    if not date_str:
        return None
    # Handle various formats like "14th Mar 2019", "2019 on Jul 12th", "on October 31st, 2019"
    date_str = date_str.lower().strip()
    date_str = re.sub(r'(\d+)(th|rd|st|nd)', r'\1', date_str)
    date_str = date_str.replace('on ', '').replace('dated ', '').strip()
    
    # Try to extract month and year
    month_patterns = [
        (r'jan(?:uary)?', '01'),
        (r'feb(?:ruary)?', '02'),
        (r'mar(?:ch)?', '03'),
        (r'apr(?:il)?', '04'),
        (r'may', '05'),
        (r'june?', '06'),
        (r'july?', '07'),
        (r'aug(?:ust)?', '08'),
        (r'sep(?:tember)?', '09'),
        (r'oct(?:ober)?', '10'),
        (r'nov(?:ember)?', '11'),
        (r'dec(?:ember)?', '12')
    ]
    
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None
    
    year = year_match.group(1)
    
    for pattern, month_num in month_patterns:
        if re.search(pattern, date_str):
            # Try to find day
            day_match = re.search(r'\b(\d{1,2})\b', date_str)
            day = day_match.group(1) if day_match else '01'
            day = day.zfill(2)
            return f"{year}-{month_num}-{day}"
    
    return None

# Filter for Germany patents granted in second half of 2019
germany_patents = []
for record in data:
    patents_info = record.get('Patents_info', '').lower()
    if 'de' not in patents_info:
        continue
    
    grant_date_str = record.get('grant_date')
    if not grant_date_str:
        continue
    
    parsed_date = parse_grant_date(grant_date_str)
    if not parsed_date:
        continue
    
    try:
        grant_date = datetime.strptime(parsed_date, '%Y-%m-%d')
        if grant_date.year == 2019 and grant_date.month >= 7:
            germany_patents.append({
                'grant_date': grant_date,
                'cpc_json': record.get('cpc', '[]'),
                'patents_info': record.get('Patents_info', '')
            })
    except:
        continue

print(f"Found {len(germany_patents)} Germany patents granted in second half of 2019")
print(f"Sample: {germany_patents[:2]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'total': '23985', 'MIN(grant_date)': '10th Apr 1945', 'MAX(grant_date)': 'on September 9th, 2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

code = """import json
import re
from datetime import datetime
from collections import defaultdict

# Load the data from the query result
file_path = locals()['var_functions.query_db:20']
with open(file_path, 'r') as f:
    data = json.load(f)

# Function to parse grant dates
def parse_grant_date(date_str):
    if not date_str:
        return None
    
    date_str = date_str.lower().strip()
    date_str = re.sub(r'(\d+)(th|rd|st|nd)', r'\1', date_str)
    date_str = date_str.replace('on ', '').replace('dated ', '').strip()
    
    month_patterns = [
        (r'jan(?:uary)?', 1), (r'feb(?:ruary)?', 2), (r'mar(?:ch)?', 3),
        (r'apr(?:il)?', 4), (r'may', 5), (r'june?', 6),
        (r'july?', 7), (r'aug(?:ust)?', 8), (r'sep(?:tember)?', 9),
        (r'oct(?:ober)?', 10), (r'nov(?:ember)?', 11), (r'dec(?:ember)?', 12)
    ]
    
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None
    
    year = int(year_match.group(1))
    
    for pattern, month_num in month_patterns:
        if re.search(pattern, date_str):
            day_match = re.search(r'\b(\d{1,2})\b', date_str)
            day = int(day_match.group(1)) if day_match else 1
            return datetime(year, month_num, day)
    
    return None

# Filter for Germany patents granted in second half of 2019
germany_patents = []
for record in data:
    patents_info = record.get('Patents_info', '')
    if not patents_info or 'DE-' not in patents_info:
        continue
    
    grant_date_str = record.get('grant_date')
    if not grant_date_str:
        continue
    
    grant_date = parse_grant_date(grant_date_str)
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        germany_patents.append({
            'grant_date': grant_date,
            'cpc_json': record.get('cpc', '[]'),
            'patents_info': patents_info
        })

# Extract CPC level 4 codes
cpc_level4_counts = defaultdict(int)
cpc_level4_codes = set()

for patent in germany_patents:
    cpc_data = patent['cpc_json']
    
    try:
        if isinstance(cpc_data, str):
            cpc_list = json.loads(cpc_data)
        else:
            cpc_list = cpc_data
            
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                # Extract level 4 CPC code (first 4 characters of the main group)
                parts = code.split('/')
                if len(parts) == 2:
                    main_group = parts[0]
                    if len(main_group) >= 4:
                        level4_code = main_group[:4]
                        cpc_level4_counts[level4_code] += 1
                        cpc_level4_codes.add(level4_code)
    except:
        continue

print(f"Unique CPC level 4 codes: {len(cpc_level4_codes)}")
print(f"Top CPC codes: {sorted(cpc_level4_counts.items(), key=lambda x: x[1], reverse=True)[:10]}")

# Save CPC codes for querying the definition database
cpc_codes_list = sorted(list(cpc_level4_codes))
print("__RESULT__:")
print(json.dumps(cpc_codes_list))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'total': '23985', 'MIN(grant_date)': '10th Apr 1945', 'MAX(grant_date)': 'on September 9th, 2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 111, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_patents': 34, 'years': [2019], 'sample_data': {'2019': {'B41F': 3, 'F02D': 16, 'F02M': 11, 'F04B': 2, 'G01D': 1, 'B23K': 1, 'B63B': 1, 'H04W': 22, 'H04L': 16, 'Y02D': 2, 'B66C': 1, 'E02F': 6, 'B60S': 1, 'Y02T': 4, 'F16C': 3, 'A47J': 1, 'A21C': 1, 'A61F': 6, 'A43B': 5, 'F24B': 3, 'F23L': 6, 'F23B': 4, 'F23N': 1, 'Y02E': 1, 'H01J': 10, 'G01M': 4, 'F05D': 2, 'F04D': 1, 'F16F': 1, 'F01D': 2, 'H01R': 6, 'B64D': 1, 'B60R': 1, 'H01L': 6, 'B62D': 2, 'F02N': 7, 'B60K': 3, 'B60W': 1, 'C04B': 45, 'C09K': 2, 'B29C': 19, 'A61B': 5, 'G01N': 2, 'A61L': 2, 'G02B': 20, 'H01F': 4, 'F02P': 4, 'Y10T': 2, 'G07C': 2, 'B29D': 1, 'H01H': 4, 'E05B': 1, 'G01L': 4, 'G01F': 2, 'F16H': 5, 'F16D': 3, 'H02J': 6, 'H03L': 6, 'B60N': 3, 'F42B': 2, 'F41H': 2, 'G08B': 2}}}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

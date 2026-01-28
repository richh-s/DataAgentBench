code = """import json
import pandas as pd
import re
from collections import defaultdict

# Read the data from the file
file_path = locals()['var_functions.query_db:8']

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and dates
cpc_data = []

for record in data:
    # Parse publication date to get year and month
    pub_date = record['publication_date']
    # Extract year from the date string
    year_match = re.search(r'2019', pub_date)
    if year_match:
        year = 2019
        # Try to extract month
        month_patterns = [
            (r'July|Jul', 7),
            (r'August|Aug', 8),
            (r'September|Sep', 9),
            (r'October|Oct', 10),
            (r'November|Nov', 11),
            (r'December|Dec', 12)
        ]
        
        month = None
        for pattern, month_num in month_patterns:
            if re.search(pattern, pub_date, re.IGNORECASE):
                month = month_num
                break
        
        # Parse CPC codes (JSON string)
        cpc_json = record['cpc']
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_item in cpc_list:
                full_code = cpc_item['code']
                # Extract level 4 CPC (group level, e.g., A01B1/00 from A01B1/002)
                # Level 4 is the group before the last slash group
                parts = full_code.split('/')
                if len(parts) >= 2:
                    # Take the subclass + group (e.g., A01B1)
                    subclass_part = parts[0]
                    if len(subclass_part) >= 4:
                        # This should be level 4: subclass + group
                        level4_code = subclass_part
                        cpc_data.append({
                            'year': year,
                            'month': month,
                            'cpc_code': level4_code,
                            'full_code': full_code
                        })
        except:
            continue

# Create DataFrame
df = pd.DataFrame(cpc_data)
print('__RESULT__:')
print(f'Total records: {len(df)}')
print(f'Unique CPC codes: {df["cpc_code"].nunique()}')
print(df.head(10).to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'publication_date': '21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'publication_date': 'December the 5th, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'publication_date': 'on August 22nd, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:18': []}

exec(code, env_args)

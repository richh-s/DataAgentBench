code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the data
result_file = locals()['var_functions.query_db:9']
with open(result_file, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Look at grant date patterns for Germany patents
sample_dates = []
germany_patents_2019 = []

for idx, row in df.iterrows():
    patents_info = str(row['Patents_info'])
    if 'DE-' in patents_info:
        grant_date_str = str(row['grant_date'])
        
        # Check if it's from 2019
        if '2019' in grant_date_str:
            sample_dates.append({
                'patent_info': patents_info,
                'grant_date_raw': grant_date_str,
                'cpc': row['cpc']
            })
        
        # Try to parse more flexibly
        if '2019' in grant_date_str:
            # Extract month
            month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date_str, re.IGNORECASE)
            if month_match:
                month_str = month_match.group(1).capitalize()
                month_map = {
                    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
                }
                month_num = month_map.get(month_str, 0)
                
                if month_num >= 7:  # Second half
                    germany_patents_2019.append({
                        'patent_info': patents_info,
                        'grant_date_raw': grant_date_str,
                        'month': month_num,
                        'cpc': row['cpc']
                    })

print('__RESULT__:')
print(json.dumps({
    "sample_dates_2019": sample_dates[:5],
    "second_half_count": len(germany_patents_2019),
    "sample_second_half": germany_patents_2019[:3]
}))"""

env_args = {'var_functions.list_db:2': ['publicationinfo'], 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'count': 0, 'sample': []}, 'var_functions.execute_python:12': {'total_records': 3838, 'germany_patents_found': 50, 'sample_germany': [{'info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.execute_python:14': {'germany_patents_second_half_2019': 0, 'sample': []}}

exec(code, env_args)

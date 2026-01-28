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

# Filter for Germany patents granted in second half of 2019
germany_patents = []

for idx, row in df.iterrows():
    # Check if it's a Germany patent
    patents_info = str(row['Patents_info'])
    if 'DE-' not in patents_info:
        continue
    
    # Parse grant date
    grant_date_str = str(row['grant_date'])
    if not grant_date_str or pd.isna(grant_date_str) or grant_date_str == 'None':
        continue
    
    # Clean and parse date
    cleaned_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', grant_date_str)
    cleaned_date = cleaned_date.replace('on ', '').replace('dated ', '')
    
    try:
        # Try multiple date formats
        date_formats = ['%d %b %Y', '%b %d %Y', '%d %B %Y', '%B %d %Y']
        grant_date = None
        for fmt in date_formats:
            try:
                grant_date = datetime.strptime(cleaned_date, fmt)
                break
            except:
                continue
        
        if grant_date is None:
            continue
            
        # Check if in second half of 2019
        if grant_date.year == 2019 and grant_date.month >= 7:
            germany_patents.append({
                'patent_info': patents_info,
                'grant_date': grant_date,
                'grant_year': grant_date.year,
                'grant_month': grant_date.month,
                'cpc': row['cpc']
            })
    except:
        continue

print('__RESULT__:')
print(json.dumps({
    "germany_patents_second_half_2019": len(germany_patents),
    "sample": germany_patents[:3] if germany_patents else []
}))"""

env_args = {'var_functions.list_db:2': ['publicationinfo'], 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'count': 0, 'sample': []}, 'var_functions.execute_python:12': {'total_records': 3838, 'germany_patents_found': 50, 'sample_germany': [{'info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}}

exec(code, env_args)

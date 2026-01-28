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

# Extract Germany patents and their CPC codes
Germany_cpc_data = []

for idx, row in df.iterrows():
    patents_info = str(row['Patents_info'])
    if 'DE-' not in patents_info:
        continue
    
    grant_date_str = str(row['grant_date'])
    if not grant_date_str or pd.isna(grant_date_str) or grant_date_str == 'None':
        continue
    
    if '2019' not in grant_date_str:
        continue
    
    # Extract month
    month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date_str, re.IGNORECASE)
    if month_match:
        month_str = month_match.group(1).capitalize()
        month_map = {
            'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
            'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
        }
        month_num = month_map.get(month_str, 0)
        
        if month_num >= 7:  # Second half of 2019
            # Extract CPC codes
            cpc_str = str(row['cpc'])
            if cpc_str and cpc_str != 'None':
                try:
                    cpc_list = json.loads(cpc_str)
                    for cpc_item in cpc_list:
                        if isinstance(cpc_item, dict) and 'code' in cpc_item:
                            cpc_code = cpc_item['code']
                            # Extract level 4 group (format: XNNN/NN or XNNNN/NN)
                            # Level 4 is the subgroup before the slash
                            if '/' in cpc_code:
                                group_part = cpc_code.split('/')[0]
                                # Get first 4 characters for level 4 group
                                if len(group_part) >= 4:
                                    level_4_group = group_part[:4]
                                    Germany_cpc_data.append({
                                        'patent_info': patents_info,
                                        'grant_date': grant_date_str,
                                        'grant_month': month_num,
                                        'cpc_full': cpc_code,
                                        'cpc_level4': level_4_group,
                                        'year': 2019
                                    })
                except:
                    # Try to parse manually if JSON parsing fails
                    cpc_matches = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
                    for cpc_code in cpc_matches:
                        if '/' in cpc_code:
                            group_part = cpc_code.split('/')[0]
                            if len(group_part) >= 4:
                                level_4_group = group_part[:4]
                                Germany_cpc_data.append({
                                    'patent_info': patents_info,
                                    'grant_date': grant_date_str,
                                    'grant_month': month_num,
                                    'cpc_full': cpc_code,
                                    'cpc_level4': level_4_group,
                                    'year': 2019
                                })

print('Germany CPC data extracted:', len(Germany_cpc_data))
print('Unique CPC level 4 groups:', len(set([x['cpc_level4'] for x in Germany_cpc_data])))

# Get unique CPC level 4 groups to query definitions
cpc_level4_groups = list(set([x['cpc_level4'] for x in Germany_cpc_data]))

print('__RESULT__:')
print(json.dumps({
    'total_records': len(Germany_cpc_data),
    'unique_level4_groups': len(cpc_level4_groups),
    'sample_records': Germany_cpc_data[:5],
    'cpc_level4_list': cpc_level4_groups
}))"""

env_args = {'var_functions.list_db:2': ['publicationinfo'], 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'count': 0, 'sample': []}, 'var_functions.execute_python:12': {'total_records': 3838, 'germany_patents_found': 50, 'sample_germany': [{'info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.execute_python:14': {'germany_patents_second_half_2019': 0, 'sample': []}, 'var_functions.execute_python:16': {'sample_dates_2019': [{'patent_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date_raw': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date_raw': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date_raw': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date_raw': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date_raw': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'second_half_count': 24, 'sample_second_half': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date_raw': 'dated 21st November 2019', 'month': 11, 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date_raw': '5th of December, 2019', 'month': 12, 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date_raw': '22nd of August, 2019', 'month': 8, 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}]}}

exec(code, env_args)

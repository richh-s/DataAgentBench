code = """import json
import re
from datetime import datetime

# Load the DE 2019 patents data
result_file = locals()['var_functions.query_db:18']
with open(result_file, 'r') as f:
    patents_data = json.load(f)

# Filter for second half of 2019 (July-December)
def parse_grant_date(date_str):
    if not date_str:
        return None
    # Extract month from various date formats
    month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', date_str, re.IGNORECASE)
    if month_match:
        month_name = month_match.group(1).lower()
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        return month_map.get(month_name, 0)
    return 0

# Filter patents
second_half_patents = []
for patent in patents_data:
    grant_date = patent.get('grant_date', '')
    month = parse_grant_date(grant_date)
    if month >= 7:  # July to December
        second_half_patents.append(patent)

print('__RESULT__:')
print(json.dumps({
    'total_de_2019': len(patents_data),
    'second_half_2019': len(second_half_patents),
    'sample_patent': second_half_patents[0] if second_half_patents else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_records': 68, 'sample_cpc_codes': ['H02J1/10', 'H02J7/34', 'H02J7/007182', 'H02J1/10', 'H02J7/34', 'H02J7/007182'], 'sample_grant_date': '14th Aug 2019'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_records': 68, 'first_few': [{'Patents_info': 'Patent application (ID DE-102009033309-A) from DE, assigned to CONTINENTAL AUTOMOTIVE GMBH, with pub. number DE-102009033309-B4.', 'grant_date': '14th Aug 2019', 'cpc': '[\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)

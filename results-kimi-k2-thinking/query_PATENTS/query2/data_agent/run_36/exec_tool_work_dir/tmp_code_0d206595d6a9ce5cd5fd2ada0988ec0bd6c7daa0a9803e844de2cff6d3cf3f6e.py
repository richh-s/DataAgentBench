code = """import json
import pandas as pd
import re
from datetime import datetime
from collections import defaultdict
import numpy as np

# Read the full result from the file
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Parse grant dates and filter for second half of 2019 (July-December)
second_half_patents = []
month_pattern = r'(July|August|September|October|November|December|Sept)'

for patent in patents_data:
    grant_date = patent.get('grant_date', '')
    # Check if grant date contains second half months
    if re.search(month_pattern, grant_date, re.IGNORECASE):
        second_half_patents.append(patent)
    # Also check numeric months
    elif any(str(month) in grant_date for month in range(7, 13)):
        second_half_patents.append(patent)

print('__RESULT__:')
print(json.dumps(f'Filtered to {len(second_half_patents)} patents granted in second half of 2019'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.execute_python:8': {'total_patents': 5, 'sample_keys': ['Patents_info', 'kind_code', 'application_kind', 'pct_number', 'family_id', 'title_localized', 'abstract_localized', 'claims_localized_html', 'description_localized_html', 'publication_date', 'filing_date', 'grant_date', 'priority_date', 'priority_claim', 'inventor_harmonized', 'examiner', 'uspc', 'ipc', 'cpc', 'citation', 'parent', 'child', 'entity_status', 'art_unit'], 'grant_date_sample': '14th Mar 2019', 'patents_info_sample': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc_sample': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'var_functions.execute_python:10': 'Loaded 5 patents for initial analysis', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 50 German patents from 2019'}

exec(code, env_args)

code = """import json
import pandas as pd
import re
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np

# Read the full result from the file
file_path = locals()['var_functions.query_db:30']
with open(file_path, 'r') as f:
    patents_data = json.load(f)

print('__RESULT__:')
print(json.dumps(f'Total German patents: {len(patents_data)}'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.execute_python:8': {'total_patents': 5, 'sample_keys': ['Patents_info', 'kind_code', 'application_kind', 'pct_number', 'family_id', 'title_localized', 'abstract_localized', 'claims_localized_html', 'description_localized_html', 'publication_date', 'filing_date', 'grant_date', 'priority_date', 'priority_claim', 'inventor_harmonized', 'examiner', 'uspc', 'ipc', 'cpc', 'citation', 'parent', 'child', 'entity_status', 'art_unit'], 'grant_date_sample': '14th Mar 2019', 'patents_info_sample': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc_sample': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'var_functions.execute_python:10': 'Loaded 5 patents for initial analysis', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 50 German patents from 2019', 'var_functions.execute_python:16': 'Filtered to 50 patents granted in second half of 2019', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'Total German patents in 2019: 50', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.execute_python:28': 'Total German patents in 2019: 50', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)

code = """import json
import re
from collections import defaultdict

# Load the data
patents_file = locals()['var_functions.query_db:20']
with open(patents_file, 'r') as f:
    patents_2019 = json.load(f)

# Load CPC level 4 definitions
cpc_file = locals()['var_functions.query_db:28']
with open(cpc_file, 'r') as f:
    cpc_level4 = json.load(f)

# Create mapping of level 4 codes to titles
cpc_titles = {}
for cpc in cpc_level4:
    symbol = cpc['symbol']
    title = cpc['titleFull']
    cpc_titles[symbol] = title

print(f"Total patents in 2019: {len(patents_2019)}")
print(f"Total CPC level 4 codes: {len(cpc_titles)}")
print(f"Sample CPC titles: {list(cpc_titles.items())[:5]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)

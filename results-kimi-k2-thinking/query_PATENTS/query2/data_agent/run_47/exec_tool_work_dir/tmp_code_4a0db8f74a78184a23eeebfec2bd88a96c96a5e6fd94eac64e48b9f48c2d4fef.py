code = """import json
import os

# Check what variables we have
all_vars = locals()
query36_key = None
query28_key = None

for key in all_vars:
    if 'query_db:36' in str(key):
        query36_key = key
    if 'query_db:28' in str(key):
        query28_key = key

print('Keys found:', query36_key, query28_key)
print('Values:', all_vars.get(query36_key), all_vars.get(query28_key))

# Try to open files
if query36_key and query28_key:
    try:
        with open(all_vars[query36_key], 'r') as f:
            patents_data = json.load(f)
        print('Patents loaded:', len(patents_data))
        
        with open(all_vars[query28_key], 'r') as f:
            cpc_data = json.load(f)
        print('CPC definitions loaded:', len(cpc_data))
        
        # Show sample data
        print('Sample patent:', patents_data[0] if patents_data else 'None')
        print('Sample CPC:', cpc_data[0] if cpc_data else 'None')
        
    except Exception as e:
        print('Error:', e)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': []}

exec(code, env_args)

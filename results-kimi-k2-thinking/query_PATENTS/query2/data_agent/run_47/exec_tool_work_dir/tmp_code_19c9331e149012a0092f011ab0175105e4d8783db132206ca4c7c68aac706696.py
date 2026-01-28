code = """import json

patents_file = locals()['var_functions.query_db:20']
with open(patents_file, 'r') as f:
    patents_2019 = json.load(f)

# Check one patent structure
sample_patent = patents_2019[0]
sample_cpc = sample_patent.get('cpc', '')
print(f"Sample CPC field: {repr(sample_cpc)}"[:100])
print(f"Type: {type(sample_cpc)}")

# Try to parse it
if sample_cpc:
    # Remove JSON formatting
    cleaned = sample_cpc.replace('\n', '').replace('  ', '')
    if '[' in cleaned:
        # Try to parse as JSON
        import ast
        try:
            parsed = ast.literal_eval(cleaned)
            print(f"Parsed sample: {parsed}")
        except Exception as e:
            print(f"Parse error: {e}")
            print(f"Cleaned: {cleaned[:100]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)

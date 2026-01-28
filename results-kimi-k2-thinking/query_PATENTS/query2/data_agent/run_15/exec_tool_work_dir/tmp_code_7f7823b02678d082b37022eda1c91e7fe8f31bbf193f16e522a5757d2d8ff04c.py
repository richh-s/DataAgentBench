code = """import json
import re

# Load the query result
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    patents_data = json.load(f)

# Check for Germany patents - Germany can be identified by DE in Patents_info
pattern = r'\bDE[-\d]'
german_patents = [p for p in patents_data if re.search(pattern, p['Patents_info'])]

# Check structure of CPC codes
cpc_parsable = False
if patents_data:
    cpc_data = patents_data[0]['cpc']
    if isinstance(cpc_data, str) and cpc_data.strip().startswith('['):
        try:
            cpc_list = json.loads(cpc_data)
            cpc_parsable = True
        except:
            cpc_parsable = False

result = {
    'total_patents': len(patents_data),
    'german_patents': len(german_patents),
    'cpc_parsable': cpc_parsable
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

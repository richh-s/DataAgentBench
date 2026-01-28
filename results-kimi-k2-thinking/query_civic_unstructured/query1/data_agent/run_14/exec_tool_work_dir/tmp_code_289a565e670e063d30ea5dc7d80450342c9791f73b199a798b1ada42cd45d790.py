code = """import json
import re

# Load data
funding_file = globals()['var_functions.query_db:4']
civic_file = globals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a dictionary of funding amounts by project name for easy lookup
funding_dict = {}
for record in funding_data:
    try:
        amount = int(record['Amount'])
        if amount > 50000:
            funding_dict[record['Project_Name']] = amount
    except:
        continue

print("__RESULT__:")
print(json.dumps({
    "projects_with_funding": len(funding_dict),
    "sample_projects": list(funding_dict.keys())[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}}

exec(code, env_args)

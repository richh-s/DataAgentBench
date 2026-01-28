code = """import json

# Load funding data (projects with >$50,000 funding)
funding_path = locals()['var_functions.query_db:64']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:40']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('DEBUG: Total funding records:', len(funding_records))
print('DEBUG: Total civic documents:', len(civic_docs))

# Create a dictionary mapping project names for funding > $50,000
high_funding_projects = {}
for record in funding_records:
    project_name = record['Project_Name']
    print('DEBUG: Processing funding record:', project_name)
    # The amount field might not have 'Amount' key, check structure
    break

# Let's check the structure first
if funding_records:
    print('DEBUG: First record structure:', json.dumps(funding_records[0], indent=2)[:500])

# Print last result for error analysis key
print('__LAST_RESULT_FOR_ERROR_ANALYSIS__')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)

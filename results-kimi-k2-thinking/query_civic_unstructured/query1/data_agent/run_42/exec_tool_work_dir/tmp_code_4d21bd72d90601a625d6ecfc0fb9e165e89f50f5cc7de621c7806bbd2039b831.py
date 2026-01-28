code = """import json

# Load funding data
funding_path = var_functions.query_db_6
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Total funding records:', len(funding_data))

# Count projects with amount > 50000
count_over_50k = sum(1 for f in funding_data if f['Amount'] > 50000)
print('Count > $50k:', count_over_50k)

# Print some sample project names
print('\nSample projects:')
for f in funding_data[:20]:
    print(f"{f['Project_Name']}: ${f['Amount']}")

__RESULT__:
print(json.dumps(count_over_50k))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

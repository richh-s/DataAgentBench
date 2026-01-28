code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print("Total funding records:", len(funding_data))
print("\nFirst 10 funding records:")
for i, record in enumerate(funding_data[:10]):
    print(f"{i+1}. {record['Project_Name'][:80]}... - ${record['Amount']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

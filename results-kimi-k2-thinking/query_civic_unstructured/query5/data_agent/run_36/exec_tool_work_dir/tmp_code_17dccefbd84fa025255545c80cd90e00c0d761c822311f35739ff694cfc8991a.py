code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:6']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "total_records": len(funding_data),
    "sample_records": funding_data[:3]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

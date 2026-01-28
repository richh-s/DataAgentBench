code = """import json

# Read the civic docs data
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
with open('var_functions.query_db:6', 'r') as f:
    funding_data = json.load(f)

print("__RESULT__:")
result = {
    "civic_docs_count": len(civic_docs),
    "funding_records_count": len(funding_data),
    "first_funding_record": funding_data[0] if funding_data else None
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

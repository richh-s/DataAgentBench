code = """import json
# var_call_3vqypdr0QQc14xdetLDUAzMO is provided in storage and contains the path to the JSON file
p = var_call_3vqypdr0QQc14xdetLDUAzMO
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
# data is a list of records like {"repo_name": "owner/repo"}
repo_names = [rec['repo_name'] for rec in data if 'repo_name' in rec]
# Build SQL IN clause safely by doubling any single quotes
escaped = [rn.replace("'", "''") for rn in repo_names]
# If too many items, DuckDB may accept a large IN; we'll proceed
in_list = ",".join([f"'{e}'" for e in escaped])
in_clause = f"({in_list})" if in_list else "('')"
result = {'in_clause': in_clause, 'count_repos': len(repo_names)}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3vqypdr0QQc14xdetLDUAzMO': 'file_storage/call_3vqypdr0QQc14xdetLDUAzMO.json'}

exec(code, env_args)

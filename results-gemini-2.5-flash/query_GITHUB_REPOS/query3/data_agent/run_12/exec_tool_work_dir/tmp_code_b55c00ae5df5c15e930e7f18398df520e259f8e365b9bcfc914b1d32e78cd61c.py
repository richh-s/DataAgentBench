code = """import pandas as pd
import json

with open(locals()['var_function-call-16630310231902441811'], 'r') as f:
    repo_names_data = json.load(f)

repo_names_df = pd.DataFrame(repo_names_data)
repo_names_list = repo_names_df['repo_name'].tolist()

repo_names_in_clause = ', '.join([f"'{repo}'" for repo in repo_names_list])

query = "SELECT COUNT(message) FROM commits WHERE repo_name IN ({}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND NOT (LOWER(message) LIKE 'merge%' OR LOWER(message) LIKE 'update%' OR LOWER(message) LIKE 'test%');".format(repo_names_in_clause)

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-16630310231902441811': 'file_storage/function-call-16630310231902441811.json'}

exec(code, env_args)

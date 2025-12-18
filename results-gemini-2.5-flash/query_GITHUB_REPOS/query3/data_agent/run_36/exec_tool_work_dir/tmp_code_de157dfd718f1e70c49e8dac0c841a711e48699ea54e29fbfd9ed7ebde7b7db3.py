code = """import pandas as pd
import json

with open(locals()['var_function-call-11954184868757041233'], 'r') as f:
    repo_names_data = json.load(f)

repo_names_df = pd.DataFrame(repo_names_data)
repo_names = repo_names_df['repo_name'].tolist()

# Prepare the list of repo names for SQL IN clause
repo_names_str = ', '.join([f"'{name}'" for name in repo_names])

sql_query = f"""
SELECT COUNT(message)
FROM commits
WHERE repo_name IN ({repo_names_str})
  AND message IS NOT NULL
  AND LENGTH(message) < 1000
  AND NOT (LOWER(message) LIKE 'merge%' OR LOWER(message) LIKE 'update%' OR LOWER(message) LIKE 'test%');
"""

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-11954184868757041233': 'file_storage/function-call-11954184868757041233.json'}

exec(code, env_args)

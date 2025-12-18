code = """import pandas as pd
import json

unique_project_names = json.loads(locals()['var_function-call-17411513133372805238'])

# Construct the WHERE clause for the DuckDB query
# Escaping single quotes in project names for SQL IN clause
project_names_escaped = [name.replace("'", "''") for name in unique_project_names]
project_names_str = ', '.join([f"'{name}'" for name in project_names_escaped])

duckdb_query = f"SELECT Project_Information FROM project_info WHERE ProjectName IN ({project_names_str}) AND Project_Information LIKE '%github.com/%' AND Project_Information LIKE '%forks:%';"

print("__RESULT__:")
print(json.dumps(duckdb_query))"""

env_args = {'var_function-call-9550500136309637979': ['project_info', 'project_packageversion'], 'var_function-call-9646753308636010247': 'file_storage/function-call-9646753308636010247.json', 'var_function-call-937077842083223208': 'file_storage/function-call-937077842083223208.json', 'var_function-call-8194439917375433551': 'file_storage/function-call-8194439917375433551.json', 'var_function-call-16374127340173290672': [], 'var_function-call-17411513133372805238': 'file_storage/function-call-17411513133372805238.json'}

exec(code, env_args)

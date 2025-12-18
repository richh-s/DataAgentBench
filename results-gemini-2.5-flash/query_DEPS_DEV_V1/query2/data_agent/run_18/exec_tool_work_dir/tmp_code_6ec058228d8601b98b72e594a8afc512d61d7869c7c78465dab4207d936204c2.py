code = """import pandas as pd
import json

# Load data from storage keys
packageinfo_df = pd.read_json(locals()['var_function-call-9646753308636010247'])
project_packageversion_df = pd.read_json(locals()['var_function-call-937077842083223208'])

# Merge the two dataframes on 'Name' and 'Version'
merged_df = pd.merge(packageinfo_df, project_packageversion_df, on=['Name', 'Version'], how='inner')

# Extract unique ProjectNames
unique_project_names = merged_df['ProjectName'].unique().tolist()

# Construct the WHERE clause for the DuckDB query using IN clause for ProjectName
# Escaping single quotes in project names for SQL IN clause
project_names_escaped = [name.replace("'", "''") for name in unique_project_names]
project_names_str = ', '.join([f"'{name}'" for name in project_names_escaped])

duckdb_query = f"SELECT Project_Information, ProjectName FROM project_info WHERE ProjectName IN ({project_names_str});"

print("__RESULT__:")
print(json.dumps(duckdb_query))"""

env_args = {'var_function-call-9550500136309637979': ['project_info', 'project_packageversion'], 'var_function-call-9646753308636010247': 'file_storage/function-call-9646753308636010247.json', 'var_function-call-937077842083223208': 'file_storage/function-call-937077842083223208.json', 'var_function-call-8194439917375433551': 'file_storage/function-call-8194439917375433551.json', 'var_function-call-16374127340173290672': [], 'var_function-call-17411513133372805238': 'file_storage/function-call-17411513133372805238.json', 'var_function-call-11625479866658419654': 'file_storage/function-call-11625479866658419654.json'}

exec(code, env_args)

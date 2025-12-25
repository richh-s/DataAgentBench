code = """import pandas as pd
import json

# Read the full JSON files
with open(locals()['var_function-call-1909453510624210863'], 'r') as f:
    packageinfo_data = json.load(f)
with open(locals()['var_function-call-4332181918179202986'], 'r') as f:
    project_packageversion_data = json.load(f)

# Convert to DataFrames
df_packageinfo = pd.DataFrame(packageinfo_data)
df_project_packageversion = pd.DataFrame(project_packageversion_data)

# Merge the two dataframes on System, Name, and Version
df_merged = pd.merge(
    df_packageinfo,
    df_project_packageversion,
    on=['System', 'Name', 'Version'],
    how='inner'
)

# Get unique ProjectNames
unique_project_names = df_merged['ProjectName'].unique().tolist()

# Format for SQL IN clause
in_clause = ', '.join([f"'{name}'" for name in unique_project_names])

print('__RESULT__:')
print(json.dumps(in_clause))"""

env_args = {'var_function-call-12206847146719381538': 'file_storage/function-call-12206847146719381538.json', 'var_function-call-14239026419335040227': 'file_storage/function-call-14239026419335040227.json', 'var_function-call-1909453510624210863': 'file_storage/function-call-1909453510624210863.json', 'var_function-call-5813020761262683926': 'file_storage/function-call-5813020761262683926.json', 'var_function-call-12858218957760100097': 'file_storage/function-call-5813020761262683926.json', 'var_function-call-12952062965713530265': 'file_storage/function-call-12952062965713530265.json', 'var_function-call-4332181918179202986': 'file_storage/function-call-4332181918179202986.json'}

exec(code, env_args)

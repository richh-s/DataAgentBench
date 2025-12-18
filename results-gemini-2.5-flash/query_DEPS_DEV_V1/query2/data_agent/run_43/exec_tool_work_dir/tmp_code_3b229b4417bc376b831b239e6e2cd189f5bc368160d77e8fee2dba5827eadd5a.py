code = """import json
import pandas as pd

filtered_packages = pd.read_json(locals()['var_function-call-5722959846294498702'])
project_packageversion = pd.read_json(locals()['var_function-call-7090475900769428024'])

merged_df = pd.merge(filtered_packages, project_packageversion, on=['System', 'Name', 'Version'], how='inner')

# Keep only unique ProjectName entries to avoid redundant lookups and to consider each project once for its aggregated fork count
unique_projects = merged_df[['ProjectName']].drop_duplicates()

print("__RESULT__:")
print(unique_projects.to_json(orient='records'))"""

env_args = {'var_function-call-16763418198789656899': 'file_storage/function-call-16763418198789656899.json', 'var_function-call-5722959846294498702': 'file_storage/function-call-5722959846294498702.json', 'var_function-call-7090475900769428024': 'file_storage/function-call-7090475900769428024.json'}

exec(code, env_args)

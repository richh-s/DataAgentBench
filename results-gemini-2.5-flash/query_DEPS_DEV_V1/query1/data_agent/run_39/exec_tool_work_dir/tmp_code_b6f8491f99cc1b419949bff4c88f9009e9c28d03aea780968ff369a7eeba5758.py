code = """import pandas as pd
import json

latest_release_packages = pd.read_json(locals()['var_function-call-5524596830193667260'])
project_package_version = pd.read_json(locals()['var_function-call-4454470930749183033'])

# Merge to link packages with project names
merged_data = pd.merge(
    latest_release_packages,
    project_package_version, 
    on=['Name', 'Version'], 
    how='inner'
)

# Select relevant columns
result = merged_data[['Name', 'Version', 'ProjectName']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2542952245398537233': ['packageinfo'], 'var_function-call-10417754161782902564': 'file_storage/function-call-10417754161782902564.json', 'var_function-call-5524596830193667260': 'file_storage/function-call-5524596830193667260.json', 'var_function-call-1109682220278830328': ['project_info', 'project_packageversion'], 'var_function-call-4454470930749183033': 'file_storage/function-call-4454470930749183033.json'}

exec(code, env_args)

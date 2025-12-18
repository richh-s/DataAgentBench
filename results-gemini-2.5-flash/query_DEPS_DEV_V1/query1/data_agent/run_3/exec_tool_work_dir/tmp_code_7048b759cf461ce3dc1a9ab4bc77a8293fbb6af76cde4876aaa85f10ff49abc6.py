code = """import pandas as pd
import json

latest_releases = pd.DataFrame(json.loads(open(locals()['var_function-call-4179847827954287643'], 'r').read()))
project_packageversion = pd.DataFrame(json.loads(open(locals()['var_function-call-12412451248896417788'], 'r').read()))

# Merge to link latest releases with their project names
merged_df = pd.merge(latest_releases, project_packageversion, on=['System', 'Name', 'Version'], how='inner')

# Select relevant columns
result = merged_df[['Name', 'Version', 'ProjectName']].drop_duplicates()

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-13869052368742656528': 'file_storage/function-call-13869052368742656528.json', 'var_function-call-4179847827954287643': 'file_storage/function-call-4179847827954287643.json', 'var_function-call-12412451248896417788': 'file_storage/function-call-12412451248896417788.json'}

exec(code, env_args)

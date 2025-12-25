code = """import pandas as pd
import json

packageinfo_df = pd.read_json(locals()['var_function-call-9646753308636010247'])
project_packageversion_df = pd.read_json(locals()['var_function-call-937077842083223208'])

merged_df = pd.merge(packageinfo_df, project_packageversion_df, on=['Name', 'Version'], how='inner')

# Extract unique project names
project_names = merged_df['ProjectName'].unique().tolist()

print("__RESULT__:")
print(json.dumps(project_names))"""

env_args = {'var_function-call-9550500136309637979': ['project_info', 'project_packageversion'], 'var_function-call-9646753308636010247': 'file_storage/function-call-9646753308636010247.json', 'var_function-call-937077842083223208': 'file_storage/function-call-937077842083223208.json'}

exec(code, env_args)

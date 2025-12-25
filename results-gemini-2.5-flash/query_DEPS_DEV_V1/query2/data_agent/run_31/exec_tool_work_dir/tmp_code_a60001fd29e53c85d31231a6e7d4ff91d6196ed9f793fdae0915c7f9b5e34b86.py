code = """import pandas as pd
import json

packageinfo_df = pd.read_json(locals()['var_function-call-10559751409959478514'])
project_packageversion_df = pd.read_json(locals()['var_function-call-17045702297132480665'])

merged_df = pd.merge(packageinfo_df, project_packageversion_df, on=['System', 'Name', 'Version'], how='inner')

unique_projects = merged_df['ProjectName'].unique().tolist()

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-10559751409959478514': 'file_storage/function-call-10559751409959478514.json', 'var_function-call-17045702297132480665': 'file_storage/function-call-17045702297132480665.json'}

exec(code, env_args)

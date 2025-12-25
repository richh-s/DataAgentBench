code = """import pandas as pd
import json

package_info_path = locals()['var_function-call-13836164031795842360']
project_packageversion_path = locals()['var_function-call-15889035169845308856']

with open(package_info_path, 'r') as f:
    package_info = json.load(f)

with open(project_packageversion_path, 'r') as f:
    project_packageversion = json.load(f)

df_package = pd.DataFrame(package_info)
df_project_packageversion = pd.DataFrame(project_packageversion)

merged_df = pd.merge(df_package, df_project_packageversion, on=['System', 'Name', 'Version'], how='inner')
project_names = merged_df['ProjectName'].unique().tolist()
project_names_str = "', '".join(project_names)

print('__RESULT__:')
print(json.dumps(project_names_str))"""

env_args = {'var_function-call-13836164031795842360': 'file_storage/function-call-13836164031795842360.json', 'var_function-call-15889035169845308856': 'file_storage/function-call-15889035169845308856.json'}

exec(code, env_args)

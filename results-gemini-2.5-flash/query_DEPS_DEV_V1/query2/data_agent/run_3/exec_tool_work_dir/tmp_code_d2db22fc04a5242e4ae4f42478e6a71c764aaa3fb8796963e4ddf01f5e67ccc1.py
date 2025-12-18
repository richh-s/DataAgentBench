code = """import json
import pandas as pd

filtered_packages = pd.read_json(locals()['var_function-call-3273800166201294856'])
project_packageversion = pd.read_json(locals()['var_function-call-11115888534947939084'])

# Join the two dataframes
merged_df = pd.merge(filtered_packages, project_packageversion, on=['System', 'Name', 'Version'], how='inner')

# Get unique ProjectNames
unique_project_names = merged_df['ProjectName'].unique().tolist()

result = pd.DataFrame({'ProjectName': unique_project_names}).to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-16653849855473276997': 'file_storage/function-call-16653849855473276997.json', 'var_function-call-3273800166201294856': 'file_storage/function-call-3273800166201294856.json', 'var_function-call-11115888534947939084': 'file_storage/function-call-11115888534947939084.json'}

exec(code, env_args)

code = """import json
import pandas as pd

unique_projects_df = pd.read_json(locals()['var_function-call-288463699051273138'])
unique_project_names = unique_projects_df['ProjectName'].tolist()

# Prepare the list of project names for the SQL IN clause
project_names_str = ', '.join([f"'{name}'" for name in unique_project_names])

# Construct the SQL query
sql_query = f"SELECT ProjectName, Project_Information FROM project_info WHERE ProjectName IN ({project_names_str});"

print('__RESULT__:')
print(json.dumps(sql_query))"""

env_args = {'var_function-call-16653849855473276997': 'file_storage/function-call-16653849855473276997.json', 'var_function-call-3273800166201294856': 'file_storage/function-call-3273800166201294856.json', 'var_function-call-11115888534947939084': 'file_storage/function-call-11115888534947939084.json', 'var_function-call-288463699051273138': 'file_storage/function-call-288463699051273138.json'}

exec(code, env_args)

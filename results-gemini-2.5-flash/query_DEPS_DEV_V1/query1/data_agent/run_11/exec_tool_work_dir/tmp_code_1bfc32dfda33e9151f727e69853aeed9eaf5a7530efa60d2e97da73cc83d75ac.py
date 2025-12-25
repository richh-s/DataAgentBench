code = """import json
import pandas as pd

latest_releases_file = locals()['var_function-call-17606046641350128240']
with open(latest_releases_file, 'r') as f:
    latest_releases_data = json.load(f)
latest_releases_df = pd.DataFrame(latest_releases_data)

project_packageversion_file = locals()['var_function-call-14061627495693256134']
with open(project_packageversion_file, 'r') as f:
    project_packageversion_data = json.load(f)
project_packageversion_df = pd.DataFrame(project_packageversion_data)

# Merge to link package versions with project names
merged_df = pd.merge(latest_releases_df,
                     project_packageversion_df,
                     left_on=['Name', 'Version'],
                     right_on=['Name', 'Version'],
                     how='inner')

# Select unique ProjectName to query project_info
unique_project_names = merged_df['ProjectName'].unique().tolist()

# Split into chunks of 1000 for the SQL IN clause
chunk_size = 1000
project_name_chunks = [unique_project_names[i:i + chunk_size] for i in range(0, len(unique_project_names), chunk_size)]

# Store the chunks to be used in the next query_db call
print('__RESULT__:')
print(json.dumps(project_name_chunks))"""

env_args = {'var_function-call-15075189816740011234': 'file_storage/function-call-15075189816740011234.json', 'var_function-call-17606046641350128240': 'file_storage/function-call-17606046641350128240.json', 'var_function-call-14061627495693256134': 'file_storage/function-call-14061627495693256134.json'}

exec(code, env_args)

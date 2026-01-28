code = """import json

# Load the data from the previous query
data = var_functions.query_db:2

print('Number of UNIV CALIFORNIA patents:', len(data))

# Let's inspect the structure
if len(data) > 0:
    print('\nFirst record keys:', list(data[0].keys()))
    print('\nFirst record Patents_info:', data[0]['Patents_info'])
    print('\nFirst record citation (truncated):', str(data[0]['citation'])[:200])
    print('\nFirst record cpc (truncated):', str(data[0]['cpc'])[:200])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

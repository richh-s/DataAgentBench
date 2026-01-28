code = """import json
import pandas as pd
path = var_call_NfH6qyUofiDUnG2SC01PQ4Tb
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# keep only relevant columns and unique name-version pairs
df = df[['System','Name','Version']].drop_duplicates()
# build tuple list
tuples = []
for _, row in df.iterrows():
    name = row['Name']
    version = row['Version']
    # escape single quotes
    name_esc = name.replace("'", "''")
    version_esc = version.replace("'", "''")
    tuples.append("('NPM','{}','{}')".format(name_esc, version_esc))

if tuples:
    tuples_str = ','.join(tuples)
    query = 'SELECT "System", "Name", "Version", "ProjectName" FROM project_packageversion WHERE ("System", "Name", "Version") IN ({});'.format(tuples_str)
else:
    query = 'SELECT "System", "Name", "Version", "ProjectName" FROM project_packageversion WHERE 1=0;'

output = {'query': query}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_mtrPk4lBt9oRBdOdheZeKJcw': 'file_storage/call_mtrPk4lBt9oRBdOdheZeKJcw.json', 'var_call_NfH6qyUofiDUnG2SC01PQ4Tb': 'file_storage/call_mtrPk4lBt9oRBdOdheZeKJcw.json'}

exec(code, env_args)

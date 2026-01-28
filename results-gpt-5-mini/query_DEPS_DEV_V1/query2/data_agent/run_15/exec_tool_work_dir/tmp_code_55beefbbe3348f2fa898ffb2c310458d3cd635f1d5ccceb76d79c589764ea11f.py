code = """import json
import pandas as pd
path = var_call_NfH6qyUofiDUnG2SC01PQ4Tb
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# keep only relevant columns and unique name-version pairs
df = df[['System','Name','Version']].drop_duplicates()
# build SQL WHERE clauses
clauses = []
for _, row in df.iterrows():
    name = row['Name'].replace("'", "''")
    version = row['Version'].replace("'", "''")
    clauses.append(f'(\"System\" = \'NPM\' AND \"Name\" = \'{name}\' AND \"Version\" = \'{version}\')')

where_clause = ' OR '.join(clauses)
query = f'SELECT \"System\", \"Name\", \"Version\", \"ProjectName\" FROM project_packageversion WHERE {where_clause};'

output = {'query': query}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_mtrPk4lBt9oRBdOdheZeKJcw': 'file_storage/call_mtrPk4lBt9oRBdOdheZeKJcw.json', 'var_call_NfH6qyUofiDUnG2SC01PQ4Tb': 'file_storage/call_mtrPk4lBt9oRBdOdheZeKJcw.json'}

exec(code, env_args)

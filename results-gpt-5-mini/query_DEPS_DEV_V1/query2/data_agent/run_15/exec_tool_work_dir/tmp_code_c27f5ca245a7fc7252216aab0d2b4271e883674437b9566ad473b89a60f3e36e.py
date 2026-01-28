code = """import json
import pandas as pd
path = var_call_mtrPk4lBt9oRBdOdheZeKJcw
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
if df.empty:
    query = "SELECT \"System\", \"Name\", \"Version\", \"ProjectName\" FROM project_packageversion WHERE 1=0;"
else:
    df = df[['System','Name','Version']].drop_duplicates()
    clauses = []
    for _, row in df.iterrows():
        name = row['Name']
        version = row['Version']
        clauses.append('(\"System\" = ' + repr('NPM') + ' AND \"Name\" = ' + repr(name) + ' AND \"Version\" = ' + repr(version) + ')')
    where_clause = ' OR '.join(clauses)
    query = 'SELECT \"System\", \"Name\", \"Version\", \"ProjectName\" FROM project_packageversion WHERE ' + where_clause + ';'

output = {'query': query}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_mtrPk4lBt9oRBdOdheZeKJcw': 'file_storage/call_mtrPk4lBt9oRBdOdheZeKJcw.json'}

exec(code, env_args)

code = """import json, pandas as pd
import os

path = var_call_EjX4hpGaGchU9YWFlkuDLl7D
with open(path, 'r') as f:
    data = json.load(f)

# put into DataFrame and deduplicate
pkg_df = pd.DataFrame(data)[['System','Name','Version']].drop_duplicates()

# convert to list of tuples for SQL IN clause
values = ",".join(["('"+r.System.replace("'","''")+"','"+r.Name.replace("'","''")+"','"+r.Version.replace("'","''")+"')" for r in pkg_df.itertuples(index=False)])

chunk_size = 500
chunks = [values[i:i+100000] for i in range(0, len(values), 100000)]

result = chunks[:1]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EjX4hpGaGchU9YWFlkuDLl7D': 'file_storage/call_EjX4hpGaGchU9YWFlkuDLl7D.json', 'var_call_lCgLvuqLfK3Lg7Ht2YeWqgFf': ['project_info', 'project_packageversion'], 'var_call_XE9XcBBFM3m9C1smCcmHTU7y': []}

exec(code, env_args)

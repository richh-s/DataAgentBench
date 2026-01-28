code = """import json
# var_call_fEkrf3z6BZZaw2CYIqcvtchS is available in storage
path = var_call_fEkrf3z6BZZaw2CYIqcvtchS
with open(path, 'r') as f:
    records = json.load(f)
repo_names = [r['repo_name'] for r in records]
# sanitize single quotes in repo names
repo_names = [rn.replace("'", "''") for rn in repo_names]
# Build IN clause
chunk_size = 1000
# Build full list
in_list = ','.join("'{}'".format(rn) for rn in repo_names)
# Construct SQL for DuckDB (artifacts_database)
sql = "SELECT count(*) as message_count FROM commits WHERE repo_name IN ({}) AND message IS NOT NULL AND message <> '' AND length(message) < 1000 AND lower(ltrim(message)) NOT LIKE 'merge%' AND lower(ltrim(message)) NOT LIKE 'update%' AND lower(ltrim(message)) NOT LIKE 'test%';".format(in_list)
import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_fEkrf3z6BZZaw2CYIqcvtchS': 'file_storage/call_fEkrf3z6BZZaw2CYIqcvtchS.json'}

exec(code, env_args)

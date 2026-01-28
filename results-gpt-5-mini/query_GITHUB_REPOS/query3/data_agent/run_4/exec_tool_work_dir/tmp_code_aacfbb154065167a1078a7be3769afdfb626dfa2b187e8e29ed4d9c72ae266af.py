code = """import json
# var_call_nDatpTdGQL5akoYvA6iJHGRT contains the path to the JSON file with the metadata query result
data_path = var_call_nDatpTdGQL5akoYvA6iJHGRT
with open(data_path, 'r') as f:
    data = json.load(f)
# extract repo names
repos = sorted({rec['repo_name'] for rec in data if 'repo_name' in rec and rec['repo_name']})
# build SQL IN clause safely by escaping single quotes
def esc(s):
    return s.replace("'", "''")
values = ",".join("'{}'".format(esc(r)) for r in repos)
query = (
    "SELECT COUNT(*) AS cnt FROM commits "
    "WHERE repo_name IN (" + values + ") "
    "AND message IS NOT NULL AND message <> '' "
    "AND length(message) < 1000 "
    "AND lower(ltrim(message)) NOT LIKE 'merge%' "
    "AND lower(ltrim(message)) NOT LIKE 'update%' "
    "AND lower(ltrim(message)) NOT LIKE 'test%';"
)
import json
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_nDatpTdGQL5akoYvA6iJHGRT': 'file_storage/call_nDatpTdGQL5akoYvA6iJHGRT.json'}

exec(code, env_args)

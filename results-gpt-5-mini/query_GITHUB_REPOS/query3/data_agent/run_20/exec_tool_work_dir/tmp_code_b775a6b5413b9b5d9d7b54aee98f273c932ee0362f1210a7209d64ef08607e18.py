code = """import json
# Load the metadata query result from the provided storage file path
with open(var_call_lY7wfSXaeaWGpDtgKR0nC7mz, 'r') as f:
    data = json.load(f)
repo_names = [item['repo_name'] for item in data]
# Build an SQL query string for DuckDB (artifacts_database) to count commits
# Conditions: message exists (not null/empty), length < 1000, does not begin with merge/update/test (case-insensitive)
# Use lower(message) NOT LIKE 'merge%' etc.
# Chunk the IN list into manageable size if needed; here we include all
escaped = ["'{}'".format(r.replace("'", "''")) for r in repo_names]
in_list = ",".join(escaped)
sql = (
    "SELECT COUNT(*) AS cnt FROM commits "
    "WHERE message IS NOT NULL AND trim(message) != '' "
    "AND length(message) < 1000 "
    "AND lower(message) NOT LIKE 'merge%' "
    "AND lower(message) NOT LIKE 'update%' "
    "AND lower(message) NOT LIKE 'test%' "
    f"AND repo_name IN ({in_list});"
)
import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_lY7wfSXaeaWGpDtgKR0nC7mz': 'file_storage/call_lY7wfSXaeaWGpDtgKR0nC7mz.json'}

exec(code, env_args)

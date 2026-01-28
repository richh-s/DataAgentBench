code = """import json
# var_call_6kPGbY8r79oPicIcfv6N0Cox contains the file path to the JSON result from earlier
path = var_call_6kPGbY8r79oPicIcfv6N0Cox
with open(path, 'r') as f:
    data = json.load(f)
repos = [r['repo_name'] for r in data]
# sanitize single quotes in repo names
repos_sanitized = [r.replace("'", "''") for r in repos]
# build IN list
if len(repos_sanitized) == 0:
    in_list = "''"
else:
    in_list = ','.join("'" + r + "'" for r in repos_sanitized)
# Build DuckDB SQL to count commits matching criteria
sql = (
    "SELECT count(*) as cnt FROM commits "
    "WHERE repo_name IN (" + in_list + ") "
    "AND message IS NOT NULL "
    "AND length(message) < 1000 "
    "AND lower(message) NOT LIKE 'merge%' "
    "AND lower(message) NOT LIKE 'update%' "
    "AND lower(message) NOT LIKE 'test%';"
)
import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_9GNQwj2I7OZo0oHIKEEcGwhD': ['languages', 'repos', 'licenses'], 'var_call_jjVU7zSG0ibs1fvSzL8g5zIO': ['commits', 'contents', 'files'], 'var_call_6kPGbY8r79oPicIcfv6N0Cox': 'file_storage/call_6kPGbY8r79oPicIcfv6N0Cox.json'}

exec(code, env_args)

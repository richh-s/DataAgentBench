code = """import json
path = var_call_6kPGbY8r79oPicIcfv6N0Cox
with open(path, 'r') as f:
    data = json.load(f)
repos = [r['repo_name'] for r in data]
# escape single quotes
repos = [r.replace("'", "''") for r in repos]
# batch size
batch_size = 200
sqls = []
for i in range(0, len(repos), batch_size):
    batch = repos[i:i+batch_size]
    in_list = ','.join("'" + r + "'" for r in batch)
    sql = (
        "SELECT count(*) as cnt FROM commits WHERE repo_name IN (" + in_list + ") "
        "AND message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(message) NOT LIKE 'merge%' "
        "AND lower(message) NOT LIKE 'update%' "
        "AND lower(message) NOT LIKE 'test%';"
    )
    sqls.append(sql)
print('__RESULT__:')
print(json.dumps(sqls))"""

env_args = {'var_call_9GNQwj2I7OZo0oHIKEEcGwhD': ['languages', 'repos', 'licenses'], 'var_call_jjVU7zSG0ibs1fvSzL8g5zIO': ['commits', 'contents', 'files'], 'var_call_6kPGbY8r79oPicIcfv6N0Cox': 'file_storage/call_6kPGbY8r79oPicIcfv6N0Cox.json', 'var_call_6yMcg4S3Z4MtkYOzkVToUlue': 'file_storage/call_6yMcg4S3Z4MtkYOzkVToUlue.json'}

exec(code, env_args)

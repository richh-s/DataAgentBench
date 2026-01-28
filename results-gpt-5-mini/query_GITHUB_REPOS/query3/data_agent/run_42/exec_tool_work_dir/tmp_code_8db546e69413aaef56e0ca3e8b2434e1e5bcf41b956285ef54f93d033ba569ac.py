code = """import json
with open(var_call_WfFqgSplgpWVCPRw9LzoU8GK, 'r') as f:
    repo_names = json.load(f)
# escape single quotes
repo_names_escaped = [r.replace("'", "''") for r in repo_names]
# chunk size
chunk_size = 100
sqls = []
for i in range(0, len(repo_names_escaped), chunk_size):
    chunk = repo_names_escaped[i:i+chunk_size]
    in_list = ",".join([f"'{r}'" for r in chunk])
    sql = ("SELECT COUNT(*) AS commit_count FROM commits WHERE repo_name IN ("+in_list+") "
           "AND message IS NOT NULL AND message != '' AND length(message) < 1000 "
           "AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' "
           "AND lower(message) NOT LIKE 'test%';")
    sqls.append(sql)
print("__RESULT__:")
print(json.dumps(sqls))"""

env_args = {'var_call_UDa2dvW0mwt1Fy7YaZNXYgJi': 'file_storage/call_UDa2dvW0mwt1Fy7YaZNXYgJi.json', 'var_call_WfFqgSplgpWVCPRw9LzoU8GK': 'file_storage/call_WfFqgSplgpWVCPRw9LzoU8GK.json', 'var_call_iSBdNm3e73JgsCKXdpZC63I7': 'file_storage/call_iSBdNm3e73JgsCKXdpZC63I7.json', 'var_call_4giFvJ08uA6WLPvjMMYlJbcR': 'file_storage/call_4giFvJ08uA6WLPvjMMYlJbcR.json'}

exec(code, env_args)

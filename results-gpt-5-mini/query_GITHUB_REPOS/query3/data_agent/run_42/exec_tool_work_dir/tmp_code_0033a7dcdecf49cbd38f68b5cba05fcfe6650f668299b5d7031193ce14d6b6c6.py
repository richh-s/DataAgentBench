code = """import json
with open(var_call_iSBdNm3e73JgsCKXdpZC63I7, 'r') as f:
    data = json.load(f)
# data is list of one dict with 'in_list'
in_list = data[0]['in_list']
# Build SQL query
sql = f"SELECT COUNT(*) AS commit_count FROM commits WHERE repo_name IN {in_list} AND message IS NOT NULL AND message != '' AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';"
import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_UDa2dvW0mwt1Fy7YaZNXYgJi': 'file_storage/call_UDa2dvW0mwt1Fy7YaZNXYgJi.json', 'var_call_WfFqgSplgpWVCPRw9LzoU8GK': 'file_storage/call_WfFqgSplgpWVCPRw9LzoU8GK.json', 'var_call_iSBdNm3e73JgsCKXdpZC63I7': 'file_storage/call_iSBdNm3e73JgsCKXdpZC63I7.json'}

exec(code, env_args)

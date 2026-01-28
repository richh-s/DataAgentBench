code = """import json
# var_call_Ua8aa5dVexPmI3pV3CqrjEyN is provided by previous query_db call
data = None
if isinstance(var_call_Ua8aa5dVexPmI3pV3CqrjEyN, str):
    with open(var_call_Ua8aa5dVexPmI3pV3CqrjEyN, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = var_call_Ua8aa5dVexPmI3pV3CqrjEyN
repo_names = sorted({item['repo_name'] for item in data if item.get('repo_name')})
# Safely escape single quotes in repo names
def esc(name):
    return "'" + name.replace("'", "''") + "'"

if not repo_names:
    sql = "SELECT 0 AS cnt;"
else:
    in_list = ','.join(esc(r) for r in repo_names)
    sql = (
        "SELECT COUNT(*) AS cnt FROM commits "
        "WHERE message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(message) NOT LIKE 'merge%' "
        "AND lower(message) NOT LIKE 'update%' "
        "AND lower(message) NOT LIKE 'test%' "
        f"AND repo_name IN ({in_list});"
    )

import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_Ua8aa5dVexPmI3pV3CqrjEyN': 'file_storage/call_Ua8aa5dVexPmI3pV3CqrjEyN.json'}

exec(code, env_args)

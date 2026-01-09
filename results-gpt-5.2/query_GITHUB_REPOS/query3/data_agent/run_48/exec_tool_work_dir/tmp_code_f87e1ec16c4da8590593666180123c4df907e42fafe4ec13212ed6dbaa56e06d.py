code = """import json

path = var_call_FyCcrS1VIozaZXKX92I1XumZ
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]

chunks = [repo_list[i:i+500] for i in range(0, len(repo_list), 500)]

total = 0
for ch in chunks:
    in_list = "(" + ",".join(["'" + x.replace("'","''") + "'" for x in ch]) + ")"
    q = (
        "SELECT COUNT(*) AS c FROM commits "
        "WHERE message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(trim(message)) NOT LIKE 'merge%' "
        "AND lower(trim(message)) NOT LIKE 'update%' "
        "AND lower(trim(message)) NOT LIKE 'test%' "
        f"AND repo_name IN {in_list}"
    )
    res = functions.query_db(db_name='artifacts_database', query=q)
    total += int(res[0]['c'])

result = json.dumps(total)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_FyCcrS1VIozaZXKX92I1XumZ': 'file_storage/call_FyCcrS1VIozaZXKX92I1XumZ.json'}

exec(code, env_args)

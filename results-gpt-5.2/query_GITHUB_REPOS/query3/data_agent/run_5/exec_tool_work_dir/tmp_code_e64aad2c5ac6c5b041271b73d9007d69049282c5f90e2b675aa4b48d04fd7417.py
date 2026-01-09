code = """import json
repo_res = var_call_BWHGpJQs9Q5iW0Mj5XIwNIKH
if isinstance(repo_res, str) and repo_res.endswith('.json'):
    with open(repo_res, 'r') as f:
        repo_rows = json.load(f)
else:
    repo_rows = repo_res
repos = [r['repo_name'] for r in repo_rows]
chunks = [repos[i:i+500] for i in range(0, len(repos), 500)]

def sql_in_list(items):
    esc = ["'" + s.replace("'", "''") + "'" for s in items]
    return '(' + ','.join(esc) + ')'

sqls = []
for ch in chunks:
    sqls.append(
        "SELECT COUNT(*) AS cnt FROM commits "
        "WHERE message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(substr(trim(message), 1, 5)) <> 'merge' "
        "AND lower(substr(trim(message), 1, 6)) <> 'update' "
        "AND lower(substr(trim(message), 1, 4)) <> 'test' "
        f"AND repo_name IN {sql_in_list(ch)};"
    )

print('__RESULT__:')
print(json.dumps({'sqls': sqls}))"""

env_args = {'var_call_BWHGpJQs9Q5iW0Mj5XIwNIKH': 'file_storage/call_BWHGpJQs9Q5iW0Mj5XIwNIKH.json', 'var_call_P6zCAnlHOwrzneJ4Bfpx8NaO': {'repo_count': 114972, 'num_chunks': 230}, 'var_call_PELgDikrvcCUkM1cjWPJpUyi': [{'cnt': '0'}]}

exec(code, env_args)

code = """import json

path = var_call_FyCcrS1VIozaZXKX92I1XumZ
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]

# build a DuckDB SQL query with VALUES list
# chunk to avoid extremely long statements
chunks = [repo_list[i:i+2000] for i in range(0, len(repo_list), 2000)]

queries = []
for ch in chunks:
    values = ",".join(["('" + x.replace("'","''") + "')" for x in ch])
    q = (
        "WITH repos(repo_name) AS (VALUES " + values + ") "
        "SELECT COUNT(*) AS c "
        "FROM commits cmt "
        "JOIN repos r ON r.repo_name = cmt.repo_name "
        "WHERE cmt.message IS NOT NULL "
        "AND length(cmt.message) < 1000 "
        "AND lower(trim(cmt.message)) NOT LIKE 'merge%' "
        "AND lower(trim(cmt.message)) NOT LIKE 'update%' "
        "AND lower(trim(cmt.message)) NOT LIKE 'test%'"
    )
    queries.append(q)

result = {'total': 0, 'chunks': len(queries)}
print('__RESULT__:')
print(json.dumps({'queries': queries[:2], 'n_queries': len(queries), 'n_repos': len(repo_list)}))"""

env_args = {'var_call_FyCcrS1VIozaZXKX92I1XumZ': 'file_storage/call_FyCcrS1VIozaZXKX92I1XumZ.json', 'var_call_maofEvbonAZxeQVPYiJzip4x': [{'any_owner': 'facebook'}, {'any_owner': 'tensorflow'}, {'any_owner': 'twbs'}, {'any_owner': 'Microsoft'}, {'any_owner': 'torvalds'}], 'var_call_hjIOdI5dy98CwjX5uSpTTO1v': [{'commit_message_count': '0'}]}

exec(code, env_args)

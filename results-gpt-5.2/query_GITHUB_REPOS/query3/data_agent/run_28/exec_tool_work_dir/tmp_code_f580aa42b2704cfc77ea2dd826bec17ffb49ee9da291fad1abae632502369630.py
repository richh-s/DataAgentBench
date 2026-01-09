code = """import json

path = var_call_gcOw7IDxIXkbMVNQ7LDer1HJ
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r.get('repo_name') for r in repos if r.get('repo_name')})

chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]

def esc(s):
    return s.replace("'", "''")

queries = []
for ch in chunks:
    in_list = ','.join(["'" + esc(x) + "'" for x in ch])
    q = "SELECT COUNT(*) AS c FROM commits WHERE message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%' AND repo_name IN (" + in_list + ");"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'chunk_count': len(chunks), 'queries': queries}))"""

env_args = {'var_call_gcOw7IDxIXkbMVNQ7LDer1HJ': 'file_storage/call_gcOw7IDxIXkbMVNQ7LDer1HJ.json', 'var_call_kwW7pslSF2CZAsoo0uGIH5nC': [{'commit_message_count': '0'}]}

exec(code, env_args)

code = """import json, pandas as pd

# load repo list from file (var_call_kB1C3nPh59JSuzBCed5YYTRz)
path = var_call_kB1C3nPh59JSuzBCed5YYTRz
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# chunk into groups for SQL IN clauses
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunks.append(repo_names[i:i+chunk_size])

out = {'n_repos': len(repo_names), 'chunks': len(chunks), 'chunk_size': chunk_size}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_kB1C3nPh59JSuzBCed5YYTRz': 'file_storage/call_kB1C3nPh59JSuzBCed5YYTRz.json', 'var_call_Uj4vNKxPci66bGzW0bwBVJZD': [{'cnt': '15016'}]}

exec(code, env_args)

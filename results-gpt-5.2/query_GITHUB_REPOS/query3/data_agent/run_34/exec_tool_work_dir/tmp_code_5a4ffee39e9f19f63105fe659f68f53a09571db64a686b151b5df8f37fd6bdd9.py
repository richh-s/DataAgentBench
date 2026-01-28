code = """import json
import pandas as pd

# Load repo list from storage file
path = var_call_EhJphjXFe6BqwbRT4VPJT16b
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Chunk to avoid huge IN clauses
chunks = [repo_names[i:i+800] for i in range(0, len(repo_names), 800)]

queries = []
for ch in chunks:
    in_list = ','.join(["'" + x.replace("'","''") + "'" for x in ch])
    q = f"""
    SELECT COUNT(*) AS c
    FROM commits
    WHERE repo_name IN ({in_list})
      AND message IS NOT NULL
      AND length(message) < 1000
      AND lower(message) NOT LIKE 'merge%'
      AND lower(message) NOT LIKE 'update%'
      AND lower(message) NOT LIKE 'test%'
    """
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'queries': queries, 'repo_count': len(repo_names), 'chunk_count': len(chunks)}))"""

env_args = {'var_call_EhJphjXFe6BqwbRT4VPJT16b': 'file_storage/call_EhJphjXFe6BqwbRT4VPJT16b.json'}

exec(code, env_args)

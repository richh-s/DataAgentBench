code = """import json, pandas as pd

# load repo list (may be a file path)
repo_src = var_call_7HhINXFEI9PLu5P9xjWSTynS
if isinstance(repo_src, str):
    with open(repo_src, 'r', encoding='utf-8') as f:
        repos = json.load(f)
else:
    repos = repo_src
repo_names = [r['repo_name'] for r in repos]

# build query with IN list chunks
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    part = repo_names[i:i+chunk_size]
    in_list = ','.join(["'" + p.replace("'","''") + "'" for p in part])
    q = f"""
    SELECT COUNT(*) AS cnt
    FROM commits
    WHERE repo_name IN ({in_list})
      AND message IS NOT NULL
      AND length(message) < 1000
      AND lower(trim(message)) NOT LIKE 'merge%'
      AND lower(trim(message)) NOT LIKE 'update%'
      AND lower(trim(message)) NOT LIKE 'test%'
    """
    chunks.append(q)

out = {
    'repo_count': len(repo_names),
    'queries': chunks[:5],
    'chunk_count': len(chunks)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7HhINXFEI9PLu5P9xjWSTynS': 'file_storage/call_7HhINXFEI9PLu5P9xjWSTynS.json', 'var_call_A6EZ4QPJJtVhF8zeBF8m7m3r': [{'cnt': '15016'}]}

exec(code, env_args)

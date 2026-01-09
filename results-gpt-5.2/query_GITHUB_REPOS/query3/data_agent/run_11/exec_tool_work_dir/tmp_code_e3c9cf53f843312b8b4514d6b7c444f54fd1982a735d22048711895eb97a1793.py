code = """import json, pandas as pd

# Load repo list from previous metadata query (may be large file path)
repo_src = var_call_k7HqCDYIWUQbxLdf1nrhQ6U0
if isinstance(repo_src, str):
    with open(repo_src, 'r') as f:
        repos = json.load(f)
else:
    repos = repo_src
repo_names = [r['repo_name'] for r in repos]

# Chunk repo_names into SQL IN lists
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    chunks.append(chunk)

# Build queries for manual execution? We'll just output chunks count and first chunk to use.
result = {
    'n_repos': len(repo_names),
    'n_chunks': len(chunks),
    'first_chunk': chunks[0] if chunks else []
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_k7HqCDYIWUQbxLdf1nrhQ6U0': 'file_storage/call_k7HqCDYIWUQbxLdf1nrhQ6U0.json'}

exec(code, env_args)

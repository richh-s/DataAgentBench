code = """import json, pandas as pd

# load repo list from file
path = var_call_xv4MJy6nathIGpNuPxbbcxzp
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# create chunks for SQL IN clauses
chunks = []
chunk_size = 5000
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    # escape single quotes
    chunk_esc = [s.replace("'","''") for s in chunk]
    chunks.append("(" + ",".join([f"'{s}'" for s in chunk_esc]) + ")")

result = {
    'repo_count': len(repo_names),
    'in_clauses': chunks,
    'n_chunks': len(chunks)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_xv4MJy6nathIGpNuPxbbcxzp': 'file_storage/call_xv4MJy6nathIGpNuPxbbcxzp.json', 'var_call_Z0jNk7lp3V3y7hsKs91jBsBc': [{'repos_cnt': '114972'}]}

exec(code, env_args)

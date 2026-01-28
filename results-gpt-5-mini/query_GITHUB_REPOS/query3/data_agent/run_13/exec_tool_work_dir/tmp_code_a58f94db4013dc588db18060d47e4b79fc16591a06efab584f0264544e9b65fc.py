code = """import json
# var_call_vuapnoTrPXdfuv1rlKyGpWql is the path to the large JSON result
path = var_call_vuapnoTrPXdfuv1rlKyGpWql
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# extract repo_name
repo_names = [rec['repo_name'] for rec in data if 'repo_name' in rec]
# unique
unique = sorted(list(dict.fromkeys(repo_names)))
# chunk into sizes of 500
chunk_size = 500
chunks = [unique[i:i+chunk_size] for i in range(0, len(unique), chunk_size)]
output = {'total_repos': len(unique), 'num_chunks': len(chunks), 'chunks': chunks}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_vuapnoTrPXdfuv1rlKyGpWql': 'file_storage/call_vuapnoTrPXdfuv1rlKyGpWql.json'}

exec(code, env_args)

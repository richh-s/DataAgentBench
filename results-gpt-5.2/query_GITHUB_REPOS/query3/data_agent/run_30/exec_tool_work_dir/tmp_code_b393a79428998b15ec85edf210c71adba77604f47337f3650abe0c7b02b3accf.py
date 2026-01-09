code = """import json, pandas as pd
# load repo list from file if needed
repo_res = var_call_TGu244PIHit9FXE0sGs30iDh
if isinstance(repo_res, str):
    with open(repo_res, 'r') as f:
        repo_res = json.load(f)
repos = [r['repo_name'] for r in repo_res]
# chunk into manageable IN lists
chunks = [repos[i:i+500] for i in range(0, len(repos), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'"+x.replace("'","''")+"'" for x in ch])
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%' AND repo_name IN ({in_list});"
    queries.append(q)
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_TGu244PIHit9FXE0sGs30iDh': 'file_storage/call_TGu244PIHit9FXE0sGs30iDh.json', 'var_call_p7JnMWQOQCwiG105SU70LgxQ': [{'1': '1'}]}

exec(code, env_args)

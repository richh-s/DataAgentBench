code = """import json, pandas as pd
# load repo list from var_call_Tsv6dkt8I05MM2XJCgyo1WNB (json file path)
path = var_call_Tsv6dkt8I05MM2XJCgyo1WNB
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]
# chunk into manageable IN lists
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'"+x.replace("'","''")+"'" for x in ch])
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%' AND repo_name IN ({in_list});"
    queries.append(q)
print('__RESULT__:')
print(json.dumps({'n_repos': len(repo_names), 'n_chunks': len(chunks), 'queries': queries[:3], 'all_queries_path_needed': len(queries)>3}))"""

env_args = {'var_call_Tsv6dkt8I05MM2XJCgyo1WNB': 'file_storage/call_Tsv6dkt8I05MM2XJCgyo1WNB.json'}

exec(code, env_args)

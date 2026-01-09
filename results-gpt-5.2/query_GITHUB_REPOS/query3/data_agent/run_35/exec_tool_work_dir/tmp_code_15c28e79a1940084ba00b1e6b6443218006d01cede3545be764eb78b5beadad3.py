code = """import json, pandas as pd

# load repo list from stored json file path
path = var_call_wWslIqbNnYleizS3X8NGpkU2
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# chunk into groups to query duckdb with IN clauses
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = f"""SELECT COUNT(*) AS c FROM commits
    WHERE message IS NOT NULL
      AND LENGTH(message) < 1000
      AND LOWER(TRIM(message)) NOT LIKE 'merge%'
      AND LOWER(TRIM(message)) NOT LIKE 'update%'
      AND LOWER(TRIM(message)) NOT LIKE 'test%'
      AND repo_name IN ({in_list});"""
    queries.append(q)

out = {'repo_count': len(repo_names), 'queries': queries}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wWslIqbNnYleizS3X8NGpkU2': 'file_storage/call_wWslIqbNnYleizS3X8NGpkU2.json'}

exec(code, env_args)

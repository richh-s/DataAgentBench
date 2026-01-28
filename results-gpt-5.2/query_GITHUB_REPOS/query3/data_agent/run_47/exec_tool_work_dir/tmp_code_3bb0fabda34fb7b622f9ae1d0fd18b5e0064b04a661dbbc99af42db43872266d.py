code = """import json
import pandas as pd

# load repo list from the sqlite query result stored as json file path
path = var_call_yOmCqfZxVcqYd7g9sIgwjsIr
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# chunk IN list to avoid query length issues
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
counts = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = f"""
    SELECT COUNT(*) AS c
    FROM commits
    WHERE message IS NOT NULL
      AND length(message) < 1000
      AND lower(message) NOT LIKE 'merge%'
      AND lower(message) NOT LIKE 'update%'
      AND lower(message) NOT LIKE 'test%'
      AND repo_name IN ({in_list});
    """
    counts.append(q)

out = {'queries': counts}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yOmCqfZxVcqYd7g9sIgwjsIr': 'file_storage/call_yOmCqfZxVcqYd7g9sIgwjsIr.json'}

exec(code, env_args)

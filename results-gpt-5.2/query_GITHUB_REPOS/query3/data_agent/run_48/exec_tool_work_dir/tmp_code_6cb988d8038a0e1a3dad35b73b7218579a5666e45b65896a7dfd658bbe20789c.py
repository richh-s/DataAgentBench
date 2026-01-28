code = """import json
import pandas as pd

# var_call_FyCcrS1VIozaZXKX92I1XumZ is a filepath to json (list of {repo_name})
path = var_call_FyCcrS1VIozaZXKX92I1XumZ
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]

# chunk to avoid too long IN list
chunks = [repo_list[i:i+500] for i in range(0, len(repo_list), 500)]

counts = []
for ch in chunks:
    in_list = "(" + ",".join(["'" + x.replace("'","''") + "'" for x in ch]) + ")"
    q = f"""
    SELECT COUNT(*) AS c
    FROM commits
    WHERE message IS NOT NULL
      AND length(message) < 1000
      AND lower(trim(message)) NOT LIKE 'merge%'
      AND lower(trim(message)) NOT LIKE 'update%'
      AND lower(trim(message)) NOT LIKE 'test%'
      AND repo_name IN {in_list}
    ;
    """
    res = functions.query_db(db_name='artifacts_database', query=q)
    counts.append(int(res[0]['c']))

result = json.dumps({'commit_message_count': int(sum(counts))})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_FyCcrS1VIozaZXKX92I1XumZ': 'file_storage/call_FyCcrS1VIozaZXKX92I1XumZ.json'}

exec(code, env_args)

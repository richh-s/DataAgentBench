code = """import json, pandas as pd

# Load repo list from file
path = var_call_YllHK59xEiLpSeUiAMlR9XQm
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos if r.get('repo_name')]

# Build DuckDB IN list safely
# Escape single quotes by doubling
vals = ",".join(["'" + rn.replace("'","''") + "'" for rn in repo_names])
query = f"""
SELECT COUNT(*)::BIGINT AS commit_message_count
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
  AND repo_name IN ({vals});
"""

result = {"query": query}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_YllHK59xEiLpSeUiAMlR9XQm': 'file_storage/call_YllHK59xEiLpSeUiAMlR9XQm.json', 'var_call_uy2B6g9ZyTVCdF7N8x6RSXLa': [{'commit_message_count': '0'}]}

exec(code, env_args)

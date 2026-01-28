code = """import json, pandas as pd
from pathlib import Path

# Load repo list from file path
p = Path(var_call_5034TdZFF1lP9Yefup6AMEGp)
repos = json.loads(p.read_text())
repo_names = [r['repo_name'] for r in repos]

# build IN list safely by escaping single quotes
in_list = ','.join(["'" + rn.replace("'","''") + "'" for rn in repo_names])
query = f"""
SELECT COUNT(*) AS cnt
FROM commits
WHERE repo_name IN ({in_list})
  AND message IS NOT NULL
  AND length(message) < 1000
  AND lower(trim(message)) NOT LIKE 'merge%'
  AND lower(trim(message)) NOT LIKE 'update%'
  AND lower(trim(message)) NOT LIKE 'test%'
;"""

out = {"query": query}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5034TdZFF1lP9Yefup6AMEGp': 'file_storage/call_5034TdZFF1lP9Yefup6AMEGp.json', 'var_call_mVIQBwn6iioDm315rXANpozH': [{'cnt': '0'}]}

exec(code, env_args)

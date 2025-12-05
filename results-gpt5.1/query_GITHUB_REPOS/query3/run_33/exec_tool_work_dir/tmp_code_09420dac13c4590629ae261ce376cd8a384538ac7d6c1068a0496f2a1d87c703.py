code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_2spo34c0AknjzqQsDz0OPCMb)
rows = json.loads(path.read_text())
repos = [r['repo_name'] for r in rows]

# If no repos, answer is 0
if not repos:
    result = 0
else:
    # Build an IN clause, taking care of quotes
    in_list = ','.join("'" + r.replace("'", "''") + "'" for r in repos)
    query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
    result = query

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2spo34c0AknjzqQsDz0OPCMb': 'file_storage/call_2spo34c0AknjzqQsDz0OPCMb.json', 'var_call_KvSSAfD6zvVxQdeZi4BH7pKP': [{'cnt': '15016'}]}

exec(code, env_args)

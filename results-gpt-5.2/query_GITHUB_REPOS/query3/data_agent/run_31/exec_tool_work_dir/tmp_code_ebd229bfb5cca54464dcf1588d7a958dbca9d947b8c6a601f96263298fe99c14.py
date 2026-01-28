code = """import json, pandas as pd

# load repo list from file path
path = var_call_yAHkqMqnhhN6xIvIRF9Ah21D
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# build VALUES clause in chunks to avoid very long SQL
chunks = []
chunk_size = 5000
for i in range(0, len(repo_names), chunk_size):
    part = repo_names[i:i+chunk_size]
    values = ','.join(["('" + rn.replace("'","''") + "')" for rn in part])
    chunks.append(f"SELECT * FROM (VALUES {values}) v(repo_name)")
repo_cte = "\nUNION ALL\n".join(chunks)

query = f"""
WITH shell_apache AS (
{repo_cte}
)
SELECT COUNT(*)::BIGINT AS commit_message_count
FROM commits c
JOIN shell_apache sa ON sa.repo_name = c.repo_name
WHERE c.message IS NOT NULL
  AND length(c.message) < 1000
  AND NOT (lower(ltrim(c.message)) LIKE 'merge%'
           OR lower(ltrim(c.message)) LIKE 'update%'
           OR lower(ltrim(c.message)) LIKE 'test%');
"""

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_yAHkqMqnhhN6xIvIRF9Ah21D': 'file_storage/call_yAHkqMqnhhN6xIvIRF9Ah21D.json', 'var_call_tareLwQ56A15duqzJ5AZodMf': [{'total': '114972'}]}

exec(code, env_args)

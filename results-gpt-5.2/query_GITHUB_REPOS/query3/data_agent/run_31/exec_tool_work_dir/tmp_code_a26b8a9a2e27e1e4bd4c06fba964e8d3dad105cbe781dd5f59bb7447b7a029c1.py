code = """import json

path = var_call_yAHkqMqnhhN6xIvIRF9Ah21D
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

chunks = []
chunk_size = 5000
for i in range(0, len(repo_names), chunk_size):
    part = repo_names[i:i+chunk_size]
    values = ','.join(["('" + rn.replace("'","''") + "')" for rn in part])
    chunks.append('SELECT * FROM (VALUES ' + values + ') v(repo_name)')
repo_cte = '\nUNION ALL\n'.join(chunks)

query = (
"WITH shell_apache AS (\n" + repo_cte + "\n)\n"
"SELECT COUNT(*)::BIGINT AS commit_message_count\n"
"FROM commits c\n"
"JOIN shell_apache sa ON sa.repo_name = c.repo_name\n"
"WHERE c.message IS NOT NULL\n"
"  AND length(c.message) < 1000\n"
"  AND NOT (lower(ltrim(c.message)) LIKE 'merge%'\n"
"           OR lower(ltrim(c.message)) LIKE 'update%'\n"
"           OR lower(ltrim(c.message)) LIKE 'test%');\n"
)

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_yAHkqMqnhhN6xIvIRF9Ah21D': 'file_storage/call_yAHkqMqnhhN6xIvIRF9Ah21D.json', 'var_call_tareLwQ56A15duqzJ5AZodMf': [{'total': '114972'}]}

exec(code, env_args)

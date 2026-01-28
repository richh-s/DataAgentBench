code = """import json

path = var_call_6EXlZ3yhaGPRTgnLYbXxpZIf
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

chunk_size = 500
clauses = []
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    vals = ",".join(["'" + x.replace("'","''") + "'" for x in chunk])
    clauses.append("repo_name IN (" + vals + ")")
where_repo = " OR ".join(["(" + c + ")" for c in clauses]) if clauses else "FALSE"

query = (
"SELECT COUNT(*) AS cnt\n"
"FROM commits\n"
"WHERE (" + where_repo + ")\n"
"  AND message IS NOT NULL\n"
"  AND LENGTH(message) < 1000\n"
"  AND LOWER(message) NOT LIKE 'merge%'\n"
"  AND LOWER(message) NOT LIKE 'update%'\n"
"  AND LOWER(message) NOT LIKE 'test%';"
)

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_6EXlZ3yhaGPRTgnLYbXxpZIf': 'file_storage/call_6EXlZ3yhaGPRTgnLYbXxpZIf.json', 'var_call_apix87Gs96Yhv3FcUZcaVsce': [{'cnt': '0'}]}

exec(code, env_args)

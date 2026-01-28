code = """import json

path = var_call_sLHCuX0XKU7J8rRMQoXzSiXL
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r.get('repo_name') for r in repos if r.get('repo_name')})

vals = ",\n    ".join(["('" + rn.replace("'", "''") + "')" for rn in repo_names])
query = (
"SELECT COUNT(*) AS commit_message_count\n"
"FROM commits\n"
"WHERE message IS NOT NULL\n"
"  AND LENGTH(message) < 1000\n"
"  AND LOWER(message) NOT LIKE 'merge%'\n"
"  AND LOWER(message) NOT LIKE 'update%'\n"
"  AND LOWER(message) NOT LIKE 'test%'\n"
"  AND repo_name IN (\n"
"    SELECT repo_name FROM (VALUES\n"
f"    {vals}\n"
"    ) v(repo_name)\n"
"  );"
)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'query': query}))"""

env_args = {'var_call_sLHCuX0XKU7J8rRMQoXzSiXL': 'file_storage/call_sLHCuX0XKU7J8rRMQoXzSiXL.json', 'var_call_PTVUCRIVmb2BwYsWqtCFjQS7': [{'commit_message_count': '0'}]}

exec(code, env_args)

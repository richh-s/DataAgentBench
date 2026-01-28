code = """import json

path = var_call_sLHCuX0XKU7J8rRMQoXzSiXL
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r.get('repo_name') for r in repos if r.get('repo_name')})

vals = ",\n    ".join(["('" + rn.replace("'", "''") + "')" for rn in repo_names])

parts = []
parts.append('SELECT COUNT(*) AS commit_message_count\n')
parts.append('FROM commits\n')
parts.append('WHERE message IS NOT NULL\n')
parts.append('  AND LENGTH(message) < 1000\n')
parts.append("  AND LOWER(message) NOT LIKE 'merge%'\n")
parts.append("  AND LOWER(message) NOT LIKE 'update%'\n")
parts.append("  AND LOWER(message) NOT LIKE 'test%'\n")
parts.append('  AND repo_name IN (\n')
parts.append('    SELECT repo_name FROM (VALUES\n')
parts.append('    ' + vals + '\n')
parts.append('    ) v(repo_name)\n')
parts.append('  );')
query = ''.join(parts)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'query_len': len(query), 'query_head': query[:200]}))"""

env_args = {'var_call_sLHCuX0XKU7J8rRMQoXzSiXL': 'file_storage/call_sLHCuX0XKU7J8rRMQoXzSiXL.json', 'var_call_PTVUCRIVmb2BwYsWqtCFjQS7': [{'commit_message_count': '0'}]}

exec(code, env_args)

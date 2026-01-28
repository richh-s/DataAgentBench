code = """import json, os
# Load only the group_concat result file path variable
p = var_call_tRfUwmP2IleVgh1nKRvA1XVi
res = None
if isinstance(p, str) and os.path.exists(p):
    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        data = json.load(f)
    if isinstance(data, list) and len(data) > 0 and 'repo_list' in data[0]:
        repo_list_str = data[0]['repo_list']
        # repo_list_str is like "'repo1','repo2',..."
        # Convert to list
        items = [s.strip().strip("'") for s in repo_list_str.split(',') if s.strip()]
        # Build SQL IN clause safely
        in_clause = '(' + ','.join("'{}'".format(s.replace("'","''")) for s in items) + ')'
        res = {'count_non_python_repos': len(items), 'in_clause': in_clause[:10000]}
    else:
        res = {'error': 'unexpected data format'}
else:
    res = {'error': 'file not found'}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_LM3tvya7aOMgQs8YKYzKm8YV': 'file_storage/call_LM3tvya7aOMgQs8YKYzKm8YV.json', 'var_call_9JPe2QYsMLtUbCP1E5AsAkEn': 'file_storage/call_9JPe2QYsMLtUbCP1E5AsAkEn.json', 'var_call_ujleLBsycHOXQnXq3165Ttf1': {'test': 1}, 'var_call_tRfUwmP2IleVgh1nKRvA1XVi': 'file_storage/call_tRfUwmP2IleVgh1nKRvA1XVi.json', 'var_call_FmiEAR0eIHy1koa8ffhDVISO': 'file_storage/call_FmiEAR0eIHy1koa8ffhDVISO.json'}

exec(code, env_args)

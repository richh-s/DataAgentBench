code = """import json

file_path = locals()['var_function-call-5659440359998634894']
with open(file_path, 'r') as f:
    papers = json.load(f)

headers = []
for p in papers[:5]:
    headers.append(p.get('text', '')[:500])

print(f"__RESULT__:")
print(json.dumps(headers))"""

env_args = {'var_function-call-7797754870209307186': 'file_storage/function-call-7797754870209307186.json', 'var_function-call-5659440359998634894': 'file_storage/function-call-5659440359998634894.json', 'var_function-call-5805009466190750349': []}

exec(code, env_args)

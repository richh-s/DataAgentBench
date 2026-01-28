code = """import json
with open(var_call_qAIVVBQpLbB6atIJDbCLzuG1, 'r') as f:
    data = json.load(f)
# Prepare a small preview
preview = []
for doc in data[:3]:
    preview.append({'filename': doc.get('filename'), 'text_preview': doc.get('text','')[:1000]})
print('__RESULT__:')
print(json.dumps(preview))"""

env_args = {'var_call_qAIVVBQpLbB6atIJDbCLzuG1': 'file_storage/call_qAIVVBQpLbB6atIJDbCLzuG1.json', 'var_call_9XqkdZByJi6RxZrjYs0ZzDwM': {'projects': [], 'project_names': []}, 'var_call_h6RMsOfq9KsOyjkk2vXzWxby': []}

exec(code, env_args)

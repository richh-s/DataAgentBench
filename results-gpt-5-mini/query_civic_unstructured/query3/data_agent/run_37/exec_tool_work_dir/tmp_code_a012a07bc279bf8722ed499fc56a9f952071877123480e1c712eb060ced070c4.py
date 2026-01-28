code = """import json, re
with open(var_call_qAIVVBQpLbB6atIJDbCLzuG1, 'r') as f:
    docs = json.load(f)
matches = []
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if re.search(r'\b(FEMA|emergency)\b', ln, re.I):
            start = max(0, i-5)
            end = min(len(lines), i+6)
            context = lines[start:end]
            matches.append({'filename': doc.get('filename'), 'line_index': i, 'match_line': ln, 'context': context})

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_qAIVVBQpLbB6atIJDbCLzuG1': 'file_storage/call_qAIVVBQpLbB6atIJDbCLzuG1.json', 'var_call_9XqkdZByJi6RxZrjYs0ZzDwM': {'projects': [], 'project_names': []}}

exec(code, env_args)

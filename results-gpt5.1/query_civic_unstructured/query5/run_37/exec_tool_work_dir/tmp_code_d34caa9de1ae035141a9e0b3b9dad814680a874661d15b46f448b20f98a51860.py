code = """import json, re

path = var_call_TyCd5mkqMKHpFWUU1gRJW5eL
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(d['text'] for d in civic_docs)
lines = [l.strip() for l in texts.split('\n') if l.strip()]

projects_2022 = set()
for line in lines:
    if '2022' in line:
        clean = re.sub(r'[\u2022\(].*', '', line).strip()
        if len(clean.split()) <= 10 and any(c.isalpha() for c in clean):
            projects_2022.add(clean)

projects_context = set(projects_2022)
prev = ''
for line in lines:
    if 'Begin Construction' in line and '2022' in line and prev:
        if len(prev.split()) <= 12 and any(c.isalpha() for c in prev):
            projects_context.add(prev.strip())
    if line and not any(ch.isdigit() for ch in line):
        prev = line

result = sorted(projects_context)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TyCd5mkqMKHpFWUU1gRJW5eL': 'file_storage/call_TyCd5mkqMKHpFWUU1gRJW5eL.json', 'var_call_QuqbUBEEOSp6cR9k9EXRPpqp': 'file_storage/call_QuqbUBEEOSp6cR9k9EXRPpqp.json'}

exec(code, env_args)

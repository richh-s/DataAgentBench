code = """import re, json, pandas as pd

# Load full civic docs
path = var_call_5cawsB7woxYPaVg5faJzGszw
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Heuristic: lines mentioning 'Park' as part of project names
lines = [l.strip() for l in full_text.split('\n') if l.strip()]
project_lines = []
for l in lines:
    if 'Park' in l and not l.lower().startswith('page '):
        project_lines.append(l)

# Additionally capture some context lines that mention completion and 2022
context = []
for i, l in enumerate(lines):
    if ('Construction was completed' in l or 'construction was completed' in l) and '2022' in l:
        window = lines[max(0, i-3):i+3]
        context.extend(window)

relevant = sorted(set(project_lines + context))

result = {'sample_lines': relevant[:200]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5cawsB7woxYPaVg5faJzGszw': 'file_storage/call_5cawsB7woxYPaVg5faJzGszw.json', 'var_call_moFj00JQ5mgre3M7zmFlY1Wq': 'file_storage/call_moFj00JQ5mgre3M7zmFlY1Wq.json'}

exec(code, env_args)

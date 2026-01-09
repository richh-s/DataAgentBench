code = """import json, pandas as pd

var = var_call_n3fmCyRhoVAGCf9wMSQmOlQO
if isinstance(var, str) and var.endswith('.json'):
    with open(var, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = var

# take first doc and show lines around 'Disaster'
text = docs[0]['text']
lines = text.splitlines()
idxs = [i for i,l in enumerate(lines) if 'Disaster' in l]
snippet = []
for i in idxs[:3]:
    start = max(0, i-3)
    end = min(len(lines), i+8)
    snippet.append({'line_index': i, 'context': lines[start:end]})

print('__RESULT__:')
print(json.dumps(snippet))"""

env_args = {'var_call_mImfOvDqjEWwtbOEFHa6RwO8': ['Funding'], 'var_call_zek2GZ6YL608W3ghopgfCLDJ': ['civic_docs'], 'var_call_gzsZiU7wXQyH4mWQvV7OHFPc': 'file_storage/call_gzsZiU7wXQyH4mWQvV7OHFPc.json', 'var_call_RJmqRBDb3cvzpVjDNrgMt7U5': 'file_storage/call_RJmqRBDb3cvzpVjDNrgMt7U5.json', 'var_call_qceswyg6XTHns5RKII4iNCGr': {'total_funding': 0, 'num_projects': 0, 'projects': [], 'started_2022_projects': []}, 'var_call_n3fmCyRhoVAGCf9wMSQmOlQO': 'file_storage/call_n3fmCyRhoVAGCf9wMSQmOlQO.json'}

exec(code, env_args)

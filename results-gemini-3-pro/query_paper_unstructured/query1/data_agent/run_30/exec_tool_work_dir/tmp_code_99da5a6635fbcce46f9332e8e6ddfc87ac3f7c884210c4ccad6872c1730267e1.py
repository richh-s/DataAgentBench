code = """import json

with open(locals()['var_function-call-8395827407536305276'], 'r') as f:
    papers = json.load(f)

matches = []

for p in papers:
    text = p.get('text', '').lower()
    title = p.get('filename', '').replace('.txt', '')
    
    if 'food' in text:
        # Get context
        idx = text.find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)]
        matches.append({"title": title, "snippet": snippet})

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_function-call-3709648201764099351': 'file_storage/function-call-3709648201764099351.json', 'var_function-call-12009379333761153785': 'file_storage/function-call-12009379333761153785.json', 'var_function-call-8395827407536305276': 'file_storage/function-call-8395827407536305276.json', 'var_function-call-12574282544977898815': []}

exec(code, env_args)

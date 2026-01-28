code = """import json

with open(locals()['var_function-call-4672195044827894195'], 'r') as f:
    papers = json.load(f)

hits = []
for p in papers:
    text = p.get('text', '')
    if 'food' in text.lower():
        # Find index
        idx = text.lower().find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)].replace('\n', ' ')
        hits.append({"title": p['filename'], "snippet": snippet})
        if len(hits) >= 5:
            break

print("__RESULT__:")
print(json.dumps(hits))"""

env_args = {'var_function-call-13370766090165900916': 'file_storage/function-call-13370766090165900916.json', 'var_function-call-9130405135784485262': 'file_storage/function-call-9130405135784485262.json', 'var_function-call-9265765399726123142': 'file_storage/function-call-9265765399726123142.json', 'var_function-call-4672195044827894195': 'file_storage/function-call-4672195044827894195.json', 'var_function-call-6440888066773927974': 876, 'var_function-call-1546429934820446288': {'count': 0, 'titles': []}}

exec(code, env_args)

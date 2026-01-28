code = """import json

with open(locals()['var_function-call-7459141219968339162'], 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers:
    text = p['text']
    if 'food' in text.lower():
        idx = text.lower().find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)]
        snippet = snippet.replace(chr(10), ' ').replace(chr(13), ' ')
        debug_info.append({"filename": p['filename'], "snippet": snippet})
        if len(debug_info) > 5:
            break

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3676184941267040123': 'file_storage/function-call-3676184941267040123.json', 'var_function-call-6873213907714452995': 'file_storage/function-call-6873213907714452995.json', 'var_function-call-17043150740226976793': 'file_storage/function-call-17043150740226976793.json', 'var_function-call-7459141219968339162': 'file_storage/function-call-7459141219968339162.json', 'var_function-call-4763535483607380': {'total_citations': 0, 'papers': []}}

exec(code, env_args)

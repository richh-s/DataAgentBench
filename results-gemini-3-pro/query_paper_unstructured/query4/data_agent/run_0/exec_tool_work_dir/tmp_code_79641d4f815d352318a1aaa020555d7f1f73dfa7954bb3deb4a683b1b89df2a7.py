code = """import json
import re

file_path = locals()['var_function-call-2371613327861333471']

with open(file_path, 'r') as f:
    papers = json.load(f)

pa_pattern = re.compile(r"physical\s+activity", re.IGNORECASE)

matches = []
for paper in papers:
    text = paper.get('text', '')
    if pa_pattern.search(text):
        matches.append({"filename": paper.get('filename'), "header": text[:500]})
        if len(matches) >= 5:
            break

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-10785526798684626706': 'file_storage/function-call-10785526798684626706.json', 'var_function-call-5504457116591251088': 'file_storage/function-call-5504457116591251088.json', 'var_function-call-2371613327861333471': 'file_storage/function-call-2371613327861333471.json', 'var_function-call-15009766085818437093': []}

exec(code, env_args)

code = """import json

with open(locals()['var_function-call-4654103334756958724'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if '(cid:190) Updates' in line or '(cid:190) Project Description' in line:
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                p_name = lines[j].strip()
                block_lines = []
                k = i
                while k < len(lines):
                    l_strip = lines[k].strip()
                    if k > i and ('(cid:190) Updates' in l_strip or '(cid:190) Project Description' in l_strip):
                        break
                    block_lines.append(lines[k])
                    k += 1
                p_text = ' '.join(block_lines)
                projects.append({'name': p_name, 'text': p_text})

# Print all park projects and their text
print("__RESULT__:")
park_projects = [p for p in projects if 'park' in p['name'].lower()]
print(json.dumps(park_projects))"""

env_args = {'var_function-call-4654103334756958724': 'file_storage/function-call-4654103334756958724.json', 'var_function-call-4654103334756962095': 'file_storage/function-call-4654103334756962095.json', 'var_function-call-13824815338074985427': {'total': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}}

exec(code, env_args)

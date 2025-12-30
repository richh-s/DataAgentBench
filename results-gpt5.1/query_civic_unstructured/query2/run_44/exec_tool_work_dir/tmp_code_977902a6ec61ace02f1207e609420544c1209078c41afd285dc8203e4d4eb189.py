code = """import re, json
from pathlib import Path

path_docs = Path(var_call_ISYRQA7gphK6UGR5Oiunyske)
with open(path_docs, 'r') as f:
    docs = json.load(f)

park_projects_2022 = set()

for doc in docs:
    text = doc.get('text', '')
    if 'park' not in text.lower():
        continue
    if '2022' not in text:
        continue
    for line in text.split('\n'):
        if 'park' in line.lower():
            line_clean = line.strip()
            if 5 < len(line_clean) < 200:
                park_projects_2022.add(line_clean)

candidates = []
for l in park_projects_2022:
    if ':' in l:
        continue
    if len(l.split()) <= 2:
        continue
    candidates.append(l)

result = json.dumps(candidates)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ISYRQA7gphK6UGR5Oiunyske': 'file_storage/call_ISYRQA7gphK6UGR5Oiunyske.json', 'var_call_ozUiEhWArxjNOU0W0oLmKYQV': 'file_storage/call_ozUiEhWArxjNOU0W0oLmKYQV.json'}

exec(code, env_args)

code = """import re, json
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_ISYRQA7gphK6UGR5Oiunyske)
with open(path_docs, 'r') as f:
    docs = json.load(f)

park_projects_2022 = set()

for doc in docs:
    text = doc.get('text', '')
    if 'park' not in text.lower():
        continue
    # crude split by line, look for lines with 'Park'
    for line in text.split('\n'):
        if 'park' in line.lower():
            # capture project-like phrases (heuristic: up to 120 chars)
            line_clean = line.strip()
            if len(line_clean) > 5 and len(line_clean) < 200:
                # require some 2022 mention nearby in document
                if '2022' in text:
                    park_projects_2022.add(line_clean)

# Just keep probable project names by filtering lines that look like titles (no colon) and capitalized words
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

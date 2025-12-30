code = """import json, re
from pathlib import Path

with open(var_call_nT6caRPYGzfRwQzIn6bwWgzT, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

projects = []
for text in texts:
    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        if 'Project' in line_stripped or 'Park' in line_stripped or 'Playground' in line_stripped:
            projects.append(line_stripped)

park_completed_2022 = set()
for line in projects:
    lower = line.lower()
    if ('park' in lower) and ('construction was completed' in lower) and ('2022' in lower):
        park_completed_2022.add(line)

result = {
    'sample_project_lines': list(park_completed_2022)[:20],
    'num_lines': len(park_completed_2022)
}

res_str = json.dumps(result)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_nT6caRPYGzfRwQzIn6bwWgzT': 'file_storage/call_nT6caRPYGzfRwQzIn6bwWgzT.json', 'var_call_VNc9MzRjYhMwP6DRIhinzDY7': 'file_storage/call_VNc9MzRjYhMwP6DRIhinzDY7.json'}

exec(code, env_args)

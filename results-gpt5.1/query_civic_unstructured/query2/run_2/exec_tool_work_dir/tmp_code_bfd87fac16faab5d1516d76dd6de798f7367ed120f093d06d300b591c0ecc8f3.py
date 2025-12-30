code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_0vENx1jeQZqtLRDGLGARccl0)
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = [d['text'] for d in docs]

projects = []
for text in texts:
    for line in text.split('\n'):
        line_clean = line.strip()
        if not line_clean:
            continue
        if 'Park' in line_clean or 'park' in line_clean:
            projects.append(line_clean)

projects_unique = sorted(set(projects))

result = json.dumps(projects_unique[:200])
print('__RESULT__:')
print(result)"""

env_args = {'var_call_0vENx1jeQZqtLRDGLGARccl0': 'file_storage/call_0vENx1jeQZqtLRDGLGARccl0.json', 'var_call_Hrb72gHg47T3uGlOv7WnIRKg': 'file_storage/call_Hrb72gHg47T3uGlOv7WnIRKg.json'}

exec(code, env_args)

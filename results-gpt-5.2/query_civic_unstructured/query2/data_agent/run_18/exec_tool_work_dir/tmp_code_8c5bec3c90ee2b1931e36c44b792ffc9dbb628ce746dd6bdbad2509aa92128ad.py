code = """import json, re
from pathlib import Path

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        return json.loads(Path(x).read_text())
    return x

docs = load_records(var_call_S2omvDbArhESgAUSzOBp3R6S)

projects=set()
for d in docs:
    lines=d.get('text','').splitlines()
    for i,l in enumerate(lines):
        if re.search(r'(?i)park', l):
            window=' '.join(lines[i:i+20])
            if re.search(r'(?i)completed', window) and re.search(r'2022', window):
                name=l.strip()
                name=re.sub(r'\s+\(.*?\)\s*','',name)
                projects.add(name)

print('__RESULT__:')
print(json.dumps({'projects':sorted(projects)}))"""

env_args = {'var_call_You8HiLjwrNqLWkqtjg5UWXj': ['civic_docs'], 'var_call_W0WylhYl6POMeBfHyo3yNJzR': ['Funding'], 'var_call_S2omvDbArhESgAUSzOBp3R6S': 'file_storage/call_S2omvDbArhESgAUSzOBp3R6S.json'}

exec(code, env_args)

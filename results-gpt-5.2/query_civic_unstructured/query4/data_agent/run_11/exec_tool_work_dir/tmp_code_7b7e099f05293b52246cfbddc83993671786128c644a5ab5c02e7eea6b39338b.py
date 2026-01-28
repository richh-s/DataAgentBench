code = """import json
from pathlib import Path

path = Path(var_call_DQLKJrtf3yYi1VEkTJZXOohY)
docs = json.loads(path.read_text())

# search for exact substring 'Begin Construction: Spring 2022' and grab preceding non-empty line as project name
projects = []
for d in docs:
    lines = d.get('text','').splitlines()
    for idx, line in enumerate(lines):
        if 'Begin Construction:' in line and 'Spring 2022' in line:
            j = idx-1
            while j>=0 and not lines[j].strip():
                j -= 1
            if j>=0:
                projects.append(lines[j].strip())

projects_unique = sorted(set(projects))
print('__RESULT__:')
print(json.dumps({'spring22_projects': projects_unique, 'count': len(projects_unique)}))"""

env_args = {'var_call_TpPn0yAmA3vLsADt1sJwRJSb': ['Funding'], 'var_call_357DOrmSTlhzjregOEGXC2P6': ['civic_docs'], 'var_call_DQLKJrtf3yYi1VEkTJZXOohY': 'file_storage/call_DQLKJrtf3yYi1VEkTJZXOohY.json'}

exec(code, env_args)

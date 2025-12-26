code = """import json
with open(var_call_3n0zhR3tgtTKd2yTjEpxx45r, 'r') as f:
    funding_projects = json.load(f)
funding_names = set([p['Project_Name'].strip().lower() for p in funding_projects])
with open(var_call_qmiqQY26wMYIpOh9TbMw6yrS, 'r') as f:
    civic_docs = json.load(f)
design_projects = set()
for doc in civic_docs:
    t = doc.get('text', '').lower().split('\n')
    for k, line in enumerate(t):
        if 'capital improvement projects (design)' in line:
            for n in range(1,16):
                if k+n < len(t):
                    l2 = t[k+n].strip().lower()
                    if 5 < len(l2) < 80 and ('project' in l2 or 'repair' in l2 or 'storm drain' in l2 or 'skate park' in l2):
                        name = l2.split(',')[0].split(':')[0].strip()
                        design_projects.add(name)
matched = [n for n in design_projects if n in funding_names]
print('__RESULT__:')
print(json.dumps(len(matched)))"""

env_args = {'var_call_3n0zhR3tgtTKd2yTjEpxx45r': 'file_storage/call_3n0zhR3tgtTKd2yTjEpxx45r.json', 'var_call_qmiqQY26wMYIpOh9TbMw6yrS': 'file_storage/call_qmiqQY26wMYIpOh9TbMw6yrS.json'}

exec(code, env_args)

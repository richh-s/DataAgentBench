code = """import re, json
from collections import defaultdict

funding = var_call_e9773KAfFzr2F8J5p1zgoob8
texts = [d['text'] for d in var_call_YYZOkM2h30Yau3ZuFvd0Fbap]

text = '\n'.join(texts)

sections = re.split(r'Capital Improvement Projects \(Design\)', text, flags=re.I)
if len(sections) < 2:
    design_block = ''
else:
    after = sections[1]
    design_block = re.split(r'Capital Improvement Projects \(Construction\)', after, flags=re.I)[0]

lines = [l.strip() for l in design_block.split('\n') if l.strip()]
projects_design = []
for line in lines:
    if re.match(r'^[A-Z0-9].*', line) and not line.lower().startswith(('updates', 'project schedule', 'estimated schedule')):
        if len(line.split())>2:
            projects_design.append(line)

projects_design = list(dict.fromkeys(projects_design))

funding_names = {row['Project_Name'] for row in funding}

matched = []
for pname in funding_names:
    for dname in projects_design:
        if dname.lower() in pname.lower() or pname.lower() in dname.lower():
            matched.append(pname)
            break

count = len(matched)

result = {"design_capital_projects_funding_over_50000_count": count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_e9773KAfFzr2F8J5p1zgoob8': 'file_storage/call_e9773KAfFzr2F8J5p1zgoob8.json', 'var_call_YYZOkM2h30Yau3ZuFvd0Fbap': 'file_storage/call_YYZOkM2h30Yau3ZuFvd0Fbap.json'}

exec(code, env_args)

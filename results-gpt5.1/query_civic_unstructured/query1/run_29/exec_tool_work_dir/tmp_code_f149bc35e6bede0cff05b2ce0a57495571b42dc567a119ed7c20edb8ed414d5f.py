code = """import re, json
from pathlib import Path

path_funding = Path(var_call_ELFjm2g7l2kEOVySoAInCYtq)
with open(path_funding, 'r') as f:
    funding = json.load(f)

path_docs = Path(var_call_J29yeOMELS731r2418tZwZIr)
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = ' '.join(d['text'] for d in docs)

sections = re.split(r'Capital Improvement Projects \(Design\)', texts, flags=re.I)
projects_design = []
if len(sections) > 1:
    after = sections[1]
    after = re.split(r'Capital Improvement Projects \(Construction\)', after, flags=re.I)[0]
    lines = [l.strip() for l in after.split('\n') if l.strip()]
    for l in lines:
        if len(l) > 3 and len(l) < 200 and not l.endswith(':') and not l.lower().startswith(('updates','project schedule','estimated schedule')):
            if re.search(r'[A-Z][a-z]+', l):
                projects_design.append(l)

projects_design = list(dict.fromkeys(projects_design))

more = re.findall(r'([A-Z][\w\s&]+?)\s*\(Design\)', texts)
for m in more:
    projects_design.append(m.strip())
projects_design = list(dict.fromkeys(projects_design))

capital_design_projects = set(projects_design)

funded_names = [r['Project_Name'] for r in funding]

count = 0
for name in funded_names:
    for pname in capital_design_projects:
        if name == pname or name.startswith(pname + ' '):
            count += 1
            break

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_ELFjm2g7l2kEOVySoAInCYtq': 'file_storage/call_ELFjm2g7l2kEOVySoAInCYtq.json', 'var_call_J29yeOMELS731r2418tZwZIr': 'file_storage/call_J29yeOMELS731r2418tZwZIr.json'}

exec(code, env_args)

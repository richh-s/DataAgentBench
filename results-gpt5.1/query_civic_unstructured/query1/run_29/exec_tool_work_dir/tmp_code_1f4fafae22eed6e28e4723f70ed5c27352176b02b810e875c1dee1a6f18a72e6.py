code = """import re, json
from pathlib import Path

# Load full funding results
path_funding = Path(var_call_ELFjm2g7l2kEOVySoAInCYtq)
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Load civic docs texts
path_docs = Path(var_call_J29yeOMELS731r2418tZwZIr)
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = ' '.join(d['text'] for d in docs)

# Identify capital projects with design status from text heuristically
sections = re.split(r'Capital Improvement Projects \(Design\)', texts, flags=re.I)
projects_design = []
if len(sections) > 1:
    after = sections[1]
    # up to next major heading
    after = re.split(r'Capital Improvement Projects \(Construction\)', after, flags=re.I)[0]
    # project names are lines with title case and not too long
    lines = [l.strip() for l in after.split('\n') if l.strip()]
    for i,l in enumerate(lines):
        if len(l) > 3 and len(l) < 200 and not l.endswith(':') and not l.lower().startswith(('updates','project schedule','estimated schedule')):
            # crude filter: contains at least one space and capital letters
            if re.search(r'[A-Z][a-z]+', l):
                projects_design.append(l)

projects_design = list(dict.fromkeys(projects_design))

# Also gather any other capital projects explicitly tagged as design
more = re.findall(r'([A-Z][\w\s&]+?)\s*\(Design\)', texts)
for m in more:
    projects_design.append(m.strip())
projects_design = list(dict.fromkeys(projects_design))

# From these, treat all as type capital with status design
capital_design_projects = set(projects_design)

# Join with funding where amount>50000
funded_names = [r['Project_Name'] for r in funding]

count = 0
for name in funded_names:
    # match if funding project name starts with or equals a capital design project name
    for pname in capital_design_projects:
        if name == pname or name.startswith(pname + ' '):
            count += 1
            break

result = count

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ELFjm2g7l2kEOVySoAInCYtq': 'file_storage/call_ELFjm2g7l2kEOVySoAInCYtq.json', 'var_call_J29yeOMELS731r2418tZwZIr': 'file_storage/call_J29yeOMELS731r2418tZwZIr.json'}

exec(code, env_args)

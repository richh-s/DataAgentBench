code = """import json
with open(var_call_3n0zhR3tgtTKd2yTjEpxx45r, 'r') as f:
    funding_projects = json.load(f)
funding_project_names = set([p['Project_Name'].lower() for p in funding_projects])
with open(var_call_qmiqQY26wMYIpOh9TbMw6yrS, 'r') as f:
    civic_docs = json.load(f)
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '').lower()
    lines = text.split('\n')
    # Look for section that starts with 'capital improvement projects (design)'
    found_section = False
    for i, line in enumerate(lines):
        if 'capital improvement projects (design)' in line:
            found_section = True
            # Look for next 15 lines for project names
            for j in range(i+1, min(i+16, len(lines))):
                candidate = lines[j].strip()
                if 5 < len(candidate) < 80 and (('project' in candidate) or ('repair' in candidate) or ('storm drain' in candidate) or ('skate park' in candidate)):
                    name = candidate.split(',')[0].split(':')[0].strip()
                    design_projects.add(name)
            break
matched_design_projects = set()
for design in design_projects:
    if design in funding_project_names:
        matched_design_projects.add(design)
count = len(matched_design_projects)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_3n0zhR3tgtTKd2yTjEpxx45r': 'file_storage/call_3n0zhR3tgtTKd2yTjEpxx45r.json', 'var_call_qmiqQY26wMYIpOh9TbMw6yrS': 'file_storage/call_qmiqQY26wMYIpOh9TbMw6yrS.json'}

exec(code, env_args)

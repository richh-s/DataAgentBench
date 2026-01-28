code = """import json
with open(var_call_3n0zhR3tgtTKd2yTjEpxx45r, 'r') as f:
    funding_projects = json.load(f)
funding_project_names = set([p['Project_Name'] for p in funding_projects])
with open(var_call_qmiqQY26wMYIpOh9TbMw6yrS, 'r') as f:
    civic_docs = json.load(f)
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '').lower()
    # Find sections related to capital projects, status 'design', and grab project names
    # heuristic: lines containing 'capital', 'design', and a plausible project name
    lines = text.split('\n')
    for line in lines:
        if 'capital' in line and 'design' in line:
            # try to parse possible project names next to status keywords
            line_parts = line.split('(')
            for part in line_parts:
                part = part.strip()
                # exclude generic headings and lines
                if 5 < len(part) < 90 and ('project' in part or 'repair' in part):
                    # extract name before first ',' or ')' or ':'
                    name = part.split(',')[0].split(')')[0].split(':')[0].strip()
                    design_projects.add(name)
        # also scan for headings "Capital Improvement Projects (Design)"
        if 'capital improvement projects' in line and '(design)' in line:
            # next 10 lines likely have project names
            idx = lines.index(line)
            for follow in lines[idx + 1:idx + 11]:
                if follow.strip() and len(follow.strip()) < 80 and (('project' in follow) or ('repair' in follow) or ('storm drain' in follow) or ('skate park' in follow)):
                    nm = follow.strip().split(',')[0].split(':')[0]
                    if nm and len(nm) > 5:
                        design_projects.add(nm)
design_funded = 0
for proj in design_projects:
    # match on lowercased names
    for fund_name in funding_project_names:
        if fund_name.lower() == proj.lower():
            design_funded += 1
            break
print('__RESULT__:')
print(json.dumps(design_funded))"""

env_args = {'var_call_3n0zhR3tgtTKd2yTjEpxx45r': 'file_storage/call_3n0zhR3tgtTKd2yTjEpxx45r.json', 'var_call_qmiqQY26wMYIpOh9TbMw6yrS': 'file_storage/call_qmiqQY26wMYIpOh9TbMw6yrS.json'}

exec(code, env_args)

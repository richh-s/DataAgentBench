code = """import json

# Funded projects
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funded = json.load(f)
funded_names = set(project['Project_Name'].strip().lower() for project in funded)

# Civic document text
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    docs = json.load(f)

def get_design_projects(txt):
    section = txt.lower().split('capital improvement projects (design)')
    if len(section) < 2:
        return []
    lines = section[1].split('\n')
    projects = []
    for line in lines:
        l = line.strip()
        if l.startswith('capital improvement projects (construction)') or l.startswith('capital improvement projects (not started)') or l.startswith('discussion:') or l.startswith('public works commission'):
            break
        if 'project' in l and 'updates' not in l and 'schedule' not in l and ':' not in l:
            projects.append(l.lower())
    return projects

design_projects = set()
for doc in docs:
    design_projects.update(get_design_projects(doc.get('text','')))

matching = funded_names.intersection(design_projects)
print("__RESULT__:")
print(json.dumps(len(matching)))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

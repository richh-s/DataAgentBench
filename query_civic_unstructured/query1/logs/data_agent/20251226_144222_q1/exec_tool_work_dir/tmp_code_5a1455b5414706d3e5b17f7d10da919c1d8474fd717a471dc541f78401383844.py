code = """import json

with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funded = json.load(f)
funded_names = set(p['Project_Name'].strip().lower() for p in funded)

with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    docs = json.load(f)

design_projects = set()
for doc in docs:
    try:
        section = doc['text'].lower().split('capital improvement projects (design)')[1]
    except Exception:
        continue
    lines = section.split('\n')
    for line in lines:
        l = line.strip()
        if l.startswith('capital improvement projects (construction)') or l.startswith('capital improvement projects (not started)') or l.startswith('discussion:') or l.startswith('public works commission'):
            break
        if 'project' in l and not any(w in l for w in ['updates', 'schedule', ':']):
            design_projects.add(l)

matching = funded_names.intersection(design_projects)
print("__RESULT__:")
print(json.dumps(len(matching)))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

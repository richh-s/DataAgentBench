code = """import json

# Load funded projects
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV,'r') as f:
    funded = json.load(f)
funded_names = set(x['Project_Name'].strip().lower() for x in funded)

# Load civic docs
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6,'r') as f:
    docs = json.load(f)

design_projects = set()
for doc in docs:
    txt = doc.get('text','').lower()
    if 'capital improvement projects (design)' in txt:
        section = txt.split('capital improvement projects (design)')[1]
        done = False
        for line in section.split('\n'):
            if any(line.strip().startswith(xx) for xx in ['capital improvement projects (construction)','capital improvement projects (not started)','discussion:','public works commission']):
                break
            L = line.strip()
            if 'project' in L and not any(x in L for x in ['updates','schedule',':']):
                design_projects.add(L)

matching = funded_names & design_projects
print("__RESULT__:")
print(json.dumps(len(matching)))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

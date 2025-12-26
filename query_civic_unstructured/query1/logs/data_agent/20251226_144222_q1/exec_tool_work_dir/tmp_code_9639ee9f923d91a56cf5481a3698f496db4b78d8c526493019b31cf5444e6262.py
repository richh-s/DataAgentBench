code = """import json

# Load funded projects
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funded = json.load(f)
funded_names = set(x['Project_Name'].strip().lower() for x in funded)

# Load civic docs
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    docs = json.load(f)

def extract_design_projects(text):
    results = []
    try:
        part = text.lower().split('capital improvement projects (design)')[1]
    except:
        return results
    lines = part.split('\n')
    for line in lines:
        l = line.strip()
        if l.startswith('capital improvement projects (construction)') or l.startswith('capital improvement projects (not started)') or l.startswith('discussion:') or l.startswith('public works commission'):
            break
        # Heuristic: is a project name if 'project' in it and not in excluded words
        if 'project' in l and not any(w in l for w in ['updates', 'schedule', ':']):
            results.append(l.lower())
    return results

design_projects = set()
for doc in docs:
    design_projects.update(extract_design_projects(doc.get('text','')))

matching = funded_names & design_projects
print("__RESULT__:")
print(json.dumps(len(matching)))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

code = """import json

# Read funded projects (amount > $50,000)
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funded = json.load(f)
funded_names = set([x['Project_Name'].lower().strip() for x in funded])

# Read civic docs documents
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    docs = json.load(f)

design_projects = set()
for doc in docs:
    txt = doc.get('text', '').lower()
    marker = 'capital improvement projects (design)'
    if marker in txt:
        section = txt.split(marker)[1]
        for line in section.split('\n'):
            stopwords = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'discussion:', 'public works commission']
            if any(sw in line for sw in stopwords):
                break
            l = line.strip()
            if 'project' in l and not any(k in l for k in ['updates', 'schedule', ':']):
                design_projects.add(l)

# Intersection
answer = len(funded_names & design_projects)
print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

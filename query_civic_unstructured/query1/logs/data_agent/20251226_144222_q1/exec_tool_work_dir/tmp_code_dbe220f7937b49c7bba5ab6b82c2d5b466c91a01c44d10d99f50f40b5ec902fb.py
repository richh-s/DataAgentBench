code = """import json

# Load funding data
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funding_data = json.load(f)
funded_projects = set([item['Project_Name'].strip().lower() for item in funding_data])

# Load civic docs data
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    civic_docs = json.load(f)

design_projects = set()
for doc in civic_docs:
    text = doc.get('text','').lower()
    if 'capital improvement projects (design)' in text:
        # The section for "Capital Improvement Projects (Design)"
        section = text.split('capital improvement projects (design)')[1]
        # End when a new section header is found
        for line in section.split('\n'):
            line_stripped = line.strip()
            if any(x in line_stripped for x in [
                'capital improvement projects (construction)',
                'capital improvement projects (not started)',
                'discussion:', 'public works commission']):
                break
            if 'project' in line_stripped and not any(w in line_stripped for w in ['update', 'schedule', ':']):
                design_projects.add(line_stripped)

# Intersection: projects with both funding > $50,000 and design status
matching = funded_projects & design_projects
print("__RESULT__:")
print(json.dumps(len(matching)))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

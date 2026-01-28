code = """import json

# Load funding data
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funding_data = json.load(f)
funded_projects = set([item['Project_Name'].strip().lower() for item in funding_data])

# Load civic docs data
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    civic_docs = json.load(f)

def is_section_end(line):
    headers = ['capital improvement projects (construction)',
               'capital improvement projects (not started)',
               'discussion:',
               'public works commission']
    return any(header in line for header in headers)

design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'capital improvement projects (design)' in text:
        section = text.split('capital improvement projects (design)')[1]
        for line in section.split('\n'):
            line_stripped = line.strip()
            if is_section_end(line_stripped):
                break
            if ('project' in line_stripped) and not any(w in line_stripped for w in ['updates', 'schedule', ':']):
                design_projects.add(line_stripped)

result = len(funded_projects.intersection(design_projects))
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

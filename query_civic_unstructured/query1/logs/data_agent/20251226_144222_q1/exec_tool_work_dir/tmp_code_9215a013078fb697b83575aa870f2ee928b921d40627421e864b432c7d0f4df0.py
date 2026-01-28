code = """import json
import pandas as pd

# Load funding data
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funding_data = json.load(f)

funded_projects = set([item['Project_Name'].strip().lower() for item in funding_data])

# Load civic doc database
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    docs_data = json.load(f)

design_projects = set()
for doc in docs_data:
    text = doc.get('text', '').lower()
    if 'capital improvement projects (design)' in text:
        section = text.split('capital improvement projects (design)')[1]
        end_candidates = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'discussion:', 'public works commission']
        end_idx = len(section)
        for candidate in end_candidates:
            idx = section.find(candidate)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        design_text = section[:end_idx]
        # split into lines
        lines = design_text.split('\n')
        # find likely project names: look for blank lines followed by text before details
        for i, line in enumerate(lines):
            line = line.strip()
            if line and ('updates:' in lines[i+1].lower() if i+1 < len(lines) else False):
                if 'project' in line:
                    design_projects.add(line)
# Lowercase matching
design_projects = set([p.strip().lower() for p in design_projects])
capital_design_projects_with_funding = funded_projects.intersection(design_projects)
result = len(capital_design_projects_with_funding)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

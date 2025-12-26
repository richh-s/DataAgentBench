code = """import json
import pandas as pd

# Step 1: Load funded projects (Amount > 50000)
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funding_data = json.load(f)

funded_project_names = set([item['Project_Name'].strip().lower() for item in funding_data])

# Step 2: Load civic docs
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    civic_docs = json.load(f)

def extract_design_projects(text):
    # Only parse lines under Capital Improvement Projects (Design) section
    lines = text.split('\n')
    found_design = False
    design_projects = set()
    for i, line in enumerate(lines):
        clean_line = line.strip().lower()
        if 'capital improvement projects (design)' in clean_line:
            found_design = True
            continue
        if found_design:
            # Section ends when meeting next major section
            if ('capital improvement projects (construction)' in clean_line
                or 'capital improvement projects (not started)' in clean_line
                or 'discussion:' in clean_line):
                break
            # Likely project name line (heuristic: not empty, does not start with bullet or header, contains 'project', not 'updates', not 'schedule', and not too long)
            if (clean_line and 'project' in clean_line and not 'updates' in clean_line
                and not 'schedule' in clean_line and len(clean_line)<80):
                design_projects.add(clean_line)
    return design_projects

all_design_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    design_projects = extract_design_projects(text)
    all_design_projects.update(design_projects)

# Step 3: Intersect funded projects and capital projects in design status
n_matching_projects = len(funded_project_names.intersection(all_design_projects))
print("__RESULT__:")
print(json.dumps(n_matching_projects))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import re

# Load funding data
with open(locals()['var_function-call-13970698935459151877'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(float)
# Group by Project_Name and sum Amount
df_funding_grouped = df_funding.groupby('Project_Name')['Amount'].sum().reset_index()
# Filter > 50000
funded_projects = set(df_funding_grouped[df_funding_grouped['Amount'] > 50000]['Project_Name'])

# Load civic docs
with open(locals()['var_function-call-13579203068557831030'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

# Helper to identify project name lines
def is_project_name(line):
    line = line.strip()
    if not line: return False
    # Skip bullets and common labels
    if line.startswith('(cid:') or line.startswith('Updates:') or line.startswith('Project Schedule:'):
        return False
    if line.startswith('Page ') or line.startswith('Agenda Item'):
        return False
    if line.lower().startswith('complete design:') or line.lower().startswith('advertise:') or line.lower().startswith('begin construction:'):
        return False
    if "estimated schedule" in line.lower(): return False
    if "project description" in line.lower(): return False
    if "project updates" in line.lower(): return False
    return True

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_capital_design = False
    
    for line in lines:
        stripped = line.strip()
        
        # Check for section headers
        if "Capital Improvement Projects (Design)" in stripped:
            in_capital_design = True
            continue
        elif "Capital Improvement Projects (" in stripped: # Any other status
            in_capital_design = False
            continue
        elif "Disaster Recovery Projects" in stripped:
            in_capital_design = False
            continue
        
        if in_capital_design:
            if is_project_name(line):
                # Clean up name
                name = stripped
                # Sometimes names might have extra chars, but let's assume lines are clean
                capital_design_projects.add(name)

# Intersection
result_projects = capital_design_projects.intersection(funded_projects)
count = len(result_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "projects": list(result_projects), "capital_design_candidates": list(capital_design_projects)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)

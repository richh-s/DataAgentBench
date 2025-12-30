code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-13970698935459151877'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce').fillna(0)
# Group by Project_Name and sum Amount
df_funding_grouped = df_funding.groupby('Project_Name')['Amount'].sum().reset_index()
# Filter > 50000
funded_projects = set(df_funding_grouped[df_funding_grouped['Amount'] > 50000]['Project_Name'])

# Load civic docs
with open(locals()['var_function-call-13579203068557831030'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

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
        elif "Capital Improvement Projects (" in stripped and "Design" not in stripped:
            in_capital_design = False
            continue
        elif "Disaster Recovery Projects" in stripped:
            in_capital_design = False
            continue
        elif "Agenda Item" in stripped and "Page" in stripped: 
            # Footer often resets context or just noise, but strictly section headers control state
            pass
            
        if in_capital_design:
            if not stripped: continue
            if stripped.startswith("(cid:") or stripped.startswith("Updates:") or stripped.startswith("Project Schedule:") or stripped.startswith("Estimated Schedule:"):
                continue
            if stripped.startswith("Page ") or stripped.startswith("Agenda Item"):
                continue
            if stripped.startswith("Complete Design") or stripped.startswith("Advertise") or stripped.startswith("Begin Construction") or stripped.startswith("Final Design"):
                continue
            if "Project Description" in stripped or "Project Updates" in stripped:
                continue
            
            # Likely a project name
            capital_design_projects.add(stripped)

# Intersection
result_projects = capital_design_projects.intersection(funded_projects)
count = len(result_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "matches": list(result_projects), "found_design": list(capital_design_projects)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)

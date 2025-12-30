code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-7811788439429183235'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-3690034761458033571'], 'r') as f:
    civic_docs = json.load(f)

def normalize(text):
    return re.sub(r'\s+', ' ', text).strip()

funding_project_names = set(funding_df['Project_Name'].apply(normalize).tolist())

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    current_dates = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check if line is a project name
        is_new_project = False
        norm_line = normalize(line)
        
        # Logic: If it's in funding names OR followed by "Updates:"
        if norm_line in funding_project_names:
            is_new_project = True
        elif i + 1 < len(lines) and ("Updates:" in lines[i+1] or "Project Description:" in lines[i+1]):
             # Avoid false positives like "Agenda Item"
             if "Agenda Item" not in line:
                 is_new_project = True
        
        if is_new_project:
            if current_project:
                extracted_projects.append({'name': current_project, 'dates': current_dates})
            current_project = norm_line
            current_dates = []
        elif current_project:
            if "Begin" in line or "Start" in line:
                current_dates.append(line)
    
    if current_project:
        extracted_projects.append({'name': current_project, 'dates': current_dates})

# Filter
disaster_keywords = ["FEMA", "CalOES", "CalJPIA"]
qualifying_projects = set()

for p in extracted_projects:
    name = p['name']
    # Check type
    if any(k in name for k in disaster_keywords):
        # Check start date 2022
        # We want to know if it started in 2022. 
        # Check if any date line mentions 2022
        for d in p['dates']:
            if "2022" in d:
                qualifying_projects.add(name)

# Calculate Total
total = 0
matched_list = []
for name in qualifying_projects:
    row = funding_df[funding_df['Project_Name'].apply(normalize) == name]
    if not row.empty:
        amt = int(row.iloc[0]['Amount'])
        total += amt
        matched_list.append(name)

print("__RESULT__:")
print(json.dumps({'total': total, 'matched_projects': matched_list}))"""

env_args = {'var_function-call-7811788439429183235': 'file_storage/function-call-7811788439429183235.json', 'var_function-call-3690034761458033571': 'file_storage/function-call-3690034761458033571.json'}

exec(code, env_args)

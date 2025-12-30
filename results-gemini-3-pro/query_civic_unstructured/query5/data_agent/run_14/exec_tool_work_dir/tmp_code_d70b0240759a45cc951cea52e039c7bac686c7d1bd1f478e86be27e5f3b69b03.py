code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-7811788439429183235'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load Civic Docs
with open(locals()['var_function-call-3690034761458033571'], 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize strings for matching
def normalize(text):
    return re.sub(r'\s+', ' ', text).strip()

funding_project_names = set(funding_df['Project_Name'].apply(normalize).tolist())

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_info = {}
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        candidate_name = normalize(line_stripped)
        
        # Check next line for indicators
        next_line = ""
        if i + 1 < len(lines):
             next_line = lines[i+1].strip()
        
        is_project_start = False
        if candidate_name in funding_project_names:
            is_project_start = True
        elif "Updates:" in next_line or "Project Description:" in next_line:
            # Heuristic: Valid project names usually aren't just "Updates:" or "Project Description:"
            if len(candidate_name) > 3 and "Agenda Item" not in candidate_name:
                is_project_start = True
                candidate_name = candidate_name.replace("(cid:190)", "").strip()
        
        if is_project_start:
            if current_project:
                extracted_projects.append(current_info)
            
            current_project = candidate_name
            current_info = {
                'Project_Name': current_project,
                'dates': []
            }
        elif current_project:
            # Check for dates
            if "Begin" in line_stripped or "Start" in line_stripped:
                current_info['dates'].append(line_stripped)

    if current_project:
        extracted_projects.append(current_info)

results = []
disaster_keywords = ["FEMA", "CalOES", "CalJPIA"]

for p in extracted_projects:
    name = p['Project_Name']
    is_disaster = any(k in name for k in disaster_keywords)
    
    started_2022 = False
    for d_str in p['dates']:
        if "2022" in d_str and ("Begin" in d_str or "Start" in d_str):
            started_2022 = True
    
    if is_disaster and started_2022:
        results.append(name)

unique_results = list(set(results))

total_funding = 0
matched_details = []
for name in unique_results:
    row = funding_df[funding_df['Project_Name'].apply(normalize) == normalize(name)]
    if not row.empty:
        amount = int(row.iloc[0]['Amount'])
        total_funding += amount
        matched_details.append({"name": name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_details}))"""

env_args = {'var_function-call-7811788439429183235': 'file_storage/function-call-7811788439429183235.json', 'var_function-call-3690034761458033571': 'file_storage/function-call-3690034761458033571.json'}

exec(code, env_args)

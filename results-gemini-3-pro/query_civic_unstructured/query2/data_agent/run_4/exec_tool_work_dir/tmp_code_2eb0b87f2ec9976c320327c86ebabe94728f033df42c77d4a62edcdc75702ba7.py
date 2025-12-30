code = """import json
import pandas as pd
import re

# Load the data
with open(locals()['var_function-call-10494056103338850643'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10332075929140261895'], 'r') as f:
    funding_data = json.load(f)

# Convert funding to DataFrame
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

found_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Identify indices of project names
    name_indices = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Look ahead for marker
        is_name = False
        for j in range(i + 1, min(i + 5, len(lines))):
            next_line = lines[j].strip()
            if not next_line:
                continue
            if '(cid:190)' in next_line:
                is_name = True
            break # Stop at first non-empty line
        
        if is_name:
            name_indices.append(i)
            
    # Extract blocks
    for k in range(len(name_indices)):
        start_idx = name_indices[k]
        end_idx = name_indices[k+1] if k + 1 < len(name_indices) else len(lines)
        
        project_name = lines[start_idx].strip()
        project_text = "\n".join(lines[start_idx:end_idx])
        
        found_projects.append({
            'name': project_name,
            'text': project_text
        })

# Filter projects
completed_park_projects = set()

for p in found_projects:
    name = p['name']
    text = p['text']
    
    # Check if park related
    if 'park' in name.lower() or 'playground' in name.lower():
        # Check completion in 2022
        # Look for line containing 'completed' or 'complete construction' AND '2022'
        lines = text.split('\n')
        is_completed_2022 = False
        for line in lines:
            l = line.lower()
            if '2022' in l:
                if 'completed' in l or 'complete construction' in l:
                    is_completed_2022 = True
                    break
        
        if is_completed_2022:
            completed_park_projects.add(name)

# Calculate funding
# Filter funding dataframe
# Note: extracted names might need exact match
matched_funding = df_funding[df_funding['Project_Name'].isin(completed_park_projects)]
total_funding = matched_funding['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": list(completed_park_projects),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-17786645428432444760': ['civic_docs'], 'var_function-call-17786645428432443965': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-9932309007747960995': 'file_storage/function-call-9932309007747960995.json', 'var_function-call-10494056103338850643': 'file_storage/function-call-10494056103338850643.json', 'var_function-call-10332075929140261895': 'file_storage/function-call-10332075929140261895.json'}

exec(code, env_args)

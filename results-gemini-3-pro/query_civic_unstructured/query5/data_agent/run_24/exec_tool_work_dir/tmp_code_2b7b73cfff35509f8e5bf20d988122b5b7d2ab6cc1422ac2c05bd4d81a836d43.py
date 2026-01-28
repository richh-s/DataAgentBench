code = """import json
import pandas as pd

# Load civic docs
with open(locals()['var_function-call-2498552123289550299'], 'r') as f:
    docs = json.load(f)

# Load funding data
funding_df = pd.DataFrame(json.load(open(locals()['var_function-call-4052442815910590834'])))

projects = []

for doc in docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_project = None
    project_content_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if "Updates:" in line:
            title = None
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if prev_line:
                    title = prev_line
                    break
            
            if title:
                if current_project:
                    content = " ".join(project_content_lines)
                    st_chunk = ""
                    if "Begin Construction:" in content:
                        idx = content.find("Begin Construction:")
                        st_chunk = content[idx:idx+50]
                    
                    started_2022 = False
                    if "2022" in st_chunk:
                        started_2022 = True
                    
                    is_disaster = False
                    upper_content = content.upper()
                    upper_name = current_project['name'].upper()
                    if any(x in upper_name or x in upper_content for x in ["FEMA", "CALOES", "CALJPIA", "DISASTER"]):
                        is_disaster = True
                    
                    current_project['started_2022'] = started_2022
                    current_project['is_disaster'] = is_disaster
                    projects.append(current_project)
                
                current_project = {'name': title}
                project_content_lines = []
        
        if current_project:
            project_content_lines.append(line)

    if current_project:
        content = " ".join(project_content_lines)
        st_chunk = ""
        if "Begin Construction:" in content:
            idx = content.find("Begin Construction:")
            st_chunk = content[idx:idx+50]
        
        started_2022 = False
        if "2022" in st_chunk:
            started_2022 = True
            
        is_disaster = False
        upper_content = content.upper()
        upper_name = current_project['name'].upper()
        if any(x in upper_name or x in upper_content for x in ["FEMA", "CALOES", "CALJPIA", "DISASTER"]):
            is_disaster = True
            
        current_project['started_2022'] = started_2022
        current_project['is_disaster'] = is_disaster
        projects.append(current_project)

# Filter
target_projects = []
for p in projects:
    if p['is_disaster'] and p['started_2022']:
        target_projects.append(p)

# Collect Funding IDs
matched_funding_ids = set()

for p in target_projects:
    p_name = p['name']
    
    # Match funding
    matches = funding_df[
        (funding_df['Project_Name'] == p_name) | 
        (funding_df['Project_Name'].str.startswith(p_name + " ("))
    ]
    
    for fid in matches['Funding_ID'].values:
        matched_funding_ids.add(fid)

# Sum amount for unique IDs
total_funding = 0
if matched_funding_ids:
    total_funding = funding_df[funding_df['Funding_ID'].isin(matched_funding_ids)]['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({"total_funding": int(total_funding), "matched_ids": list(matched_funding_ids)}))"""

env_args = {'var_function-call-2498552123289550299': 'file_storage/function-call-2498552123289550299.json', 'var_function-call-4052442815910590834': 'file_storage/function-call-4052442815910590834.json', 'var_function-call-6314395038111642624': {'total_funding': 518000, 'breakdown': [{'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'amount': 81000}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': 44000}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': 43000}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'amount': 81000}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': 44000}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': 43000}]}}

exec(code, env_args)

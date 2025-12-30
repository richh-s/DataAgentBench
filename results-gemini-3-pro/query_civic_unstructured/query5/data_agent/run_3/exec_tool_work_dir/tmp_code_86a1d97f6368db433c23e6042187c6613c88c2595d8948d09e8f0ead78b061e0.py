code = """import json
import pandas as pd
import re
import os

civic_docs_var = locals()['var_function-call-72276613876208038']
funding_var = locals()['var_function-call-9094127879311422561']

# Load Civic Docs
if isinstance(civic_docs_var, str) and os.path.exists(civic_docs_var):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

# Load Funding
if isinstance(funding_var, str) and os.path.exists(funding_var):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var

funding_df = pd.DataFrame(funding_data)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_section = "Unknown"
    current_project = None
    project_buffer = [] 
    
    def save_project(name, buffer, section):
        if not name: return
        full_text = " ".join(buffer)
        
        # Regex for Start Date
        st = None
        # Look for "Begin Construction: <Date>"
        match = re.search(r"(?:Begin Construction|Start|Commence Construction)[:\s]+([A-Za-z0-9\s,]+)", full_text, re.IGNORECASE)
        if match:
            st = match.group(1).strip()
            # truncate
            if len(st) > 50: st = st[:50]
        
        p_type = "capital"
        if "Disaster" in section:
            p_type = "disaster"
        elif "(FEMA Project)" in name or "(CalJPIA Project)" in name or "(CalOES Project)" in name:
            p_type = "disaster"
        elif "Woolsey Fire" in full_text:
            p_type = "disaster"
            
        projects.append({
            "Project_Name": name,
            "type": p_type,
            "st": st,
            "section": section,
            "full_text_preview": full_text[:100]
        })

    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        if "Capital Improvement Projects" in line:
            current_section = "Capital Improvement Projects"
        if "Disaster Recovery Projects" in line:
            current_section = "Disaster Recovery Projects"
        
        # Detect Project Name
        is_project_name = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check for (cid:190) or Updates
            # Also check if line is not too long
            if ("Updates:" in next_line or next_line.startswith("(cid")) and len(line) < 100:
                 if "Page" not in line and "Agenda" not in line:
                     is_project_name = True
        
        if is_project_name:
            if current_project:
                save_project(current_project, project_buffer, current_section)
            current_project = line
            project_buffer = []
        else:
            if current_project:
                project_buffer.append(line)
    
    if current_project:
        save_project(current_project, project_buffer, current_section)

projects_df = pd.DataFrame(projects)

# Filter
projects_df['is_disaster'] = projects_df['type'] == 'disaster'
projects_df['started_2022'] = projects_df['st'].fillna('').str.contains("2022")

target_projects = projects_df[projects_df['is_disaster'] & projects_df['started_2022']].copy()

# Clean names
target_projects['Project_Name'] = target_projects['Project_Name'].str.strip()
funding_df['Project_Name'] = funding_df['Project_Name'].str.strip()
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

merged = pd.merge(target_projects, funding_df, on='Project_Name', how='inner')
total = merged['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "total_funding": total,
    "merged_projects": merged[['Project_Name', 'Amount', 'st']].to_dict(orient='records'),
    "projects_dump": projects_df[['Project_Name', 'type', 'st']].head(10).to_dict(orient='records')
}))"""

env_args = {'var_function-call-9094127879311422366': 'file_storage/function-call-9094127879311422366.json', 'var_function-call-9094127879311422561': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-72276613876208038': 'file_storage/function-call-72276613876208038.json'}

exec(code, env_args)

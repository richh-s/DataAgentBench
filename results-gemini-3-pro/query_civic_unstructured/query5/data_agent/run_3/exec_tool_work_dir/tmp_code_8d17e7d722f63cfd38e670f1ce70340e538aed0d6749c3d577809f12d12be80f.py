code = """import json
import pandas as pd
import re

civic_docs_path = locals()['var_function-call-72276613876208038']
funding_path = locals()['var_function-call-9094127879311422561']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = "Unknown"
    current_project = None
    project_buffer = [] 
    
    def save_project(name, buffer, section):
        if not name: return
        full_text = " ".join(buffer)
        
        # Regex for Start Date
        # Need to match: "Begin Construction: <Date>"
        # Using [\\s] to represent whitespace in regex when passed via JSON
        st = None
        st_match = re.search(r'(?:Begin Construction|Start|Commence Construction)[:\s]+([A-Za-z0-9\s,]+)', full_text, re.IGNORECASE)
        if st_match:
            st_str = st_match.group(1).strip()
            # Split by newline or long spaces to get just the date part
            st = st_str.split('  ')[0].strip()
            # Further clean: if it's too long (>30 chars), truncate
            if len(st) > 30: st = st[:30]
        
        p_type = "capital"
        if "Disaster" in section:
            p_type = "disaster"
        elif any(x in name for x in ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)"]):
            p_type = "disaster"
        elif "Woolsey Fire" in full_text: # additional check based on hint
            p_type = "disaster"
            
        projects.append({
            "Project_Name": name,
            "type": p_type,
            "st": st,
            "section": section
        })

    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        if "Capital Improvement Projects" in line:
            current_section = "Capital Improvement Projects"
            # Don't continue, as the line might be the header for the section but not a project
        if "Disaster Recovery Projects" in line:
            current_section = "Disaster Recovery Projects"
        
        # Detect Project Name
        # Heuristic: Line followed by "(cid:190)" or "Updates:"
        is_project_name = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") or "Updates:" in next_line:
                 if len(line) < 100 and not line.startswith("Page") and not line.startswith("Agenda"):
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
def check_date(d):
    if not d: return False
    return "2022" in d
projects_df['started_2022'] = projects_df['st'].apply(check_date)

target_projects = projects_df[projects_df['is_disaster'] & projects_df['started_2022']]

# Join
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
    "all_projects_debug": projects_df[['Project_Name', 'type', 'st']].head(10).to_dict(orient='records')
}))"""

env_args = {'var_function-call-9094127879311422366': 'file_storage/function-call-9094127879311422366.json', 'var_function-call-9094127879311422561': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-72276613876208038': 'file_storage/function-call-72276613876208038.json'}

exec(code, env_args)

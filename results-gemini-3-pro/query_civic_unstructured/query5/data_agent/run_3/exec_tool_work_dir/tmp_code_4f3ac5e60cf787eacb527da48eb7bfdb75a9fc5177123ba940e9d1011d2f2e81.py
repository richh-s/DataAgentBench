code = """import json
import pandas as pd
import re

# Load data
civic_docs_path = locals()['var_function-call-72276613876208038']
funding_path = locals()['var_function-call-9094127879311422561']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Funding data might be in a file or direct list depending on size. 
# The previous tool output said it's stored under key, but usually if it's small it's in the 'results' list directly?
# Wait, for the funding_db call, the result was small and printed in the message: "The result is stored under key..."
# Actually, the tool output message says: "The result is stored under key: var_function-call-..."
# This implies it's a file path string.
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Parse logic
projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = "Unknown"
    current_project = None
    project_buffer = [] # lines belonging to current project
    
    # Helper to save project
    def save_project(name, buffer, section):
        if not name: return
        # Join buffer to search for dates and keywords
        full_text = " ".join(buffer)
        
        # Extract Start Date
        # Patterns: "Begin Construction: <Date>", "Start: <Date>"
        # Date format examples: "Fall 2023", "April 2023", "2022-Spring"
        st = None
        st_match = re.search(r'(?:Begin Construction|Start|Commence Construction)[:\s]+([A-Za-z0-9\s,]+)', full_text, re.IGNORECASE)
        if st_match:
            # Take the first few words as date
            st_str = st_match.group(1).strip()
            # clean up: take until newline or reasonable length
            st = st_str.split('\n')[0].strip()
        
        # Determine Type
        p_type = "capital" # default
        # Check section
        if "Disaster" in section:
            p_type = "disaster"
        # Check name suffixes/keywords
        elif any(x in name for x in ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)"]):
            p_type = "disaster"
        # Check text for keywords? (Maybe risky, sticking to hints)
        # Hint says: "Disaster project names often include suffixes..."
        
        # Status? (Not strictly needed for filtering, but good to know)
        
        projects.append({
            "Project_Name": name,
            "type": p_type,
            "st": st,
            "raw_text": full_text[:200]
        })

    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check for Section Headers
        if "Capital Improvement Projects" in line:
            current_section = "Capital Improvement Projects"
            continue
        if "Disaster Recovery Projects" in line:
            current_section = "Disaster Recovery Projects"
            continue
            
        # Check for Project Name
        # Logic: If next line starts with "(cid:190)" (bullet) and contains "Updates" or "Project Description", this line is a name.
        # Look ahead
        is_project_name = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") or "Updates:" in next_line or "Project Description:" in next_line:
                 # It's likely a project name, but we need to be careful not to pick up garbage
                 if len(line) < 100 and not line.startswith("Page"):
                     is_project_name = True
        
        # Also check if the line itself ends with "Project" and looks like a header (heuristic)
        
        if is_project_name:
            # Save previous project
            if current_project:
                save_project(current_project, project_buffer, current_section)
            
            current_project = line
            project_buffer = []
        else:
            if current_project:
                project_buffer.append(line)
    
    # Save last project
    if current_project:
        save_project(current_project, project_buffer, current_section)

# Convert to DF
projects_df = pd.DataFrame(projects)

# Filter for Disaster + Start 2022
# Start date matching: "2022" in string
def is_start_2022(date_str):
    if not date_str: return False
    return "2022" in date_str

projects_df['is_disaster'] = projects_df['type'] == 'disaster'
projects_df['started_2022'] = projects_df['st'].apply(is_start_2022)

target_projects = projects_df[projects_df['is_disaster'] & projects_df['started_2022']]

# Join with Funding
# Clean Project_Name for join? Names should match.
# Let's strip whitespace.
target_projects['Project_Name'] = target_projects['Project_Name'].str.strip()
funding_df['Project_Name'] = funding_df['Project_Name'].str.strip()
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

merged = pd.merge(target_projects, funding_df, on='Project_Name', how='inner')

total_funding = merged['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "target_projects": target_projects[['Project_Name', 'st', 'type']].to_dict(orient='records'),
    "all_projects_sample": projects_df[['Project_Name', 'st', 'type']].head(5).to_dict(orient='records'),
    "funding_sample": funding_df.head(5).to_dict(orient='records')
}))"""

env_args = {'var_function-call-9094127879311422366': 'file_storage/function-call-9094127879311422366.json', 'var_function-call-9094127879311422561': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-72276613876208038': 'file_storage/function-call-72276613876208038.json'}

exec(code, env_args)

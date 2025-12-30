code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function_call_10631543890590275884'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function_call_10631543890590275137'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Ensure Amount is numeric
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

projects = []

# Helper to normalize dates
def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower().strip()
    if 'spring 2022' in date_str or 'spring, 2022' in date_str:
        return True
    # Check for months
    if '2022' in date_str:
        if 'march' in date_str or 'april' in date_str or 'may' in date_str:
            return True
        # Check numerical dates like 03/2022, 04/2022, 05/2022, 2022-03, etc.
        # Simple regex for numerical dates
        if re.search(r'(03|3)/(\d{1,2}/)?2022', date_str) or re.search(r'(04|4)/(\d{1,2}/)?2022', date_str) or re.search(r'(05|5)/(\d{1,2}/)?2022', date_str):
            return True
        if re.search(r'2022-(03|3)', date_str) or re.search(r'2022-(04|4)', date_str) or re.search(r'2022-(05|5)', date_str):
            return True
    return False

# Iterate documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    project_buffer = []
    
    # Simple state machine to capture project blocks
    # We assume a project starts with a Name and ends when the next project starts
    # We identify a project name by looking for lines that are not bullets and followed by "Updates:" or "Project Description" or "Project Schedule"
    
    # Refined parsing:
    # 1. Identify potential headers.
    # 2. Group lines into blocks.
    
    # Let's try to identify the Project Name lines.
    # From the sample:
    # "2022 Morning View Resurfacing & Storm Drain Improvements"
    # "(cid:190) Updates:"
    
    # "PCH Median Improvements Project"
    # "(cid:190) Updates:"
    
    # "Malibu Canyon Road Traffic Study"
    # "(cid:190) Project Description:"
    
    # So a line followed (maybe with empty lines in between) by a line starting with "(cid:190)" or "Updates:" etc.
    
    # Let's iterate and build a list of (ProjectName, TextBlock)
    
    doc_projects = []
    potential_name_idx = -1
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line indicates start of a section (bullet)
        is_bullet = line.startswith('(cid:190)') or line.startswith('(cid:131)') or line.startswith('Updates:') or line.startswith('Project Description:') or line.startswith('Project Schedule:')
        
        if is_bullet:
            # If we found a bullet, the previous non-empty line(s) might be the project name.
            # But we need to be careful about page headers.
            pass
    
    # Let's use a regex approach to split the text by Project Headers
    # We look for a line that does NOT start with special chars, and is shortly followed by "(cid:190)" lines.
    
    # Alternatively, split by "(cid:190)" and look backwards for the name.
    
    # Let's try parsing line by line.
    
    extracted_projects = {} # Name -> info
    
    current_name = None
    buffer_lines = []
    
    # We'll skip the first few lines which are agenda headers.
    # "Subject: Capital Improvement Projects..."
    # "DISCUSSION:"
    
    # Scan for lines that look like project names
    # Heuristic: A line that is Uppercase or Title Case, longer than 3 chars, not in ignore list, 
    # and followed by lines containing "Updates" or "Project Description" or "Project Schedule".
    
    ignore_list = ["Page", "Agenda Item", "Public Works", "Commission", "Date prepared", "Meeting date", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:", "Capital Improvement Projects", "Updates:", "Project Schedule:", "Project Description:"]
    
    clean_lines = [l.strip() for l in lines if l.strip()]
    
    # It's hard to get perfect splitting. 
    # Let's look for known keys in the text structure.
    # Keys: "(cid:190) Updates:", "(cid:190) Project Description:", "(cid:190) Project Schedule:", "(cid:190) Estimated Schedule:", "(cid:190) Complete Construction:"
    
    # We can iterate through the text, finding these keys. The text *before* the first key of a block is likely the Project Name.
    
    # Find all indices of lines starting with "(cid:190)"
    bullet_indices = [i for i, l in enumerate(clean_lines) if l.startswith('(cid:190)')]
    
    if not bullet_indices:
        continue
        
    # Group bullet indices into clusters (projects)
    # Usually a project has multiple bullets. The Project Name is before the first bullet of the cluster.
    # How to determine when a new cluster starts?
    # Usually the Project Name is explicitly written.
    # If there is a "gap" in topics or a new Name line.
    
    # Let's look at the line before the FIRST bullet of a sequence.
    # "2022 Morning View..." -> (cid:190) Updates
    # ...
    # (cid:131) Begin Construction...
    # [Next Project Name] -> (cid:190) Updates
    
    # So if we see a line that is NOT a bullet (starts with (cid:190) or (cid:131)) and is not a continuation of a sentence, it might be a header.
    
    # Better approach:
    # Iterate clean_lines.
    # If line starts with "(cid:190)", it's a section start.
    # The line(s) before it (that are not bullets) form the Project Name.
    # Once inside a project, we collect lines until we hit a new Project Name.
    # How to identify a new Project Name? It's a line that doesn't start with (cid:190) or (cid:131) and is followed eventually by (cid:190).
    
    current_proj_lines = []
    current_proj_name = None
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Check if this line is a Project Name candidate
        # It must be followed by (cid:190) lines within 1-2 lines
        is_name = False
        if not line.startswith('(') and "Page" not in line and "Agenda" not in line and "Capital Improvement Projects" not in line and "DISCUSSION" not in line:
            # Look ahead
            for k in range(1, 4): # Look ahead up to 3 lines
                if i + k < len(clean_lines):
                    if clean_lines[i+k].startswith('(cid:190)'):
                        is_name = True
                        break
                    if clean_lines[i+k].startswith('(') and not clean_lines[i+k].startswith('(cid:190)'):
                         # Maybe (131) or something, but usually (190) starts sections
                         pass
        
        if is_name:
            # Save previous project
            if current_proj_name:
                extracted_projects[current_proj_name] = "\n".join(current_proj_lines)
            
            current_proj_name = line
            current_proj_lines = []
            i += 1
            continue
            
        if current_proj_name:
            current_proj_lines.append(line)
        
        i += 1
        
    # Add last project
    if current_proj_name:
        extracted_projects[current_proj_name] = "\n".join(current_proj_lines)

    # Now parse extracted projects for dates
    for proj_name, content in extracted_projects.items():
        # Find start date
        # Content contains lines like "(cid:190) Project Schedule: ... (cid:131) Begin Construction: Fall 2023"
        
        # Normalize content
        content_lower = content.lower()
        
        start_date = None
        
        # Look for "Begin Construction: <Date>"
        match = re.search(r'begin construction[:\s]+([a-zA-Z0-9,\s]+)', content_lower)
        if match:
            start_date = match.group(1).split('\n')[0].strip()
        else:
            # Look for "Start: <Date>"
            match = re.search(r'start[:\s]+([a-zA-Z0-9,\s]+)', content_lower)
            if match:
                start_date = match.group(1).split('\n')[0].strip()
            else:
                 # Look for "Advertise: <Date>" (as a proxy if no construction start)
                match = re.search(r'advertise[:\s]+([a-zA-Z0-9,\s]+)', content_lower)
                if match:
                    start_date = match.group(1).split('\n')[0].strip()
        
        # If still no date found, check for "Spring 2022" mentioned in the text
        if not start_date:
            # If "Spring 2022" is in the text, we might want to consider it if it's relevant.
            # But the query asks for projects that "Started in Spring 2022".
            # If "Begin Construction: Spring 2022" exists, regex would catch it.
            # If "Advertise: Spring 2022", regex catches it.
            pass

        if start_date and is_spring_2022(start_date):
            projects.append({'Project_Name': proj_name, 'Start_Date': start_date, 'Source_Doc': doc['filename']})

# DataFrame of projects
df_projects = pd.DataFrame(projects)

# Join with funding
# We need to fuzzy match or exact match Project_Name
# Let's try exact match first after some normalization
def normalize(name):
    if not name: return ""
    return name.lower().strip()

df_projects['join_key'] = df_projects['Project_Name'].apply(normalize)
df_funding['join_key'] = df_funding['Project_Name'].apply(normalize)

merged = pd.merge(df_projects, df_funding, on='join_key', how='inner')

# Identify unmerged projects
unmerged = df_projects[~df_projects['join_key'].isin(df_funding['join_key'])]

print("__RESULT__:")
print(json.dumps({
    "projects_found": projects,
    "merged_count": len(merged),
    "total_funding": merged['Amount'].sum() if not merged.empty else 0,
    "project_names": merged['Project_Name_x'].tolist() if not merged.empty else [],
    "unmerged_names": unmerged['Project_Name'].tolist() if not unmerged.empty else []
}))"""

env_args = {'var_function-call-16904404130023659614': 'file_storage/function-call-16904404130023659614.json', 'var_function-call-16904404130023657657': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10631543890590275137': 'file_storage/function-call-10631543890590275137.json', 'var_function-call-10631543890590275884': 'file_storage/function-call-10631543890590275884.json'}

exec(code, env_args)

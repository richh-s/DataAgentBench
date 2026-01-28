code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-7811788439429183235'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
# Normalize funding amounts
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
    # Split by lines
    lines = text.split('\n')
    
    current_project = None
    current_info = {}
    
    # Heuristic: Iterate lines. 
    # If a line matches a funding project name (mostly), it's a project header.
    # Or if it precedes "Updates:" or "Project Description:".
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        # Check for Project Name candidates
        # A line is likely a project name if it is in our funding list
        # OR if the NEXT line contains "Updates:" or "Project Description:"
        is_project_start = False
        candidate_name = normalize(line_stripped)
        
        # Check next line for indicators
        next_line = ""
        if i + 1 < len(lines):
             next_line = lines[i+1].strip()
        
        if candidate_name in funding_project_names:
            is_project_start = True
        elif "Updates:" in next_line or "Project Description:" in next_line:
            is_project_start = True
            # Clean up artifacts if any
            candidate_name = candidate_name.replace("(cid:190)", "").strip()
            
        if is_project_start:
            # Save previous project
            if current_project:
                extracted_projects.append(current_info)
            
            current_project = candidate_name
            current_info = {
                'Project_Name': current_project,
                'raw_text': "",
                'dates': []
            }
        elif current_project:
            current_info['raw_text'] += " " + line_stripped
            # Check for dates
            # Patterns: "Begin Construction: ...", "Begin Design: ...", "Complete Construction: ..."
            # We look for lines containing "Begin" or "Start"
            if "Begin" in line_stripped or "Start" in line_stripped:
                current_info['dates'].append(line_stripped)

    # Append last project
    if current_project:
        extracted_projects.append(current_info)

# Now filter and process
results = []
disaster_keywords = ["FEMA", "CalOES", "CalJPIA"]

for p in extracted_projects:
    name = p['Project_Name']
    # Check type
    is_disaster = any(k in name for k in disaster_keywords)
    # Note: Type might also be inferred if I tracked headers, but let's stick to name suffixes first as per Hint.
    
    # Check start date
    # We look for "Begin ... 2022"
    started_2022 = False
    for d_str in p['dates']:
        # simplistic check: contains 2022
        if "2022" in d_str and ("Begin" in d_str or "Start" in d_str):
            started_2022 = True
    
    if is_disaster and started_2022:
        results.append(name)

# Remove duplicates (same project in multiple docs)
unique_results = list(set(results))

# Calculate funding
total_funding = 0
matched_projects = []
for name in unique_results:
    # Find in funding_df
    # Exact match might fail due to normalization. Try robust match.
    # We normalized funding names earlier.
    row = funding_df[funding_df['Project_Name'].apply(normalize) == normalize(name)]
    if not row.empty:
        amount = row.iloc[0]['Amount']
        total_funding += amount
        matched_projects.append({"name": name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects, "extracted_debug": results}))"""

env_args = {'var_function-call-7811788439429183235': 'file_storage/function-call-7811788439429183235.json', 'var_function-call-3690034761458033571': 'file_storage/function-call-3690034761458033571.json'}

exec(code, env_args)

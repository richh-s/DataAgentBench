code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-18248731954071622536'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-18328159169731343039'], 'r') as f:
    funding_data = json.load(f)

# Helper to identify if a line is a project header
def is_project_header(lines, i):
    # Heuristic: line i is a header if line i+1 or i+2 starts with "(cid:190)" or "Updates:"
    if i + 1 < len(lines):
        if "(cid:190)" in lines[i+1] or "Updates:" in lines[i+1] or "Project Description:" in lines[i+1]:
            return True
    if i + 2 < len(lines):
        if "(cid:190)" in lines[i+2] or "Updates:" in lines[i+2] or "Project Description:" in lines[i+2]:
            return True
    return False

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    current_project = None
    project_text_block = []
    
    for i, line in enumerate(lines):
        # Check if this line is a new project header
        if is_project_header(lines, i):
            # Save previous project if exists
            if current_project:
                projects.append({
                    'Project_Name': current_project,
                    'full_text': " ".join(project_text_block)
                })
            
            current_project = line
            project_text_block = []
        else:
            if current_project:
                project_text_block.append(line)
    
    # Append the last project
    if current_project:
        projects.append({
            'Project_Name': current_project,
            'full_text': " ".join(project_text_block)
        })

# Filter Projects
completed_park_projects_2022 = []

for p in projects:
    name = p['Project_Name']
    text = p['full_text'].lower()
    
    # Check for 'park' topic
    is_park = 'park' in name.lower() or 'park' in text
    
    # Check for completed in 2022
    # Look for patterns like "completed <month> 2022" or "complete construction: <month> 2022"
    # Actually, simpler: check if "completed" and "2022" appear near each other, or specific phrases.
    
    is_completed_2022 = False
    if 'completed' in text and '2022' in text:
        # Validate context
        # "Construction was completed November 2022"
        # "Construction was completed, November 2022"
        # "Complete Construction: November 2022"
        
        # Regex to be more specific
        # Match 'completed' followed by optional chars then '2022'
        if re.search(r'completed.*?2022', text) or re.search(r'complete construction.*?2022', text):
             is_completed_2022 = True
    
    # Also check if it says "completed January 2023" which would NOT be 2022.
    # The simple check might be prone to error if "2022" is mentioned elsewhere.
    # But let's stick to the specific phrases found in sample.
    
    if is_park and is_completed_2022:
        completed_park_projects_2022.append(name)

# Funding Data Frame
df_funding = pd.DataFrame(funding_data)

# Filter Funding
# We need to match names. The names extracted from text might correspond to Project_Name in Funding.
# Let's clean the extracted names (sometimes they have extra stuff?)
# But the Funding table names look clean. "Bluffs Park Shade Structure".
# Extracted name: "Bluffs Park Shade Structure". Matches.

# Find funding for these projects
total_funding = 0
matched_projects = []

for proj_name in completed_park_projects_2022:
    # Try exact match first
    match = df_funding[df_funding['Project_Name'] == proj_name]
    
    if match.empty:
        # Try fuzzy or partial match?
        # Maybe the extracted name has some noise.
        # Let's try to find if the extracted name is contained in the Funding DB or vice versa.
        # Actually, let's look at the funding table Project_Name that are IN our list.
        pass
    else:
        total_funding += match['Amount'].sum()
        matched_projects.append(proj_name)

print("__RESULT__:")
print(json.dumps({"total_funding": float(total_funding), "projects": matched_projects}))"""

env_args = {'var_function-call-17862480380810104238': 'file_storage/function-call-17862480380810104238.json', 'var_function-call-18328159169731343039': 'file_storage/function-call-18328159169731343039.json', 'var_function-call-18248731954071622536': 'file_storage/function-call-18248731954071622536.json'}

exec(code, env_args)

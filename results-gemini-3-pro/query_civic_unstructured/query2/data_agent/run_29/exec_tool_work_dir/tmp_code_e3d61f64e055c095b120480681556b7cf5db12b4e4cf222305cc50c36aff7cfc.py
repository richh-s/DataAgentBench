code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-18248731954071622536'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-18328159169731343039'], 'r') as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    current_project = None
    project_text_block = []
    
    for i, line in enumerate(lines):
        # Check markers
        is_marker = False
        if "Updates:" in line or "Project Description:" in line:
            is_marker = True
        elif "(cid:190)" in line: # This specific string might appear
             if "Updates:" in line or "Project Description:" in line:
                 is_marker = True
        
        if is_marker:
            # The previous line (ignoring the marker line itself) is likely the project name
            # We look at lines[i-1]
            if i > 0:
                potential_name = lines[i-1]
                # If the previous line was part of the previous project's block, we might have an issue.
                # But usually titles are distinct.
                # Also check if potential_name is not another marker or short garbage.
                
                # A better approach: 
                # If we hit a marker, we close the previous project and start a new one with the name from i-1.
                # BUT, we need to handle the content.
                # The content follows the marker.
                pass

    # Alternative parsing strategy:
    # 1. Find indices of all lines starting with "(cid:190)" or containing "Updates:"
    # 2. Treat the line BEFORE that index as the project name.
    # 3. The text BETWEEN the current marker and the next project name is the content.

    # Let's map project indices
    project_indices = []
    for i, line in enumerate(lines):
        if "(cid:190)" in line or "Updates:" in line or "Project Description:" in line:
            # But "Updates:" might be a sub-header.
            # The sample shows: "(cid:190) Updates:"
            # So let's rely on "(cid:190)" or the word "Updates:" at start.
            if line.startswith("(cid:190)") or line.startswith("Updates:"):
                # Potential start of a section for a project.
                # The project name is likely at i-1.
                project_name = lines[i-1]
                # Filter out if project_name looks like a page number or date
                if "Page" in project_name or "Agenda" in project_name:
                    continue
                project_indices.append(i-1)

    project_indices = sorted(list(set(project_indices)))
    
    for k in range(len(project_indices)):
        start_idx = project_indices[k]
        end_idx = project_indices[k+1] if k+1 < len(project_indices) else len(lines)
        
        p_name = lines[start_idx]
        p_text = " ".join(lines[start_idx+1:end_idx])
        projects.append({'Project_Name': p_name, 'full_text': p_text})

# Now filter
completed_park_projects = []
df_funding = pd.DataFrame(funding_data)
funding_names = set(df_funding['Project_Name'].unique())

for p in projects:
    name = p['Project_Name']
    text = p['full_text'].lower()
    
    # Topic Park
    # Check name and text
    is_park = "park" in name.lower() or "park" in text
    
    # Status Completed in 2022
    # Check for "completed ... 2022"
    # "Construction was completed November 2022"
    # "Construction was completed, November 2022"
    # "Complete Construction: ... 2022"
    
    is_2022 = False
    if "completed" in text and "2022" in text:
        # Check proximity or pattern
        if re.search(r'completed.{0,20}2022', text) or re.search(r'complete construction.{0,20}2022', text):
            is_2022 = True
    
    if is_park and is_2022:
        # Check against funding names for better matching
        # Sometimes extracted name has extra chars.
        # Clean name: remove trailing/leading non-alnum (except parens)
        clean_name = name.strip()
        
        # Try direct match
        if clean_name in funding_names:
             completed_park_projects.append(clean_name)
        else:
             # Try to find if the clean_name is contained in any funding name or vice-versa
             for fn in funding_names:
                 if clean_name == fn or clean_name in fn or fn in clean_name:
                     # Use the funding name
                     completed_park_projects.append(fn)
                     break

# Remove duplicates
completed_park_projects = list(set(completed_park_projects))

# Calculate total
total_amount = df_funding[df_funding['Project_Name'].isin(completed_park_projects)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"total_funding": float(total_amount), "projects": completed_park_projects}))"""

env_args = {'var_function-call-17862480380810104238': 'file_storage/function-call-17862480380810104238.json', 'var_function-call-18328159169731343039': 'file_storage/function-call-18328159169731343039.json', 'var_function-call-18248731954071622536': 'file_storage/function-call-18248731954071622536.json'}

exec(code, env_args)

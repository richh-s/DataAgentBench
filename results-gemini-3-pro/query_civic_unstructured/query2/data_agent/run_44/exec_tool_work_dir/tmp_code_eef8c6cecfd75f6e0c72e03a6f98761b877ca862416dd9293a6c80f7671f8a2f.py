code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2604806260123292981'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Helper to identify park projects
def is_park_project(name, text):
    # content = name + " " + text
    # Check for "park" or "playground" but avoid "parking"
    # Simple check:
    content = (name + " " + text).lower()
    if 'park' in content and 'parking' not in content:
        return True
    if 'playground' in content:
        return True
    # "Skate Park" -> park
    # "Bluffs Park" -> park
    return False

# Helper to check completion in 2022
def is_completed_2022(text):
    text_lower = text.lower()
    # Patterns seen: "Construction was completed November 2022", "Construction was completed, November 2022"
    # Also need to avoid "Complete Design: ... 2022" if that's not the project status.
    # The user asks for projects completed in 2022.
    
    # We look for "completed" and "2022" in the same sentence or line, 
    # and specifically exclude "design" if it's "complete design"
    
    # Let's split into lines
    lines = text_lower.split('\n')
    for line in lines:
        if 'completed' in line and '2022' in line:
            # Check for negative lookahead logic manually
            if 'design' in line:
                # e.g. "Complete Design: Summer 2022" -> This is NOT project completion.
                # But "Design completed in 2022" -> still Design phase.
                # "Project completed" or "Construction completed" is what we want.
                # If the line says "Construction was completed", we are good.
                if 'construction' in line:
                    return True
                else:
                    # Ambiguous. "Design completed" is not project completed.
                    pass
            else:
                # "Construction was completed, November 2022" -> No "design" word.
                # "Project completed..."
                return True
    return False

# Extraction logic
projects = []

for doc in civic_docs:
    text = doc['text']
    # Split by the marker for projects.
    # Pattern: Line, newlines, (cid:190)
    # We can iterate through lines and look for lines starting with (cid:190)
    lines = text.split('\n')
    
    # Find indices of lines starting with (cid:190) or containing it?
    # In the preview: "(cid:190) Updates:"
    # The Project Name is usually the line(s) before it, separated by empty lines.
    
    # Let's group lines into blocks.
    # A project starts with a Name (header) and continues until the next Name.
    # Names seem to be identifiable by being followed by a "(cid:190)" block.
    
    # Alternative: Use regex to split the text.
    # Pattern: \n([^\n]+)\n+\(cid:190\)
    # The group 1 is the project name.
    
    # Regex approach
    # We iterate over matches
    pattern = re.compile(r'\n+([^\n]+)\n+\(cid:190\)')
    
    # This might miss the first one if it's at start of file?
    # The text starts with "Public Works Commission..." and then lists projects.
    
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.end()
        
        # End index is the start of the next match or end of string
        if i < len(matches) - 1:
            end_index = matches[i+1].start()
        else:
            end_index = len(text)
            
        project_text = text[start_index:end_index]
        
        projects.append({
            'name': project_name,
            'text': project_text,
            'source': doc['filename']
        })

# Filter Projects
completed_park_projects = []
for p in projects:
    if is_park_project(p['name'], p['text']):
        if is_completed_2022(p['text']):
            completed_park_projects.append(p['name'])

# Deduplicate names
completed_park_projects = list(set(completed_park_projects))

print(f"Found {len(projects)} total projects extracted.")
print(f"Identified {len(completed_park_projects)} completed park projects in 2022: {completed_park_projects}")

# Join with Funding
# Funding Project_Name matches exactly?
# We'll try exact match first.
total_funding = 0
matched_projects = []

for name in completed_park_projects:
    # Try exact match
    record = funding_df[funding_df['Project_Name'] == name]
    if not record.empty:
        amount = record['Amount'].sum() # Sum in case of multiple entries (unlikely based on schema but possible)
        total_funding += amount
        matched_projects.append(name)
    else:
        # Try stripping or fuzzy? The hint says "matches".
        # Let's try matching with strip
        record = funding_df[funding_df['Project_Name'].str.strip() == name.strip()]
        if not record.empty:
            amount = record['Amount'].sum()
            total_funding += amount
            matched_projects.append(name)
        else:
             print(f"Could not find funding for: {name}")

print("__RESULT__:")
print(json.dumps({"total_funding": int(total_funding), "projects": matched_projects}))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json'}

exec(code, env_args)

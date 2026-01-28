code = """import json
import re

# Load the data
with open(locals()['var_function-call-11045079689153923464'], 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    # Normalize text to handle the cid characters
    text = text.replace('(cid:190)', '>').replace('(cid:131)', '-')
    
    # Split into lines
    lines = text.split('\n')
    
    current_project = {}
    buffer_project_name = None
    
    # Iterate to find project blocks
    # Heuristic: A line that is not empty, and the next line (skipping empty lines) starts with "> Updates:" or "> Project Description:" or "> Project Updates:"
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line or "Agenda Item" in line or "Page " in line:
            i += 1
            continue
            
        # Check if this line is a project title
        # Look ahead
        j = i + 1
        is_title = False
        while j < len(lines):
            next_line = lines[j].strip()
            if not next_line:
                j += 1
                continue
            if next_line.startswith('> Updates') or next_line.startswith('> Project Description') or next_line.startswith('> Project Updates'):
                is_title = True
            break
        
        if is_title:
            # Save previous project if exists
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'full_text': line,
                'st': None,
                'is_disaster': False
            }
            # Add following lines to full_text until next title
            i = j # Move to the Update line
        else:
            if current_project:
                current_project['full_text'] += "\n" + line
        
        i += 1
    
    # Add last project
    if current_project:
        projects.append(current_project)

# Analyze each project
parsed_projects = []
for p in projects:
    text = p['full_text']
    name = p['Project_Name']
    
    # Check for disaster
    is_disaster = False
    disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster', 'Emergency', 'Fire', 'Recovery', 'Woolsey']
    if any(k.lower() in text.lower() for k in disaster_keywords):
        is_disaster = True
        
    # Extract Start Date (st)
    # Look for "Begin Construction: <Date>"
    st = None
    begin_match = re.search(r'Begin [cC]onstruction:?\s*([A-Za-z0-9\s]+)', text)
    if begin_match:
        st = begin_match.group(1).strip()
    
    # Also check "Start Date:" if exists (not seen in example but possible)
    
    # Store
    parsed_projects.append({
        'Project_Name': name,
        'st': st,
        'is_disaster': is_disaster,
        'snippet': text[:200]
    })

print("__RESULT__:")
print(json.dumps(parsed_projects))"""

env_args = {'var_function-call-11045079689153923464': 'file_storage/function-call-11045079689153923464.json'}

exec(code, env_args)

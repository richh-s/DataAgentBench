code = """import json

# Load civic docs
with open(locals()['var_function-call-12716671968640832607'], 'r') as f:
    civic_docs = json.load(f)
text = civic_docs[0]['text']

# Load funding data
with open(locals()['var_function-call-12716671968640831510'], 'r') as f:
    funding_data = json.load(f)
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

lines = text.split('\n')

projects = []
current_project = None
buffer_text = []

# Marker usually starts the line or follows whitespace
# We check if line stripped starts with (cid:190) or \u00be
def is_marker(line):
    s = line.strip()
    return s.startswith('(cid:190)') or s.startswith('\u00be')

for i, line in enumerate(lines):
    if is_marker(line):
        # Check if it is a new project start
        # Usually followed by "Updates:" or "Project Description:"
        # Or "Project Updates:"
        s = line.strip()
        # Remove the marker to check content
        content = s.replace('(cid:190)', '').replace('\u00be', '').strip()
        
        # Heuristic: New project if header is 'Updates:' or 'Project Description:'
        # But 'Project Updates:' is also used.
        # And sometimes 'Updates' is used for existing project?
        # Let's look at the previous line.
        
        # Find previous non-empty line
        prev_idx = i - 1
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
            
        if prev_idx >= 0:
            potential_name = lines[prev_idx].strip()
            # Heuristics for a valid name:
            # - Not a marker line
            # - Not a page header "Agenda Item..."
            # - Not "Page X of Y"
            # - Not a generic header like "Capital Improvement Projects (Design)"
            
            is_new_project = True
            if is_marker(lines[prev_idx]): is_new_project = False
            if "Agenda Item" in potential_name: is_new_project = False
            if "Page " in potential_name and " of " in potential_name: is_new_project = False
            if "Capital Improvement Projects" in potential_name: is_new_project = False
            
            # If it's a new project, save the previous one
            if is_new_project:
                if current_project:
                    projects.append({'name': current_project, 'text': "\n".join(buffer_text)})
                
                current_project = potential_name
                buffer_text = []
    
    # Add line to buffer
    if current_project:
        buffer_text.append(line)

# Add last project
if current_project:
    projects.append({'name': current_project, 'text': "\n".join(buffer_text)})

# Filter and Sum
target_projects = []
total_funding = 0
keywords = ['park', 'playground']

for p in projects:
    name = p['name']
    details = p['text']
    
    # Check Topic
    if not any(k in name.lower() for k in keywords):
        continue
        
    # Check Status and Date (Completed in 2022)
    # Search for "completed" and "2022" in close proximity
    # Normalize text
    details_lower = details.lower()
    
    if "completed" in details_lower and "2022" in details_lower:
        # Verify the year 2022 is associated with "completed"
        # Extract phrases like "completed November 2022"
        # We'll split by sentences or just look at the line
        
        # Simple check: Is "2022" after "completed" and before "2023" or other years?
        # Or does "completed" line contain 2022?
        
        relevant_lines = [l for l in details.split('\n') if 'completed' in l.lower()]
        found = False
        for l in relevant_lines:
            if '2022' in l:
                # Exclude if it says "completed, January 2023" and 2022 is elsewhere?
                # But the line check handles proximity.
                # Check for negation "not completed"? Unlikely.
                found = True
                break
        
        if found:
            amount = funding_map.get(name, 0)
            target_projects.append({'name': name, 'amount': amount})
            total_funding += amount

print("__RESULT__:")
print(json.dumps({'target_projects': target_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-12716671968640832607': 'file_storage/function-call-12716671968640832607.json', 'var_function-call-12716671968640831510': 'file_storage/function-call-12716671968640831510.json'}

exec(code, env_args)

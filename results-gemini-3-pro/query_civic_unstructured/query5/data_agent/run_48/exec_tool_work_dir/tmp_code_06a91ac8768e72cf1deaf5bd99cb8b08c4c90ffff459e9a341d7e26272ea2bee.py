code = """import json
import re

file_path = locals()['var_function-call-11045079689153923464']
with open(file_path, 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    # Normalize
    text = text.replace('(cid:190)', '>').replace('(cid:131)', '-')
    
    lines = text.split('\n')
    current_project = {}
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty or irrelevant lines
        if not line or "Agenda Item" in line or "Page " in line:
            i += 1
            continue
            
        # Look ahead for "Updates" or "Project Description"
        j = i + 1
        is_title = False
        found_indicator = False
        
        while j < len(lines):
            next_line = lines[j].strip()
            if not next_line:
                j += 1
                continue
            if next_line.startswith('> Updates') or next_line.startswith('> Project Description') or next_line.startswith('> Project Updates'):
                is_title = True
            found_indicator = True # Found a non-empty line
            break
        
        # Check if current line is a header like "Capital Improvement Projects (Design)"
        # These are not projects themselves usually, but headers.
        # Projects seem to be below them.
        # However, the heuristic above (title followed by > Updates) works for projects.
        
        if is_title:
            if current_project:
                projects.append(current_project)
            current_project = {'Project_Name': line, 'full_text': line}
            i = j # Jump to the update line
        else:
            if current_project:
                current_project['full_text'] += "\n" + line
        i += 1
    
    if current_project:
        projects.append(current_project)

results = []
for p in projects:
    t = p['full_text']
    name = p['Project_Name']
    
    is_disaster = False
    disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster', 'Emergency', 'Fire', 'Recovery']
    if any(k.lower() in t.lower() for k in disaster_keywords):
        is_disaster = True
        
    st = None
    # Look for start dates
    # "Begin Construction: ..."
    m = re.search(r'Begin [cC]onstruction:?\s*([^\n]+)', t)
    if m:
        st = m.group(1).strip()
    
    results.append({'Project_Name': name, 'st': st, 'is_disaster': is_disaster})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11045079689153923464': 'file_storage/function-call-11045079689153923464.json'}

exec(code, env_args)

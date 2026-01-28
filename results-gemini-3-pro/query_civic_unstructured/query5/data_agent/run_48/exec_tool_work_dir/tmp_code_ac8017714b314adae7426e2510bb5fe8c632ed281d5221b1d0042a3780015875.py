code = """import json
import re

file_path = locals()['var_function-call-11045079689153923464']
with open(file_path, 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    last_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this line indicates the start of details for a project
        # e.g. "(cid:190) Updates:" or "Updates:"
        if "Updates:" in line or "Project Description:" in line:
            # The previous line was the project title
            if last_line and "Agenda Item" not in last_line:
                if current_project:
                    projects.append(current_project)
                current_project = {
                    'Project_Name': last_line,
                    'full_text': last_line + "\n" + line
                }
            else:
                # Could be a continuation or issue, just append to current if exists
                if current_project:
                    current_project['full_text'] += "\n" + line
        else:
            if current_project:
                current_project['full_text'] += "\n" + line
            last_line = line

    if current_project:
        projects.append(current_project)

results = []
for p in projects:
    t = p['full_text']
    name = p['Project_Name']
    
    is_disaster = False
    # Check for disaster keywords
    if "FEMA" in t or "CalOES" in t or "CalJPIA" in t or "Recovery" in t or "Fire" in t:
        is_disaster = True
        
    st = None
    # Check for "Begin Construction: <Date>"
    # Use simple string find or regex
    m = re.search(r"Begin [cC]onstruction:?\s*([^\n]+)", t)
    if m:
        st = m.group(1).strip()
    else:
        # Check "Construction was completed" - might indicate it started recently?
        # But question asks for "started in 2022".
        # If it completed in 2022, it might have started in 2022.
        # Let's extract completion date too just in case.
        m2 = re.search(r"Construction was completed,?\s*([^\n]+)", t)
        if m2:
            st = "Completed " + m2.group(1).strip()

    results.append({'Project_Name': name, 'st': st, 'is_disaster': is_disaster})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11045079689153923464': 'file_storage/function-call-11045079689153923464.json'}

exec(code, env_args)

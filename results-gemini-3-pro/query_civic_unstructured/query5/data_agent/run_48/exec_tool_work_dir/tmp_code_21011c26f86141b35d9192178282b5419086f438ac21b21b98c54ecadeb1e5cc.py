code = """import json
import re

file_path = locals()['var_function-call-11045079689153923464']
with open(file_path, 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    lines = text.split('\\n') 
    
    current_project = None
    last_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if "Updates:" in line or "Project Description:" in line:
            if last_line and "Agenda Item" not in last_line and "Page" not in last_line:
                if current_project:
                    projects.append(current_project)
                current_project = {
                    'Project_Name': last_line,
                    'full_text': last_line + " " + line
                }
            elif current_project:
                 current_project['full_text'] += " " + line
        else:
            if current_project:
                current_project['full_text'] += " " + line
            last_line = line

    if current_project:
        projects.append(current_project)

results = []
for p in projects:
    t = p['full_text']
    name = p['Project_Name']
    
    is_disaster = False
    if "FEMA" in t or "CalOES" in t or "CalJPIA" in t or "Recovery" in t or "Fire" in t:
        is_disaster = True
    
    st = None
    # Begin Construction
    m = re.search(r"Begin [cC]onstruction:?\s*([A-Za-z0-9\s]+)", t)
    if m:
        st = m.group(1).strip()
    
    # Check for "Construction was completed"
    if not st:
        m2 = re.search(r"Construction was completed,?\s*([A-Za-z0-9\s]+)", t)
        if m2:
            st = "Completed " + m2.group(1).strip()

    # Check for Start Date explicitly if needed.
    # Also "Advertise" date might be relevant? 
    # Usually "Start" means "Begin Construction" or "Start Date".
    
    # Also check if name has 2022
    if "2022" in name and not st:
        st = "2022 (in name)"

    results.append({'Project_Name': name, 'st': st, 'is_disaster': is_disaster})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11045079689153923464': 'file_storage/function-call-11045079689153923464.json'}

exec(code, env_args)

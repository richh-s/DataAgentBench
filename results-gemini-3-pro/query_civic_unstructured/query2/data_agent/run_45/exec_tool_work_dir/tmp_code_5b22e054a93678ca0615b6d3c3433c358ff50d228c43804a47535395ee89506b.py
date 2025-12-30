code = """import json
import re

# Load the data
file_path = locals()['var_function-call-18190371962378278332']
with open(file_path, 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    # Split lines
    lines = text.splitlines()
    
    current_name = None
    current_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Identify project start
        # Looking for "(cid:190) Updates:"
        if "(cid:190)" in line and "Updates" in line:
            # Name is likely in the lines before
            # Search backwards
            found_name = None
            for j in range(i-1, -1, -1):
                prev = lines[j].strip()
                if not prev: continue
                # Skip headers
                if "Page" in prev or "Agenda Item" in prev or "Capital Improvement" in prev or "Public Works" in prev:
                    continue
                # Assuming this is the name
                found_name = prev
                break
            
            if found_name:
                # Save previous
                if current_name:
                    projects.append({"name": current_name, "text": "\n".join(current_lines)})
                current_name = found_name
                current_lines = []
        
        if current_name:
            current_lines.append(line)
            
    if current_name:
        projects.append({"name": current_name, "text": "\n".join(current_lines)})

# Filter
matched = []
for p in projects:
    name = p['name'].strip()
    text = p['text'].lower()
    
    # 1. Park related
    if "park" in name.lower() or "playground" in name.lower():
        # 2. Completed in 2022
        # Check text
        # Look for "completed" and "2022"
        # Avoid "design" completion
        
        completed = False
        if "2022" in text:
            # Check context
            if "construction was completed" in text or "construction completed" in text:
                if "2022" in text:
                    # Simple check: is 2022 in the same snippet?
                    # Let's check lines
                    for l in text.splitlines():
                        if "2022" in l and ("construction was completed" in l or "construction completed" in l or "completed construction" in l):
                             completed = True
                        # Also "Completed: ... 2022"
                        if "2022" in l and l.strip().startswith("completed") and "design" not in l:
                             completed = True
                             
        if completed:
            matched.append(name)

print("__RESULT__:")
print(json.dumps(matched))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json'}

exec(code, env_args)

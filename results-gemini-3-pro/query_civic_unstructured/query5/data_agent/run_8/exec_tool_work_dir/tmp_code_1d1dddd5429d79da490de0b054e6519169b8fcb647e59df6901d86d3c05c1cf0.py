code = """import json
import re

# Load data
with open(locals()['var_function-call-5680067546526520620'], 'r') as f:
    civic_data = json.load(f)
    
with open(locals()['var_function-call-10418813875074106507'], 'r') as f:
    funding_data = json.load(f)

text = civic_data[0]['text']

# Base names from funding
base_names = set()
for r in funding_data:
    name = r['Project_Name']
    # Remove parens
    base = re.split(r'\s*\(', name)[0].strip()
    base_names.add(base)

lines = text.split('\n')
projects = []
current_project = None
current_section = ""
current_block = []

# Heuristic: Project name is a line that matches a base name from funding
# and is not a section header.

for line in lines:
    line = line.strip()
    if not line: continue
    
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
        current_section = line
        continue
        
    # Check if line matches a base name
    # We do case-insensitive match
    is_project = False
    for base in base_names:
        if line.lower() == base.lower():
            is_project = True
            matched_name = base
            break
    
    if is_project:
        # Save previous project
        if current_project:
            projects.append({
                "name": current_project,
                "section": current_section,
                "text": " ".join(current_block)
            })
        current_project = matched_name
        current_block = []
    else:
        if current_project:
            current_block.append(line)

# Add last
if current_project:
    projects.append({
        "name": current_project,
        "section": current_section,
        "text": " ".join(current_block)
    })

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json'}

exec(code, env_args)

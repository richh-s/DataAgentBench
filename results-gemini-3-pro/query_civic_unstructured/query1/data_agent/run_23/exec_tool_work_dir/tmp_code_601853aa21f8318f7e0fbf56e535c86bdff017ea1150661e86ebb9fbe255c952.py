code = """import json
import re

# Load funding data
with open(locals()['var_function_call_14956260562366733902'], 'r') as f:
    funding_data = json.load(f)

# Filter funding data
funded_projects = {}
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        continue

# Load civic docs
with open(locals()['var_function_call_4179271317217180395'], 'r') as f:
    docs = json.load(f)

design_capital_projects = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Markers for sections
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
        
        # Stop if we hit other sections
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            in_design_section = False
            continue
            
        if in_design_section:
            # Heuristic to identify project names vs details
            # Exclude lines with "Updates:", "Schedule:", "Page X", "Agenda Item"
            if "Updates:" in line or "Schedule:" in line or "Page " in line or "Agenda Item" in line:
                continue
            
            # Exclude lines starting with (cid:...) or similar bullets
            # The preview showed (cid:190) which often decodes to a bullet or similar.
            # We can exclude lines starting with parentheses '('
            if line.startswith('('):
                continue
                
            # Exclude lines that look like a date or part of a sentence
            if line.lower().startswith('prepared by') or line.lower().startswith('approved by'):
                continue

            # It's likely a project name
            design_capital_projects.add(line)

# Match
count = 0
matches = []
# Normalize matching
funded_names = set(funded_projects.keys())

for proj in design_capital_projects:
    if proj in funded_names:
        count += 1
        matches.append(proj)
    else:
        # Try simple cleaning?
        # Maybe the funding name has (FEMA Project) but the text doesn't?
        # Or vice versa?
        # The prompt says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted from the civic documents."
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "extracted": list(design_capital_projects)}))"""

env_args = {'var_function-call-14956260562366733902': 'file_storage/function-call-14956260562366733902.json', 'var_function-call-4179271317217180395': 'file_storage/function-call-4179271317217180395.json'}

exec(code, env_args)

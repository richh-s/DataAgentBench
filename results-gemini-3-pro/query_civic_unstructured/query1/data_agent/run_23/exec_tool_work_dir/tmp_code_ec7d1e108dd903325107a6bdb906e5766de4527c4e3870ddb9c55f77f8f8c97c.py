code = """import json
import re

# Load funding data
with open(var_function_call_14956260562366733902, 'r') as f:
    funding_data = json.load(f)

# Filter funding data
# Amount is string in JSON, convert to int/float
funded_projects = {}
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        continue

# Load civic docs
with open(var_function_call_4179271317217180395, 'r') as f:
    docs = json.load(f)

design_capital_projects = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_capital_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        # Use simple string matching or regex for robustness against casing/whitespace
        if "Capital Improvement Projects (Design)" in line:
            in_capital_design_section = True
            continue
        elif "Capital Improvement Projects" in line and "(Design)" not in line:
            # Entering another section like (Construction) or (Not Started)
            in_capital_design_section = False
            continue
        elif "Disaster Recovery Projects" in line:
            in_capital_design_section = False
            continue

        if in_capital_design_section:
            # identifying project names
            # Filter out lines that are clearly not project names
            if line.startswith('(') or line.startswith('Page ') or line.startswith('Agenda Item'):
                continue
            if "Updates:" in line or "Project Schedule:" in line or "Estimated Schedule:" in line or "Prepared by:" in line or "Approved by:" in line or "Subject:" in line:
                continue
            if "Complete Design:" in line or "Advertise:" in line or "Begin Construction:" in line:
                continue
            
            # Use regex to skip lines starting with special bullets often found in PDF text extraction
            # The preview shows (cid:190) which is unicode.
            # Let's filter out lines starting with non-alphanumeric if possible, but project names might start with numbers "2022 Morning..."
            # Project names usually look like title strings.
            
            # Simple heuristic: If it passes above filters, treat as potential project name.
            # Clean the name
            name = line.strip()
            if len(name) < 3: # Skip very short lines
                continue
            
            design_capital_projects.add(name)

# Find intersection
count = 0
matches = []
for proj in design_capital_projects:
    # Try exact match first
    if proj in funded_projects:
        count += 1
        matches.append(proj)
    else:
        # The prompt hints: "The Project_Name ... matches the project names that can be extracted"
        # But extracted text might have artifacts.
        # Let's check for "almost" matches or substring? 
        # The hint says "matches", implying exact or very close.
        # Let's just print the projects I found to debug if needed.
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "extracted_design_projects": list(design_capital_projects)}))"""

env_args = {'var_function-call-14956260562366733902': 'file_storage/function-call-14956260562366733902.json', 'var_function-call-4179271317217180395': 'file_storage/function-call-4179271317217180395.json'}

exec(code, env_args)

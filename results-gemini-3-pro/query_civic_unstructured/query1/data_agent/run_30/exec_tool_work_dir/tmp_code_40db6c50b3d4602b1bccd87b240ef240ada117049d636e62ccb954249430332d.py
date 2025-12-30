code = """import json

# Load funding data
with open(locals()['var_function-call-3513875169581502759'], 'r') as f:
    funding_data = json.load(f)

# Aggregate funding by Project_Name
funding_map = {}
for record in funding_data:
    name = record['Project_Name'].strip()
    amount = float(record['Amount'])
    if name not in funding_map:
        funding_map[name] = 0.0
    funding_map[name] += amount

# Load civic docs
with open(locals()['var_function-call-3513875169581504334'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check sections
        if "Capital Improvement Projects (Design)" in line:
            current_section = "DESIGN"
            i += 1
            continue
        
        # Stop if we hit another section
        # Common next sections based on preview
        if "Capital Improvement Projects (Construction)" in line:
            current_section = None
        if "Capital Improvement Projects (Not Started)" in line:
            current_section = None
        if "Disaster Recovery Projects" in line:
            # Could be a main header or sub header. 
            # If we are in DESIGN, and this appears, it might be switching context.
            # But the prompt implies Capital vs Disaster are Types.
            # If the header is "Disaster Recovery Projects Status Report", it's the main title.
            # If "Capital Improvement Projects (Design)" was a subheader, we are good.
            # If we see a new main header, stop.
            pass
            
        if current_section == "DESIGN":
            # Extract Project Name
            # Criteria:
            # 1. Not empty
            # 2. Doesn't start with typical metadata markers
            # 3. Followed closely by an 'Updates' or 'Description' bullet
            
            if not line:
                i += 1
                continue
            
            # Skip page headers/footers/bullets
            if line.startswith("Page ") or "Agenda Item" in line:
                i += 1
                continue
            if "(cid:" in line: # Bullet point line
                i += 1
                continue
            if "Updates:" in line or "Project Schedule:" in line:
                i += 1
                continue
                
            # Peek ahead for confirmation
            # We look for a line containing "(cid:" and ("Updates" or "Description" or "Project")
            is_valid_project = False
            for offset in range(1, 6):
                if i + offset >= len(lines):
                    break
                next_l = lines[i + offset].strip()
                if not next_l:
                    continue
                if "(cid:" in next_l:
                    # Found a bullet. Check if it's a project detail bullet.
                    if "Updates" in next_l or "Description" in next_l or "Project" in next_l or "Schedule" in next_l:
                        is_valid_project = True
                    break # Stop at first bullet
                else:
                    # Found another text line. 
                    # If it's a metadata line (Agenda Item), skip it and keep looking?
                    if "Agenda Item" in next_l or "Page " in next_l:
                        continue
                    # If it looks like another project name, then the current one wasn't a project (or missing details).
                    # Actually, some projects might not have details? But usually they do in these reports.
                    # Let's assume strict structure.
                    break
            
            if is_valid_project:
                capital_design_projects.add(line)
                
        i += 1

# Calculate answer
count = 0
matches = []

# Debug list
debug_unmatched = []

for proj in capital_design_projects:
    if proj in funding_map:
        if funding_map[proj] > 50000:
            count += 1
            matches.append(proj)
    else:
        debug_unmatched.append(proj)

print("__RESULT__:")
print(json.dumps({
    "count": count, 
    "extracted_projects": list(capital_design_projects),
    "matches": matches,
    "unmatched": debug_unmatched
}))"""

env_args = {'var_function-call-3513875169581502759': 'file_storage/function-call-3513875169581502759.json', 'var_function-call-3513875169581504334': 'file_storage/function-call-3513875169581504334.json'}

exec(code, env_args)

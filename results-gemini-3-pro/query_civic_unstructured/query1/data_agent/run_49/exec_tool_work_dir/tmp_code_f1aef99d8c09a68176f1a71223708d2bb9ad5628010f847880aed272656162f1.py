code = """import json

# Load funding results
funding_file = locals()['var_function-call-12998690230637064644']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

funded_projects = set()
for row in funding_data:
    if row.get('Project_Name'):
        funded_projects.add(row['Project_Name'].strip())

# Load civic docs
docs_file = locals()['var_function-call-12998690230637064277']
with open(docs_file, 'r') as f:
    docs_data = json.load(f)

design_projects = set()

for doc in docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    
    in_design_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect start of section
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            i += 1
            continue
            
        # Detect end of section
        if in_design_section:
            # Check if we hit another header
            # Headers seem to start with Capital Improvement Projects or Disaster Recovery
            if "Capital Improvement Projects (" in line and "(Design)" not in line:
                in_design_section = False
                break # Move to next doc or just stop if we assume structure
            if "Disaster Recovery Projects" in line:
                in_design_section = False
                break
                
            # Extract project name
            # Heuristic: A non-empty line followed eventually by "Updates:" or "(cid:190)" lines
            if line:
                # Look ahead a few lines for cues
                is_project = False
                for k in range(1, 6):
                    if i + k < len(lines):
                        next_line = lines[i+k].strip()
                        if "Updates:" in next_line or "Project Description:" in next_line or "(cid:190)" in next_line:
                            is_project = True
                            break
                        # If we hit another potential project name (unlikely to have 2 names in a row without updates), maybe stop?
                        # But empty lines exist.
                
                if is_project:
                    # Filter out some common headers that might be mistaken
                    if "Page" not in line and "Agenda" not in line and "Item" not in line:
                        design_projects.add(line)
        
        i += 1

# Intersect
matching_projects = []
for dp in design_projects:
    if dp in funded_projects:
        matching_projects.append(dp)
    else:
        # Try simple cleaning?
        # Maybe " (FEMA Project)" suffix mismatch?
        # But we want strict matching if possible.
        pass

print("__RESULT__:")
print(json.dumps({
    "design_projects_found": list(design_projects),
    "matching_projects": matching_projects,
    "count": len(matching_projects)
}))"""

env_args = {'var_function-call-12998690230637064644': 'file_storage/function-call-12998690230637064644.json', 'var_function-call-12998690230637064277': 'file_storage/function-call-12998690230637064277.json'}

exec(code, env_args)

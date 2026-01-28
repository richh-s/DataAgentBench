code = """import json
import re

# Load funding data
with open(locals()['var_function-call-3513875169581502759'], 'r') as f:
    funding_data = json.load(f)

# Create a lookup for funding. Handle potential duplicates or just take the first one?
# The prompt implies unique projects or just joining.
# Let's normalize names to lower case and stripped for joining.
funding_map = {}
for record in funding_data:
    name = record['Project_Name'].strip()
    amount = float(record['Amount'])
    # In case of duplicates, maybe sum? Or duplicate rows? 
    # Usually "Funding" table implies sources. A project might have multiple funding sources.
    # The prompt says "Fields: Funding_ID, Project_Name, Funding_Source, Amount".
    # So a project can have multiple entries. The question asks if the project has "funding greater than $50,000".
    # This implies TOTAL funding for the project? Or *a* funding record > 50k?
    # "How many capital projects ... have funding greater than $50,000?"
    # Usually implies total funding. I'll sum it up.
    if name not in funding_map:
        funding_map[name] = 0
    funding_map[name] += amount

# Load civic docs
with open(locals()['var_function-call-3513875169581504334'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

# Helper to clean lines
def clean_line(line):
    return line.strip()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    
    # Iterate lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect Section Headers
        # Note: The text might have "Capital Improvement Projects (Design)" spread or formatted.
        # Based on preview: "Capital Improvement Projects (Design)" is on its own line.
        if "Capital Improvement Projects (Design)" in line:
            current_section = "CAPITAL_DESIGN"
            i += 1
            continue
        elif "Capital Improvement Projects (Construction)" in line or \
             "Capital Improvement Projects (Not Started)" in line or \
             "Disaster Recovery Projects" in line:
            current_section = None
            i += 1
            continue
            
        if current_section == "CAPITAL_DESIGN":
            # Heuristics to find project name
            # 1. Not empty
            # 2. Doesn't start with (cid:190) or (cid:131) or similar garbage
            # 3. Not a page number or footer
            if not line:
                i += 1
                continue
                
            # Skip noise lines
            if line.startswith('(cid:') or line.startswith('Page ') or line.startswith('Agenda Item'):
                i += 1
                continue
            
            # Skip likely header repetitions or other metadata
            if "updates:" in line.lower() or "project schedule:" in line.lower():
                i += 1
                continue

            # Potential Project Name
            # Usually followed by "(cid:190) Updates:" or "(cid:190) Project Description:" or "(cid:190) Project Updates:" in the next few lines
            # Let's peek ahead to confirm
            is_project = False
            for k in range(1, 5): # Look ahead 4 lines
                if i + k < len(lines):
                    next_line = lines[i+k].strip()
                    if "(cid:190)" in next_line and ("Updates" in next_line or "Description" in next_line or "Project" in next_line):
                        is_project = True
                        break
                    if not next_line: # Skip empty lines looking for the bullet
                        continue
                    # If we hit another text line before the bullet, maybe the current line is just garbage?
                    # Or maybe the project name is multi-line? (Simplification: assume single line names)
                    if len(next_line) > 0 and not next_line.startswith("(cid:"):
                         # Found another text line before bullet. Maybe this line wasn't a project.
                         break
            
            if is_project:
                capital_design_projects.add(line)
        
        i += 1

# Join and Count
count = 0
matching_projects = []

# Normalize for joining
# funding_map keys are original names. 
# We need to fuzzy match or exact match?
# SQLite names: "Birdview Avenue Improvements"
# Extracted names: "Birdview Avenue Improvements" (likely)
# Let's try exact match first (stripped)

print("Extracted Capital Design Projects:", list(capital_design_projects))

for proj in capital_design_projects:
    # Try exact match
    if proj in funding_map:
        total_funding = funding_map[proj]
        if total_funding > 50000:
            count += 1
            matching_projects.append((proj, total_funding))
    else:
        # Try finding it in funding map (maybe partial match?)
        # For strictness, I'll stick to exact match first.
        # But let's check if there are minor discrepancies (like suffixes)
        # The prompt says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted..."
        # So exact match (after strip) should work.
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matching_projects, "extracted_count": len(capital_design_projects)}))"""

env_args = {'var_function-call-3513875169581502759': 'file_storage/function-call-3513875169581502759.json', 'var_function-call-3513875169581504334': 'file_storage/function-call-3513875169581504334.json'}

exec(code, env_args)

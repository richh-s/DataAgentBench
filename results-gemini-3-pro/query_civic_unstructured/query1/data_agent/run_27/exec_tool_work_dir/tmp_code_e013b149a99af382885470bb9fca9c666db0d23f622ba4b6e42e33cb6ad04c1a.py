code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-6706861510607389059'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-4954927585096532442'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding data for Amount > 50,000
# Note: Amount in JSON is string, need to convert to int/float
funded_projects = []
for record in funding_data:
    try:
        if float(record['Amount']) > 50000:
            funded_projects.append(record['Project_Name'])
    except ValueError:
        pass

funded_projects_set = set(funded_projects)

# extract projects from text
design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    # We are looking for "Capital Improvement Projects (Design)"
    # The text might contain other sections like "Capital Improvement Projects (Construction)"
    
    # Iterate through lines to find the section and projects
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        if "Capital Improvement Projects (Design)" in line:
            current_section = "Capital_Design"
            i += 1
            continue
        elif "Capital Improvement Projects" in line and "Design" not in line:
            # e.g. Construction or Not Started
            current_section = None
        elif "Disaster Recovery Projects" in line:
            current_section = None
            
        if current_section == "Capital_Design":
            # Potential project name
            # Heuristic: A project name is usually followed by a line starting with (cid:190) or similar bullet
            # Or the project name might be multiple lines? 
            # In the preview:
            # "2022 Morning View Resurfacing & Storm Drain Improvements"
            # "(cid:190) Updates:"
            
            # So if line[i] is the name, line[i+1] might be empty or contain the bullet.
            # Let's look ahead.
            
            if not line: # skip empty lines
                i += 1
                continue
                
            # Check if this line is likely a project name
            # It shouldn't be a bullet point itself
            if line.startswith("(cid") or line.startswith("Updates:") or line.startswith("Project Schedule:"):
                i += 1
                continue
            
            # Look ahead for confirmation (the update block)
            is_project = False
            for offset in range(1, 5): # check next few lines
                if i + offset < len(lines):
                    next_line = lines[i+offset].strip()
                    if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                        is_project = True
                        break
                    if next_line and not (next_line.startswith("(cid") or "Updates" in next_line):
                         # If we hit another text line that looks like a start of something else before the update bullet, 
                         # maybe the current line is just garbage or part of previous?
                         # But wait, sometimes project name spans two lines?
                         pass
            
            if is_project:
                # Clean up the project name
                p_name = line
                # check if next line is also part of name (if it's not the update line)
                # In the preview, names are single lines. 
                # "2022 Morning View Resurfacing & Storm Drain Improvements"
                
                # Add to set
                design_projects.add(p_name)
                
        i += 1

# Now we have a set of project names from the docs that are Capital & Design.
# We also have a set of funded projects > 50k.
# Find intersection.

# We need to match names. The names might not be identical (case, whitespace).
# Let's normalize both sets.
def normalize(s):
    return s.strip().lower()

design_projects_norm = {normalize(p): p for p in design_projects}
funded_projects_norm = {normalize(p) for p in funded_projects}

# Intersection
matches = []
for dp_norm, dp_orig in design_projects_norm.items():
    if dp_norm in funded_projects_norm:
        matches.append(dp_orig)

count = len(matches)

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "matches": matches,
    "design_projects_found": list(design_projects),
    "funded_projects_preview": list(funded_projects)[:10]
}))"""

env_args = {'var_function-call-6706861510607389059': 'file_storage/function-call-6706861510607389059.json', 'var_function-call-4954927585096532442': 'file_storage/function-call-4954927585096532442.json'}

exec(code, env_args)

code = """import json

# Load data
with open(locals()['var_function-call-13773859182325991137']) as f:
    sqlite_projects = json.load(f)

with open(locals()['var_function-call-15526337120589505523']) as f:
    mongo_docs = json.load(f)

# Extract SQLite names > 50k
# We'll use a set for faster lookup, but also need to handle fuzzy matching
funded_names = set(p['Project_Name'] for p in sqlite_projects)

design_projects_text = []

for doc in mongo_docs:
    text = doc['text']
    # Find start of Design section
    start_idx = text.find("Capital Improvement Projects (Design)")
    if start_idx == -1:
        continue
    
    # Find end of Design section
    # Possible next sections based on preview
    next_sections = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
    end_idx = len(text)
    for ns in next_sections:
        idx = text.find(ns, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    
    # Parse projects
    lines = section_text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        # Skip headers and metadata
        if "Capital Improvement Projects" in line: continue
        if line.startswith("Page"): continue
        if line.startswith("Agenda Item"): continue
        if line.startswith("(cid"): continue # Bullet points
        if line.startswith("Updates:"): continue
        if line.startswith("Project Schedule"): continue
        if line.startswith("Estimated Schedule"): continue
        
        # Heuristic: A project name line is followed (eventually) by a bullet point line like (cid:190) Updates:
        # We look ahead a few lines
        is_project = False
        for j in range(i+1, min(i+5, len(lines))):
            next_line = lines[j].strip()
            if not next_line: continue
            if next_line.startswith("(cid") or "Updates" in next_line or "Project Description" in next_line:
                is_project = True
                break
            # If we hit another likely project name (text line) before an update, then the current line might not be a project name?
            # Or maybe the structure is strict.
            # In the preview:
            # "2022 Morning View..."
            # "(cid:190) Updates:"
            # So looking for the bullet/Update immediately or after empty lines is good.
            if not (next_line.startswith("(cid") or "Updates" in next_line):
                # Found another text line. Maybe the project name spans two lines? 
                # Or it's garbage. 
                # Let's assume one line names for now.
                pass
        
        if is_project:
            # Clean up the name
            # Remove leading/trailing
            clean_name = line.strip()
            if clean_name not in design_projects_text:
                design_projects_text.append(clean_name)

# Matching
matched_projects = set()

# Normalize
# We want to match `design_name` to `funded_name`
# If design_name is "Westward Beach Road Repair Project"
# and funded_name is "Westward Beach Road Drainage Improvements Project"
# Containment might fail.
# But let's look at the extracted list first.

print("DEBUG: Extracted Design Projects:", design_projects_text)

count = 0
for d_proj in design_projects_text:
    d_norm = d_proj.lower().strip()
    match_found = False
    for f_proj in funded_names:
        f_norm = f_proj.lower().strip()
        
        # Check exact match
        if d_norm == f_norm:
            match_found = True
        # Check containment
        elif d_norm in f_norm or f_norm in d_norm:
            match_found = True
        
        if match_found:
            # print(f"Match found: '{d_proj}' matches '{f_proj}'")
            break
    if match_found:
        count += 1
        matched_projects.add(d_proj)

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-13773859182325991137': 'file_storage/function-call-13773859182325991137.json', 'var_function-call-13773859182325990970': 'file_storage/function-call-13773859182325990970.json', 'var_function-call-15526337120589505523': 'file_storage/function-call-15526337120589505523.json'}

exec(code, env_args)

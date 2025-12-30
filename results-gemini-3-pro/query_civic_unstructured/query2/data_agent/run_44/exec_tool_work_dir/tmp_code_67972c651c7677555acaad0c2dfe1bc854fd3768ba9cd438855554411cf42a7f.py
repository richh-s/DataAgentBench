code = """import json
import pandas as pd

with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2604806260123292981'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

projects = []
current_project = None
buffer_text = []
last_non_empty_line = ""

# Process each document
for doc in civic_docs:
    lines = doc['text'].splitlines()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check for marker (cid:190)
        # We can also check for "Updates:" if (cid:190) is stripped or encoding issue
        # The preview showed (cid:190) which is unicode \u00be (fraction 3/4) often? 
        # Or just the string "(cid:190)"?
        # The preview output string literal "(cid:190)".
        if "(cid:190)" in line or "Updates:" in line:
            # Check if this line actually starts a block (heuristic)
            # If "Updates:" is present, it's likely a marker.
            # But "Updates:" might appear in text.
            # The combination with (cid:190) is strong.
            # Or if line starts with "(cid:190)"
            is_marker = False
            if "(cid:190)" in line:
                is_marker = True
            elif line.strip().startswith("Updates:"):
                is_marker = True
            
            if is_marker:
                # If we were building a project, save it
                # But wait, if we are already in a project, 
                # does this marker start a NEW project or is it a subsection?
                # The preview shows each project has ONE "(cid:190) Updates:" or similar.
                # Sub-bullets use (cid:131).
                # So (cid:190) is the main bullet for project sections.
                # However, a project might have multiple (cid:190) sections?
                # "Updates", "Project Schedule", "Project Description".
                # Look at preview:
                # "PCH Median ... (cid:190) Updates: ... (cid:190) Project Schedule:"
                # So a project has multiple markers.
                
                # We need to detect when a NEW project starts.
                # A new project starts when we see a Title (which we only know is a title when we see the first marker).
                # If we are already in a project, and we see a marker, is it a new project?
                # No, it could be "Project Schedule".
                
                # Heuristic: A new project starts if the line BEFORE the marker is a Title.
                # Titles are usually not "Updates:" or "Project Schedule:".
                # But `last_non_empty_line` tracks the line before.
                # If `last_non_empty_line` was "Project Schedule", then this marker is just a section.
                # If `last_non_empty_line` is "Bluffs Park Shade Structure", it is a title.
                
                # So we verify `last_non_empty_line` against known section headers?
                # Known section headers: "Updates:", "Project Schedule:", "Project Description:", "Estimated Schedule:", "Complete Construction:", "Complete Design:".
                
                # If `last_non_empty_line` ends with ":", it's likely a header/label, not a project title?
                # Projects don't end with ":".
                
                if last_non_empty_line.strip().endswith(":"):
                    # Likely a continuation of the same project (e.g. previous line was a label)
                    # Or the marker line itself is just a bullet point.
                    if current_project:
                        buffer_text.append(line)
                    # Not a new project
                else:
                    # Likely a new project!
                    # Save old
                    if current_project:
                        current_project['text'] = "\n".join(buffer_text)
                        projects.append(current_project)
                    
                    # Start new
                    current_project = {'name': last_non_empty_line, 'text': ""}
                    buffer_text = [line]
            else:
                if current_project:
                    buffer_text.append(line)
        else:
            if current_project:
                buffer_text.append(line)
            last_non_empty_line = stripped

    # Save last
    if current_project:
        current_project['text'] = "\n".join(buffer_text)
        projects.append(current_project)
        current_project = None
        buffer_text = []

# Now extract
completed_parks = []
for p in projects:
    name = p['name']
    text = p['text'].lower()
    full_text = (name + " " + p['text']).lower()
    
    # Topic
    is_park = False
    if 'park' in full_text and 'parking' not in full_text:
        is_park = True
    if 'playground' in full_text:
        is_park = True
        
    # Completed 2022
    is_comp_2022 = False
    # Check for "completed" and "2022"
    # Logic: Look for lines with "completed" and "2022".
    # Exclude if line has "design" (unless it also has construction)
    
    # Split text into sentences or lines
    # Using lines from original text might be better but we joined them.
    # Split by newline
    p_lines = p['text'].split('\n')
    for line in p_lines:
        l_lower = line.lower()
        if 'completed' in l_lower and '2022' in l_lower:
            # Check context
            # "Construction was completed" -> Good
            # "Design completed" -> Bad (unless query allows design completion? No, usually 'projects completed' means construction)
            # "Project completed" -> Good
            if 'design' in l_lower and 'construction' not in l_lower:
                continue # Skip "Design completed"
            
            # Check for "Notice of completion filed January 2023" - this line has completion and 2023.
            # What if line says "Construction completed Nov 2022. Notice filed Jan 2023"?
            # If "2022" is in the line, it matches.
            is_comp_2022 = True
            break
            
    if is_park and is_comp_2022:
        completed_parks.append(name)

completed_parks = list(set(completed_parks))

# Match funding
total = 0
found_projects = []

for name in completed_parks:
    # Clean name: remove special chars?
    # Name from `last_non_empty_line` might be clean.
    clean_name = name.strip()
    
    # Exact match
    match = funding_df[funding_df['Project_Name'].str.strip() == clean_name]
    if match.empty:
        # Try case insensitive
        match = funding_df[funding_df['Project_Name'].str.strip().str.lower() == clean_name.lower()]
    
    if not match.empty:
        total += match['Amount'].sum()
        found_projects.append(clean_name)

print("__RESULT__:")
print(json.dumps({"total_funding": int(total), "projects": found_projects}))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json'}

exec(code, env_args)

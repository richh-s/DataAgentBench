code = """import json
import re

# Load data
funding_path = locals()['var_function-call-18362202212542543188']
civic_path = locals()['var_function-call-18362202212542543219']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f) # List of docs

# Parse civic docs
projects_info = []

def get_section(line, current_section):
    line = line.strip()
    if "Capital Improvement Projects (Design)" in line:
        return "Design"
    if "Capital Improvement Projects (Construction)" in line:
        return "Construction"
    if "Capital Improvement Projects (Not Started)" in line:
        return "Not Started"
    if "Disaster Recovery Projects" in line:
        return "Disaster"
    return current_section

for doc in civic_data:
    text = doc['text']
    # Normalize text
    text = text.replace('\r\n', '\n')
    
    # Split by the update marker to isolate projects
    # Marker: (cid:190) Updates: or just (cid:190)
    # The text uses (cid:190) for bullets like "Updates:", "Project Schedule:", "Project Description:"
    # A new project starts after the previous one ends.
    
    # Heuristic: Split by "\n\n" and look for blocks.
    # But names are often just lines.
    
    # Better approach: Iterate lines.
    lines = text.split('\n')
    current_section = "Unknown"
    
    current_project_name = None
    current_project_text = []
    
    # We need to buffer lines to identify the name.
    # A name is a non-empty line that is not a bullet and not a header, 
    # and is followed (eventually) by a bullet line starting with (cid:190).
    
    # Let's group lines into blocks separated by blank lines? No, sometimes single newlines.
    
    # Let's try to find lines that look like Project Names.
    # Characteristics:
    # - Not a header (checked via known headers).
    # - Not a bullet (doesn't start with (cid:190) or (cid:131)).
    # - Not "Page X of Y".
    # - Not "Agenda Item".
    # - Followed by "(cid:190)" lines.
    
    # First pass: Identify section ranges?
    # No, just iterate.
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check section
        new_section = get_section(line, current_section)
        if new_section != current_section:
            current_section = new_section
            # If we were building a project, save it?
            # A section header usually appears between projects.
            if current_project_name:
                projects_info.append({
                    "name": current_project_name,
                    "section": current_section, # Note: this logic might assign the *new* section to the *old* project if not careful.
                    # Actually, the section header applies to subsequent projects.
                    # So the previous project belongs to the old section.
                    # But here I updated current_section immediately.
                    # Let's fix: the previous project is done.
                    "text": "\n".join(current_project_text),
                    # "status_section": old_section # Need to track.
                })
                # Fix later.
                current_project_name = None
                current_project_text = []
            continue

        # Check if it's a bullet
        if line.startswith("(cid:190)") or line.startswith("(cid:131)") or line.startswith("Updates:") or line.startswith("Project Schedule:"):
            # This is part of the current project
            if current_project_name:
                current_project_text.append(line)
            continue
            
        # Check junk
        if "Page" in line and "of" in line: continue
        if "Agenda Item" in line: continue
        if "Prepared by:" in line: continue
        if "Approved by:" in line: continue
        if "Date prepared:" in line: continue
        if "Subject:" in line: continue
        if "RECOMMENDED ACTION:" in line: continue
        if "DISCUSSION:" in line: continue
        
        # If it's none of the above, it MIGHT be a project name.
        # But it could be just text description.
        # A project name is usually followed immediately by "(cid:190) Updates:" or "(cid:190) Project Description:"
        # Let's check the next few non-empty lines.
        
        is_name = False
        # Look ahead
        for j in range(i + 1, min(i + 5, len(lines))):
            next_l = lines[j].strip()
            if not next_l: continue
            if next_l.startswith("(cid:190)"):
                is_name = True
                break
            else:
                # If we hit another text line before a bullet, the current line is probably not a name 
                # (unless it's a multi-line name, which we can concatenate).
                # But looking at the sample: names are single lines.
                # "2022 Morning View ...\n\n(cid:190) Updates:"
                # So if next non-empty is (cid:190), it's a name.
                pass
                break # Stop at first non-empty
        
        if is_name:
            # Save previous project
            if current_project_name:
                projects_info.append({
                    "name": current_project_name,
                    "section": current_section, # This is the section active when the project started? 
                    # Actually, section headers update `current_section`.
                    # The project found *after* the header belongs to that header.
                    # So `current_section` is correct for the `new` project (this line).
                    # The `previous` project (saved now) belongs to the section it was found in.
                    # Wait, `current_section` is global.
                    # When I encounter a header, I update it.
                    # Then I encounter a name.
                    # So the name belongs to the updated section.
                    # The *previous* project (which is being saved now) belonged to the section *before* this name.
                    # But since I update `current_section` when I see the header, and headers come before names,
                    # the `current_section` variable holds the correct section for the `new` project.
                    # What about the `previous` project?
                    # It was processed under the `current_section` value *at that time*.
                    # So I should store the section *with* the project when I create it.
                    # Ah, I am storing `current_project_name` string. I need to store structure.
                    "text": "\n".join(current_project_text)
                })
                # But wait, the `projects_info.append` above uses `current_section`.
                # If I just updated `current_section` via a header line, 
                # and then I hit a name, the *previous* project (if any) is already finished?
                # Usually, headers separate projects or groups.
                # If a header appeared, `current_project_name` should have been saved/cleared?
                # My loop structure:
                # - If header: update section. (If there was a project pending, it should have been saved? No, because the header is just a line.)
                #   - The sample text: Project 1 ... \n Header \n Project 2 ...
                #   - When at Header:
                #     - Update section.
                #     - Should I save Project 1? Yes.
                #     - BUT, I only save when I hit a NEW NAME or Header?
                #     - My code checks header: `if new_section != current_section`.
                #       - It saves `current_project_name` if exists. Good.
                # - If Name:
                #   - Save previous project (if exists).
                #   - Start new project.
                #   - Set `current_project_obj` with section = current_section.
                pass
            
            # Start new project
            # Store the section NOW.
            # But wait, the `projects_info` list needs to store the finished project.
            # The *current* project is just starting.
            # I need a buffer variable for the *active* project.
            
            # Refined loop:
            # Buffer: `active_project = {"name": ..., "section": ..., "text_lines": []}`
            
            pass
            
    # Re-write the loop for clarity
    
projects_extracted = []
active_project = None
current_section = "Unknown"

# Helper to save
def save_project(proj):
    if proj:
        proj['text'] = "\n".join(proj['text_lines'])
        del proj['text_lines']
        projects_extracted.append(proj)

for doc in civic_data:
    lines = doc['text'].split('\n')
    current_section = "Unknown" # Reset per doc? Assuming headers are present.
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check Header
        new_sec = get_section(line, current_section)
        if new_sec != current_section:
            # Section change.
            # Save active project if any.
            save_project(active_project)
            active_project = None
            current_section = new_sec
            continue
            
        # Check Bullet/Update
        if line.startswith("(cid:190)") or line.startswith("(cid:131)") or line.startswith("Updates:") or line.startswith("Project Schedule:"):
            if active_project:
                active_project['text_lines'].append(line)
            continue
            
        # Check Junk
        if any(x in line for x in ["Page ", "Agenda Item", "Prepared by:", "Approved by:", "Date prepared:", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:"]):
            continue
            
        # Check for Name candidate
        # Heuristic: followed by (cid:190) in next few lines
        is_name = False
        for j in range(i + 1, min(i + 5, len(lines))):
            nl = lines[j].strip()
            if not nl: continue
            if nl.startswith("(cid:190)"):
                is_name = True
                break
            else:
                break
        
        if is_name:
            # Found a new name
            save_project(active_project)
            active_project = {
                "name": line,
                "section": current_section,
                "text_lines": []
            }
        else:
            # Just text? Add to current project if exists
            if active_project:
                active_project['text_lines'].append(line)

    # End of doc
    save_project(active_project)
    active_project = None

# Now process extracted projects to determine status and topics
final_projects = []
for p in projects_extracted:
    name = p['name']
    text = p['text']
    section = p['section']
    
    # Status
    status = "Unknown"
    if section == "Design":
        status = "Design"
    elif section == "Not Started":
        status = "Not Started"
    elif section == "Construction":
        if "completed" in text.lower():
            status = "Completed"
        else:
            status = "Construction" # or "Under Construction"
    elif section == "Disaster":
        # Check text for status
        if "completed" in text.lower():
            status = "Completed"
        elif "design" in text.lower():
            status = "Design"
        else:
            status = "Unknown"
    else:
        # Fallback
        if "completed" in text.lower(): status = "Completed"
        elif "design" in text.lower(): status = "Design"
            
    p['status'] = status
    
    # Topics
    topics = []
    keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]
    combined_text = (name + " " + text).lower()
    for k in keywords:
        if k in combined_text:
            topics.append(k)
    p['topics'] = topics
    
    # Check relatedness to 'emergency' or 'FEMA'
    # 1. Topic contains 'emergency' or 'FEMA'.
    # 2. Name contains 'emergency' or 'FEMA'.
    # 3. Type is 'disaster' (implied by section 'Disaster' or topic 'FEMA'?).
    
    is_related = False
    if "emergency" in combined_text or "fema" in combined_text:
        is_related = True
    if "disaster" in section.lower():
        is_related = True
        
    p['is_related'] = is_related

# Join with Funding
# Strategy: Iterate Funding. Find match in Projects.
# If Funding matches, use funding info + project status.
# If Project is related to emergency/FEMA, include.
# Or if Funding Name has 'FEMA'/'Emergency', include.

results = []
funding_used = set()

# Helper to normalize for matching
def norm(s):
    return s.lower().replace(" project", "").replace(" improvements", "").replace(" repairs", "").strip()

for fund in funding_data:
    f_name = fund['Project_Name']
    f_source = fund['Funding_Source']
    f_amount = fund['Amount']
    
    # Check if Funding entry itself is related
    f_related = "fema" in f_name.lower() or "emergency" in f_name.lower() or "disaster" in f_name.lower()
    
    # Find matching project in extracted list
    match = None
    
    # Exact match first
    for p in projects_extracted:
        if p['name'] == f_name:
            match = p
            break
            
    # Starts with match
    if not match:
        for p in projects_extracted:
            if f_name.startswith(p['name']):
                match = p
                break
    
    # Reverse starts with (Text name starts with Funding name? Unlikely given suffixes in Funding)
    if not match:
        for p in projects_extracted:
            if p['name'].startswith(f_name):
                match = p
                break
                
    # Fuzzy/Token match?
    # e.g. "Birdview Avenue Improvements (CalOES Project)" vs "Birdview Avenue Improvements"
    if not match:
        for p in projects_extracted:
            if p['name'] in f_name:
                match = p
                break

    status = "Unknown"
    p_related = False
    
    if match:
        status = match['status']
        p_related = match['is_related']
        
    if f_related or p_related:
        results.append({
            "Project_Name": f_name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5064142693074181436': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-5064142693074180553': 'file_storage/function-call-5064142693074180553.json', 'var_function-call-18362202212542543188': 'file_storage/function-call-18362202212542543188.json', 'var_function-call-18362202212542543219': 'file_storage/function-call-18362202212542543219.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-15070344879824368496'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-15070344879824368069'], 'r') as f:
    civic_docs = json.load(f)

# Keywords
keywords = ["park", "road", "fema", "fire", "emergency warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail", "emergency"]

# Helper to normalize strings
def normalize(s):
    return s.strip().lower()

# Parse civic docs
projects_info = {} # Name -> {status, topic, type, etc}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_type = None
    current_section_status = None
    
    # Iterate lines to find projects
    # We look for lines starting with (cid:190) or similar bullet.
    # The line before is the project name.
    # We also track headers.
    
    # Bullet char might be represented as (cid:190) or actual char. 
    # In the preview it is "(cid:190)". 
    # Let's handle both.
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for Section Headers
        if "Capital Improvement Projects (Design)" in line:
            current_type = "capital"
            current_section_status = "design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_type = "capital"
            current_section_status = "construction" # Handle specifically
        elif "Capital Improvement Projects (Not Started)" in line:
            current_type = "capital"
            current_section_status = "not started"
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"
            current_section_status = "design" # Default to design? Or check sub-headers?
            # Disaster projects might be listed under this header directly?
            # Let's assume structure is similar.
        
        # Check for Project Block
        # Look ahead for bullet
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") or next_line.startswith("¾"): # (cid:190) is ¾
                # Potential project name in current line
                p_name = line
                if not p_name: # Skip empty lines
                    i += 1
                    continue
                
                # Verify p_name is not a header?
                # Headers usually don't have bullets immediately after? 
                # Actually headers might be followed by text. 
                # But in the sample: "2022 Morning View ... \n \n (cid:190) Updates:"
                # So there might be empty lines.
                
                # Let's look backwards for the Name if current line is empty?
                # No, iterate lines. If we see a bullet line, the Project Name is the previous non-empty line.
                pass

        i += 1

# Refined Parsing Strategy
# Iterate lines. Keep track of last non-empty line as potential Project Name.
# When a bullet line is found (starting with (cid:190) or ¾), the last_non_empty_line is the Project Name.
# Then parse the block (Updates, Schedule) until the next Project Name is found (next bullet block).
# Wait, "Updates" is a bullet. "Project Schedule" is a bullet.
# So "Project Name" is only before the *first* bullet of the block.
# How to distinguish "Updates" bullet from "Project Name" bullet?
# Actually, the bullets *contain* "Updates:" or "Project Schedule:".
# So the structure is:
# [Project Name]
# [Bullet] Updates: ...
# [Bullet] Project Schedule: ...
#
# So if a line starts with a bullet, it belongs to the current project.
# If a line does NOT start with a bullet (and is not a header), it might be a new Project Name.

parsed_projects = {}
current_project_name = None
current_project_data = {}

# Reset state
current_type = None
current_section_status = None

doc_lines = civic_docs[0]['text'].replace('\r', '').split('\n')

# Iterate
last_non_empty_line = ""
line_idx = 0

while line_idx < len(doc_lines):
    line = doc_lines[line_idx].strip()
    
    if not line:
        line_idx += 1
        continue
        
    # Headers detection
    if "Capital Improvement Projects (Design)" in line:
        current_type = "capital"
        current_section_status = "design"
        current_project_name = None
        last_non_empty_line = line
        line_idx += 1
        continue
    if "Capital Improvement Projects (Construction)" in line:
        current_type = "capital"
        current_section_status = "construction"
        current_project_name = None
        last_non_empty_line = line
        line_idx += 1
        continue
    if "Capital Improvement Projects (Not Started)" in line:
        current_type = "capital"
        current_section_status = "not started"
        current_project_name = None
        last_non_empty_line = line
        line_idx += 1
        continue
    if "Disaster Recovery Projects" in line:
        current_type = "disaster"
        current_section_status = "disaster_section" # Might be mixed statuses
        current_project_name = None
        last_non_empty_line = line
        line_idx += 1
        continue
    
    # Check for Bullet
    is_bullet = line.startswith("(cid:190)") or line.startswith("¾")
    
    if is_bullet:
        # If we hit a bullet, the previous line (last_non_empty_line) was the Project Name, 
        # UNLESS we are already inside a project and this is just another bullet (like Schedule).
        # We need to decide if we are starting a new project.
        # Structure: Name -> Bullet(Updates) -> Bullet(Schedule) -> Name ...
        # So if the current project is None, OR the last line was NOT a bullet line from the same project...
        
        # Actually, if we are in a project, and we see a bullet, it continues the project.
        # If we see a non-bullet line, it's a candidate for the NEXT project name.
        # But that candidate is only confirmed when we see the NEXT bullet.
        
        # So:
        # If is_bullet:
        #   If current_project_name is None or (last_non_empty_line != current_project_name):
        #      # This means last_non_empty_line is the new project name.
        #      start_new_project(last_non_empty_line)
        #   parse_bullet_content(line)
        
        if current_project_name is None or (last_non_empty_line != current_project_name and last_non_empty_line != "Updates:" and "Agenda Item" not in last_non_empty_line and "Page" not in last_non_empty_line):
             # Validate last_non_empty_line is a valid name?
             # It shouldn't be a header (handled above) or page number.
             p_name = last_non_empty_line
             # Start new project
             current_project_name = p_name
             parsed_projects[p_name] = {
                 "type": current_type,
                 "status": current_section_status,
                 "topics": [],
                 "text_content": ""
             }
        
        # Add content to current project
        parsed_projects[current_project_name]["text_content"] += line + " "
        
        # Extract specific info from bullet line
        lower_line = line.lower()
        if "construction was completed" in lower_line or "construction has been completed" in lower_line:
             parsed_projects[current_project_name]["status"] = "completed"
        # If in disaster section, status might be different.
        
    else:
        # Non-bullet line. Could be text continuation or Next Project Name.
        # We store it as last_non_empty_line.
        last_non_empty_line = line

    line_idx += 1

# Post-processing parsed projects
final_projects = []

for p_name, p_data in parsed_projects.items():
    # Derive Topics
    # Combine Name and Text Content for keyword search
    full_text = (p_name + " " + p_data["text_content"]).lower()
    topics = []
    for kw in keywords:
        if kw in full_text:
            topics.append(kw)
    
    # Refine Status
    status = p_data["status"]
    if status == "construction":
        # If not explicitly completed, what is it?
        # Check text again
        if "completed" in p_data["text_content"].lower():
            status = "completed"
        else:
            status = "design" # Fallback or keep 'under construction'?
            # Hint says "Projects have three statuses: 'design', 'completed', 'not started'".
            # If "under construction", it's technically "active" -> "design"?
            # Or maybe "not started"? No.
            # I will allow "under construction" to be safe or map to "design" if required.
            # Given the specific 3 statuses in hint, I'll map "under construction" -> "design" (implementation phase)??
            # Or maybe I should check if the user *wants* the strict statuses.
            # "Projects have three statuses...". This usually means the answer expects one of these.
            # I will map "construction" section to "design" UNLESS it says "completed".
            pass 
    if status == "disaster_section":
        # Check text for status
        if "completed" in p_data["text_content"].lower():
            status = "completed"
        elif "design" in p_data["text_content"].lower() or "planning" in p_data["text_content"].lower():
            status = "design"
        else:
            status = "design" # Default for active disaster projects?
            
    # Map status to strict 3 if possible
    # "under construction" -> ? 
    # Let's keep "under construction" if found, maybe the hint was just descriptive of phases, not strict enum.
    # But wait, "Projects have three statuses..." is very specific.
    # If I see "Project is currently under construction", and I must choose [design, completed, not started],
    # "design" is the closest to "ongoing/active".
    
    # Let's just output the status I found, but normalized.
    # If I can't determine, use section default.
    
    p_data["topics"] = topics
    p_data["final_status"] = status
    
    # Check filter
    # "related to 'emergency' or 'FEMA'"
    # 'emergency' keyword matches 'emergency warning'.
    # 'FEMA' keyword matches 'FEMA'.
    # Also check Project Name for 'FEMA' or 'Emergency'.
    
    is_relevant = False
    if "fema" in topics or "emergency" in topics or "emergency warning" in topics:
        is_relevant = True
    if "fema" in p_name.lower() or "emergency" in p_name.lower():
        is_relevant = True
        
    if is_relevant:
        final_projects.append({
            "Project_Name": p_name,
            "Status": status,
            "Topics": topics
        })

# Join with Funding
# Normalize names for join?
# SQLite names are clean. Parsed names might have extra chars or slight diffs.
# I will try exact match first.

results = []
funding_map = {row['Project_Name']: row for row in funding_data}

for fp in final_projects:
    p_name = fp['Project_Name']
    # Try direct match
    f_info = funding_map.get(p_name)
    
    if not f_info:
        # Try stripping special chars or normalizing
        # Check if any funding name is in p_name or vice versa
        pass 
    
    if f_info:
        results.append({
            "Project Name": p_name,
            "Funding Source": f_info['Funding_Source'],
            "Amount": f_info['Amount'],
            "Status": fp['Status']
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json'}

exec(code, env_args)

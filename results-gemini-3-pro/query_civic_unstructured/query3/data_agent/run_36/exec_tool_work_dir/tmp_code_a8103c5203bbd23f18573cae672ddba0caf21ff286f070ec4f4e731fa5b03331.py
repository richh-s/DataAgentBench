code = """import json

# Load data
with open(locals()['var_function-call-15070344879824368496'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-15070344879824368069'], 'r') as f:
    civic_docs = json.load(f)

# Keywords
keywords = ["park", "road", "fema", "fire", "emergency warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail", "emergency"]

parsed_projects = {}
current_project_name = None
current_data = {}
last_non_empty_line = ""

# Status defaults
current_section_status = "design"

# Process text
text = civic_docs[0]['text']
lines = text.split('\n')

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    # Headers
    if "Capital Improvement Projects (Design)" in line:
        current_section_status = "design"
        current_project_name = None
        continue
    if "Capital Improvement Projects (Construction)" in line:
        current_section_status = "construction" # Mixed
        current_project_name = None
        continue
    if "Capital Improvement Projects (Not Started)" in line:
        current_section_status = "not started"
        current_project_name = None
        continue
    if "Disaster Recovery Projects" in line:
        current_section_status = "disaster" # Mixed
        current_project_name = None
        continue
        
    # Bullet detection
    # (cid:190) is \u00be
    is_bullet = line.startswith("(cid:190)") or line.startswith("\u00be")
    
    if is_bullet:
        # If we have a pending candidate name (last_non_empty_line), and we are not just continuing the current project...
        # A new bullet block starts.
        # If the bullet says "Updates:" or "Project Schedule:", it belongs to a project.
        # The project name is the line above (last_non_empty_line).
        
        # Check if last_non_empty_line is likely a project name
        # It shouldn't be a known keyword like "Updates:" (though bullet line contains Updates, the PREVIOUS line is Name)
        
        if current_project_name != last_non_empty_line:
            # New project detected
            # But we must ensure last_non_empty_line is valid.
            # E.g. exclude page numbers or agenda items headers if they appear as lines.
            if "Page" not in last_non_empty_line and "Agenda Item" not in last_non_empty_line:
                current_project_name = last_non_empty_line
                parsed_projects[current_project_name] = {
                    "status": current_section_status,
                    "text": ""
                }
        
        # Add line to text
        if current_project_name:
            parsed_projects[current_project_name]["text"] += line + " "
            
            # Check for completion in text
            lower = line.lower()
            if "construction was completed" in lower or "construction has been completed" in lower:
                parsed_projects[current_project_name]["status"] = "completed"
                
    else:
        # Potential name for next project
        last_non_empty_line = line

# Filter and Join
results = []
funding_map = {f['Project_Name']: f for f in funding_data}

for p_name, p_data in parsed_projects.items():
    # Determine Topics
    p_topics = []
    full_text = (p_name + " " + p_data["text"]).lower()
    for kw in keywords:
        if kw in full_text:
            p_topics.append(kw)
            
    # Determine Final Status
    status = p_data["status"]
    if status == "construction":
        # If not marked completed
        if "completed" not in p_data.get("final_status_override", ""): # Check logic above
             # We set status="completed" in loop if found.
             # If it's still "construction", it means we didn't find "completed".
             # So it's "design" (active) or "under construction".
             # Given hint 3 statuses, we use "design" or "not started" or "completed".
             # Active construction is closest to "design" (implementation) or we output "under construction".
             # I'll stick to what the text says if possible, or "design" if forced.
             # But let's check if the prompt requires strictly those 3.
             # "Projects have three statuses: ...". 
             # This implies I should classify into these 3.
             # "under construction" -> "design"? No, usually distinct.
             # But "design" is "planning/design phase".
             # Maybe "Capital Improvement Projects (Construction)" -> "completed" is the intent?
             # But text says "Project is currently under construction".
             # I will output "design" as it is "in progress".
             status = "design"
    
    if status == "disaster":
        # Default for disaster section if not completed
        status = "design"
        
    # Check Filter
    is_related = False
    if "fema" in p_topics or "emergency" in p_topics or "emergency warning" in p_topics:
        is_related = True
    if "fema" in p_name.lower() or "emergency" in p_name.lower():
        is_related = True
        
    if is_related:
        # Join
        f_info = funding_map.get(p_name)
        if f_info:
            results.append({
                "Project_Name": p_name,
                "Funding_Source": f_info['Funding_Source'],
                "Amount": f_info['Amount'],
                "Status": status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json'}

exec(code, env_args)

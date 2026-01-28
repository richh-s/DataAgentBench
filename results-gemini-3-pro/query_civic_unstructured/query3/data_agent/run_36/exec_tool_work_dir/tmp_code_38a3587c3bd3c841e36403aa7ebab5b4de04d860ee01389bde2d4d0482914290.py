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
current_section_status = "design"
last_non_empty_line = ""

# Process text
text = civic_docs[0]['text']
lines = text.split(chr(10))

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
        current_section_status = "construction"
        current_project_name = None
        continue
    if "Capital Improvement Projects (Not Started)" in line:
        current_section_status = "not started"
        current_project_name = None
        continue
    if "Disaster Recovery Projects" in line:
        current_section_status = "disaster"
        current_project_name = None
        continue
        
    # Bullet detection
    # (cid:190) or ¾
    is_bullet = line.startswith("(cid:190)") or line.startswith(chr(190))
    
    if is_bullet:
        if current_project_name != last_non_empty_line:
            if "Page" not in last_non_empty_line and "Agenda Item" not in last_non_empty_line:
                current_project_name = last_non_empty_line
                parsed_projects[current_project_name] = {
                    "status": current_section_status,
                    "text": ""
                }
        
        if current_project_name:
            parsed_projects[current_project_name]["text"] += line + " "
            
            lower = line.lower()
            if "construction was completed" in lower or "construction has been completed" in lower:
                parsed_projects[current_project_name]["status"] = "completed"
                
    else:
        last_non_empty_line = line

# Filter and Join
results = []
funding_map = {f['Project_Name']: f for f in funding_data}

for p_name, p_data in parsed_projects.items():
    p_topics = []
    full_text = (p_name + " " + p_data["text"]).lower()
    for kw in keywords:
        if kw in full_text:
            p_topics.append(kw)
            
    status = p_data["status"]
    if status == "construction":
        # Check text again for completion if not caught
        if "completed" in p_data["text"].lower():
             status = "completed"
        else:
             status = "design" 
    if status == "disaster":
        status = "design" # Default
        
    # Filter
    is_related = False
    if "fema" in p_topics or "emergency" in p_topics or "emergency warning" in p_topics:
        is_related = True
    if "fema" in p_name.lower() or "emergency" in p_name.lower():
        is_related = True
        
    if is_related:
        f_info = funding_map.get(p_name)
        if f_info:
            results.append({
                "Project Name": p_name,
                "Funding Source": f_info['Funding_Source'],
                "Amount": f_info['Amount'],
                "Status": status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json'}

exec(code, env_args)

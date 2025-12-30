code = """import json

# Load data
with open('var_function-call-15771920902434159033.json', 'r') as f:
    civic_docs = json.load(f)
    
with open('var_function-call-13220906500236783647.json', 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_status = None
    
    buffer_lines = []
    current_project_name = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for header
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            if "(" in line and ")" in line:
                # Extract status between parens
                parts = line.split("(")
                status_part = parts[-1].replace(")", "").strip().lower()
                current_status = status_part
            else:
                current_status = "unknown"
            
            # Save previous
            if current_project_name:
                desc = " ".join(buffer_lines)
                projects.append({
                    "Project_Name": current_project_name,
                    "description": desc,
                    "status": "unknown" # use previous status
                })
                # But wait, I need to store the status associated with the previous block
                # My logic for saving 'previous' is slightly buggy here because I update current_status before saving.
                # Actually, the previous project belongs to the *previous* status.
                # I should store 'previous_status' or just correct the loop.
                # Correct fix: I'll just append the previous project with the *old* status (which I don't track easily here).
                # Simpler: Update status, then continue. The previous project was already saved or belongs to previous section?
                # No, if I hit a header, the *previous* project (from the previous section) is finished.
                # So I should save it using `current_status` (which is the *old* status before I update it).
                # Wait, I update `current_status` *after* saving?
                # No, I update it inside the `if`.
                # Let's fix:
            pass # placeholder
            
            # Logic inside header block
            # Save previous project with OLD status
            if current_project_name:
                # But wait, `current_status` variable currently holds the status of the *current* project being built.
                # So if I use `current_status` here, it is correct (it's the one from the section we just finished).
                desc = " ".join(buffer_lines)
                projects.append({
                    "Project_Name": current_project_name,
                    "description": desc,
                    "status": current_status 
                })
                current_project_name = None
                buffer_lines = []

            # Now update status for the NEW section
            if "(" in line and ")" in line:
                parts = line.split("(")
                status_part = parts[-1].replace(")", "").strip().lower()
                current_status = status_part
            else:
                current_status = "unknown"
                
            i += 1
            continue
            
        if current_status:
            is_new_project = False
            # Heuristics
            if line and not line.startswith("Page") and not line.startswith("Agenda") and not line.startswith("Item") and "cid:" not in line:
                 if i + 1 < len(lines):
                     next_line = lines[i+1].strip()
                     # Check for update indicators
                     if "Updates:" in next_line or "Project Description:" in next_line or "cid:" in next_line:
                         is_new_project = True
            
            if is_new_project:
                # Save previous
                if current_project_name:
                    desc = " ".join(buffer_lines)
                    projects.append({
                        "Project_Name": current_project_name,
                        "description": desc,
                        "status": current_status
                    })
                
                current_project_name = line
                buffer_lines = []
            else:
                if current_project_name:
                    buffer_lines.append(line)
        
        i += 1

    # Save last
    if current_project_name:
        desc = " ".join(buffer_lines)
        projects.append({
            "Project_Name": current_project_name,
            "description": desc,
            "status": current_status
        })

final_results = []
for p in projects:
    name = p['Project_Name']
    desc = p['description']
    status = p['status']
    
    # Check if really completed
    if "construction was completed" in desc.lower():
        status = "completed"
    
    # Check keywords
    text_blob = (name + " " + desc).lower()
    if "emergency" in text_blob or "fema" in text_blob:
        
        funding = funding_map.get(name)
        if not funding:
            # Fuzzy
            candidates = [v for k,v in funding_map.items() if k.startswith(name)]
            if candidates:
                funding = candidates[0]
        
        f_source = funding['Funding_Source'] if funding else "N/A"
        f_amount = funding['Amount'] if funding else "N/A"
        
        final_results.append({
            "Project_Name": name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-4008715317058091339': 'file_storage/function-call-4008715317058091339.json', 'var_function-call-4008715317058091730': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15771920902434159033': 'file_storage/function-call-15771920902434159033.json', 'var_function-call-13220906500236783647': 'file_storage/function-call-13220906500236783647.json'}

exec(code, env_args)

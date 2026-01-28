code = """import json
import re

# Load data
with open('var_function-call-15771920902434159033.json', 'r') as f:
    civic_docs = json.load(f)
    
with open('var_function-call-13220906500236783647.json', 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    current_type = None 
    
    buffer_lines = []
    current_project_name = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for header
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            # Check for parens
            if "(" in line and ")" in line:
                status_part = line.split("(")[1].split(")")[0].lower()
                current_status = status_part
            else:
                current_status = "unknown"
            
            # Save previous project
            if current_project_name:
                desc = "\n".join(buffer_lines)
                projects.append({
                    "Project_Name": current_project_name,
                    "description": desc,
                    "status": current_status,
                    "type": current_type
                })
                current_project_name = None
                buffer_lines = []
            
            if "Capital" in line:
                current_type = "capital"
            else:
                current_type = "disaster"
            
            i += 1
            continue
            
        if current_status:
            # Check for new project start
            is_new_project = False
            # Avoid page headers/footers
            if line and not line.startswith("Page") and not line.startswith("Agenda") and not line.startswith("(cid:190)") and not line.startswith("(cid:131)"):
                 # Look ahead
                 if i + 1 < len(lines):
                     next_line = lines[i+1].strip()
                     if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                         is_new_project = True
            
            if is_new_project:
                if current_project_name:
                    desc = "\n".join(buffer_lines)
                    projects.append({
                        "Project_Name": current_project_name,
                        "description": desc,
                        "status": current_status, # Use the status of the section the project was found in
                        "type": current_type
                    })
                
                current_project_name = line
                buffer_lines = []
            else:
                if current_project_name:
                    buffer_lines.append(line)
        
        i += 1

    # Save last
    if current_project_name:
        desc = "\n".join(buffer_lines)
        projects.append({
            "Project_Name": current_project_name,
            "description": desc,
            "status": current_status,
            "type": current_type
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
        
        # Find funding
        funding = funding_map.get(name)
        
        if not funding:
            # Try fuzzy match (startswith)
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

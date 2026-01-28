code = """import json
import re

with open('var_function-call-8182209293978562195', 'r') as f:
    docs = json.load(f)

with open('var_function-call-15395128546112038851', 'r') as f:
    funding = json.load(f)

funding_names = set(item['Project_Name'] for item in funding)
projects = []

for doc in docs:
    text = doc['text']
    lines = text.split(chr(10))
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        is_new_project = False
        
        if line in funding_names:
            is_new_project = True
        else:
            # Heuristic check
            for k in range(1, 4):
                if i + k < len(lines):
                    next_l = lines[i+k].strip()
                    if "Updates:" in next_l or "Project Description:" in next_l:
                         if len(line) > 5 and "Agenda" not in line and "Page" not in line:
                             is_new_project = True
                             break
        
        if is_new_project:
            if current_project:
                projects.append(current_project)
            current_project = {"name": line, "text": []}
        
        if current_project:
            current_project["text"].append(line)

    if current_project:
        projects.append(current_project)

analyzed_projects = []
for p in projects:
    full_text = " ".join(p["text"])
    
    start_date = ""
    # Regex for start date
    # Look for 2022 in start context
    match = re.search(r"Begin Construction:?\s*([A-Za-z0-9\s]+)", full_text, re.IGNORECASE)
    if match:
        start_date = match.group(1).strip()
    
    is_disaster = False
    if any(k in full_text.upper() for k in ["FEMA", "CALOES", "DISASTER", "WOOLSEY", "RECOVERY"]):
        is_disaster = True
        
    analyzed_projects.append({
        "name": p["name"],
        "start_date": start_date,
        "is_disaster": is_disaster
    })

print("__RESULT__:")
print(json.dumps(analyzed_projects))"""

env_args = {'var_function-call-17928919016931246816': 'file_storage/function-call-17928919016931246816.json', 'var_function-call-17928919016931249021': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8182209293978562195': 'file_storage/function-call-8182209293978562195.json', 'var_function-call-15395128546112038851': 'file_storage/function-call-15395128546112038851.json'}

exec(code, env_args)

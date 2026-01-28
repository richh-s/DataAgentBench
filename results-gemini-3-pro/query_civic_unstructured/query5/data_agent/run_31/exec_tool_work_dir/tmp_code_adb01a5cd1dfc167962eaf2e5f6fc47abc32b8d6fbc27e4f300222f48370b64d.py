code = """import json
import re

# Load civic docs
with open('var_function-call-8182209293978562195', 'r') as f:
    docs = json.load(f)

# Load funding docs
with open('var_function-call-15395128546112038851', 'r') as f:
    funding = json.load(f)
funding_names = set(item['Project_Name'] for item in funding)

projects = []

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Iterate to find project blocks
    # Heuristic: A line is a project name if it matches a known funding name 
    # OR it looks like a header (checked via subsequent lines)
    # Given the description "matches the project names... extracted", we can try to match to funding list.
    
    # Let's try to identify project sections first
    current_project = None
    current_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a project name
        # We can check if it exists in funding_names
        # Or use the heuristic of being followed by updates
        is_new_project = False
        
        # Check against funding names (exact match)
        if line in funding_names:
            is_new_project = True
        else:
            # Check for suffixes mapping
            # Actually, let's rely on the text structure mainly
            # The sample showed names followed by "(cid:190) Updates:"
            # Look ahead
            for k in range(1, 5):
                if i + k < len(lines):
                    next_l = lines[i+k].strip()
                    if next_l.startswith("(cid:190)") or next_l.startswith("Updates:") or next_l.startswith("Project Description:") or "Updates:" in next_l:
                        # But ensure it's not a generic line
                        if len(line) > 5 and "Agenda" not in line and "Page" not in line:
                             is_new_project = True
                        break
        
        if is_new_project:
            # Save previous
            if current_project:
                projects.append(current_project)
            
            current_project = {
                "name": line,
                "text": [],
                "start_date": None,
                "is_disaster": False
            }
        
        if current_project:
            current_project["text"].append(line)

    if current_project:
        projects.append(current_project)

# Process extracted projects
results = []
for p in projects:
    full_text = " ".join(p["text"])
    
    # Extract Start Date
    # Pattern: Begin Construction: [Date]
    # or Start: [Date]
    st_match = re.search(r"(?:Begin Construction|Start Date|Estimated Schedule|Project Schedule)[:\s]+(.*?)(?:\(cid:131\)|\(cid:190\)|\n|$)", full_text, re.IGNORECASE)
    # The text has bullets (cid:131).
    # Sample: "(cid:131) Begin Construction: Fall 2023"
    
    st_val = ""
    # Let's be more specific with regex for the sample format
    # Look for "Begin Construction: <value>"
    bc_match = re.search(r"Begin Construction[:\s]+([A-Za-z0-9\s]+)", full_text, re.IGNORECASE)
    if bc_match:
        st_val = bc_match.group(1).strip()
    
    p["start_date"] = st_val
    
    # Check Disaster
    # Keywords
    is_disaster = False
    keywords = ["FEMA", "CalOES", "Disaster", "Woolsey", "Fire", "Recovery"]
    if any(k.upper() in full_text.upper() for k in keywords):
        is_disaster = True
    
    p["is_disaster"] = is_disaster
    results.append(p)

print("__RESULT__:")
print(json.dumps(results[:20])) # Print preview"""

env_args = {'var_function-call-17928919016931246816': 'file_storage/function-call-17928919016931246816.json', 'var_function-call-17928919016931249021': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8182209293978562195': 'file_storage/function-call-8182209293978562195.json', 'var_function-call-15395128546112038851': 'file_storage/function-call-15395128546112038851.json'}

exec(code, env_args)

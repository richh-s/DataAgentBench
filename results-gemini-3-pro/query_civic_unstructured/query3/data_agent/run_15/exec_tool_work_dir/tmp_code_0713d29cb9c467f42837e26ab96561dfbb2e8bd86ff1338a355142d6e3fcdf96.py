code = """import json
import re

# Load data
with open('var_function-call-15771920902434159033.json', 'r') as f:
    civic_docs = json.load(f)
    
with open('var_function-call-13220906500236783647.json', 'r') as f:
    funding_data = json.load(f)

# Create a map for funding for faster lookup
# Normalize keys? The names seem to match well based on manual inspection.
funding_map = {item['Project_Name']: item for item in funding_data}

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    current_type = None # "capital" or "disaster"
    
    buffer_lines = []
    current_project_name = None
    
    # Regex for headers
    # "Capital Improvement Projects (Design)"
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    # "Disaster Recovery Projects"? (None seen in sample, but maybe exists)
    
    # To be robust, I'll search for lines containing "Projects (" or "Projects" and treat as header if it looks like one.
    # In the sample: "Capital Improvement Projects (Design)"
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for header
        # We assume headers have "Projects (" in them or are just "Capital Improvement Projects" etc.
        # But looking at the sample:
        # "Capital Improvement Projects (Design)"
        # "Capital Improvement Projects (Construction)"
        # "Capital Improvement Projects (Not Started)"
        
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            # Check for parens
            status_match = re.search(r"\((.*?)\)", line)
            
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
            
            if status_match:
                s = status_match.group(1).lower()
                current_status = s # design, construction, not started
            else:
                current_status = "unknown" # or derived from context
            
            i += 1
            continue
            
        if current_status:
            # Check for new project start
            # Logic: Next line starts with (cid:190) or "Updates:" or "Project Description:"
            is_new_project = False
            if line and not line.startswith("Page") and not line.startswith("Agenda") and not line.startswith("(cid:190)") and not line.startswith("(cid:131)"):
                 # Look ahead
                 if i + 1 < len(lines):
                     next_line = lines[i+1].strip()
                     # In sample, artifacts like (cid:190) appear.
                     if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                         is_new_project = True
            
            if is_new_project:
                if current_project_name:
                    desc = "\n".join(buffer_lines)
                    projects.append({
                        "Project_Name": current_project_name,
                        "description": desc,
                        "status": current_status,
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

# Filter and format
final_results = []
for p in projects:
    name = p['Project_Name']
    desc = p['description']
    status = p['status']
    
    # Refine status
    # If description says "Construction was completed", status = completed
    if "construction was completed" in desc.lower():
        status = "completed"
    
    # Check keywords in Name or Description
    # Keywords: "emergency", "FEMA"
    text_blob = (name + " " + desc).lower()
    if "emergency" in text_blob or "fema" in text_blob:
        
        # Find funding
        # Try exact match
        funding = funding_map.get(name)
        
        # If not found, try appending " (FEMA Project)" etc?
        if not funding:
            # Check extracting prefixes?
            # Or iterate funding map to find partial matches?
            # E.g. "Outdoor Warning Sirens" matches "Outdoor Warning Sirens (FEMA Project)"?
            # Or "Latigo Canyon Road Retaining Wall Repair Project" matches "Latigo Canyon Road Retaining Wall Repair Project"
            
            # Simple fuzzy: Check if project name starts with extracted name
            candidates = [v for k,v in funding_map.items() if k.startswith(name)]
            if candidates:
                funding = candidates[0] # Take first match
        
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

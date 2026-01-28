code = """import json
import re

# Load data
with open(locals()['var_function-call-7451822493204456003'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-4857704780297180574'], 'r') as f:
    civic_docs = json.load(f)

# Combine all text
full_text = "\n".join([doc['text'] for doc in civic_docs])
lines = full_text.split('\n')

projects = []
current_type = "capital" # Default
current_status = None
current_project = None

# Symbols to ignore or treat as bullets
bullets = ["(cid:190)", "(cid:131)"]

clean_lines = [l.strip() for l in lines if l.strip()]

i = 0
while i < len(clean_lines):
    line = clean_lines[i]
    
    # Check headers
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
        if "Disaster" in line:
            current_type = "disaster"
        else:
            current_type = "capital"
        
        if "Design" in line:
            current_status = "design"
        elif "Construction" in line:
            current_status = "construction"
        elif "Not Started" in line:
            current_status = "not started"
        elif "Completed" in line:
            current_status = "completed"
        
        i += 1
        continue
    
    # Identify Project Name
    # Condition: Line does not start with bullet, Page, Agenda Item
    # And next line(s) contain "Updates:" or "Project Description:" or "Project Schedule:"
    is_project = False
    if not any(line.startswith(b) for b in bullets) and not line.startswith("Page") and not line.startswith("Agenda"):
        if i + 1 < len(clean_lines):
            next_line = clean_lines[i+1]
            if "Updates:" in next_line or "Project Description:" in next_line or "Project Schedule:" in next_line:
                is_project = True
            elif any(next_line.startswith(b) for b in bullets) and ("Updates" in next_line or "Description" in next_line):
                is_project = True
    
    if is_project:
        if current_project:
            projects.append(current_project)
        
        p_name = line
        p_type = current_type
        # Overwrite type if name contains keywords
        if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name:
            p_type = "disaster"
            
        current_project = {
            "name": p_name,
            "type": p_type,
            "status": current_status,
            "start_info": [],
            "raw": ""
        }
        i += 1
        continue

    # Capture details
    if current_project:
        current_project["raw"] += line + " "
        # Extract dates
        # Look for "Begin Construction: <val>"
        # or "Start Date: <val>"
        # or "Advertise: <val>"
        if "Begin Construction" in line or "Start" in line or "Advertise" in line or "Completed" in line:
            current_project["start_info"].append(line)
            
    i += 1

if current_project:
    projects.append(current_project)

# Filter for Disaster + Start 2022
candidates = []
for p in projects:
    is_disaster = (p['type'] == 'disaster')
    
    # Check start date
    # We look for "Begin Construction: ... 2022" or similar
    started_2022 = False
    
    # Check extracted info
    for info in p['start_info']:
        # Normalize
        info_lower = info.lower()
        if "2022" in info:
            if "begin construction" in info_lower:
                started_2022 = True
            elif "construction was completed" in info_lower:
                # If completed in 2022, did it start in 2022?
                # E.g. "Construction was completed November 2022"
                # If it's a small project.
                # But safer to look for explicit start. 
                # Or if the prompt implies "started in 2022" (meaning the start date is in 2022).
                pass
            elif "start" in info_lower and "date" in info_lower:
                started_2022 = True
    
    # Also check if just "Start: ... 2022" is in raw text
    if not started_2022:
         # simple regex
         if re.search(r"Begin Construction.*2022", p['raw'], re.IGNORECASE):
             started_2022 = True
    
    if is_disaster and started_2022:
        candidates.append(p['name'])

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-7451822493204456003': 'file_storage/function-call-7451822493204456003.json', 'var_function-call-4857704780297180574': 'file_storage/function-call-4857704780297180574.json'}

exec(code, env_args)

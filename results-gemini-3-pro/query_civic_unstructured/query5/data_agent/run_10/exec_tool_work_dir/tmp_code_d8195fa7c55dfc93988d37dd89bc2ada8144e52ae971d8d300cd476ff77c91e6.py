code = """import json
import re

with open(locals()['var_function-call-7451822493204456003'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-4857704780297180574'], 'r') as f:
    civic_docs = json.load(f)

# Use chr(10) for newline to avoid escaping issues
full_text = chr(10).join([doc['text'] for doc in civic_docs])
lines = full_text.splitlines()

projects = []
current_type = "capital" 
current_project = None
bullets = ["(cid:190)", "(cid:131)"]

clean_lines = [l.strip() for l in lines if l.strip()]

i = 0
while i < len(clean_lines):
    line = clean_lines[i]
    
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
        if "Disaster" in line:
            current_type = "disaster"
        else:
            current_type = "capital"
        i += 1
        continue
    
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
        if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name:
            p_type = "disaster"
        current_project = {"name": p_name, "type": p_type, "start_info": [], "raw": ""}
        i += 1
        continue

    if current_project:
        current_project["raw"] += line + " "
        if "Begin Construction" in line or "Start" in line or "Advertise" in line:
            current_project["start_info"].append(line)
    i += 1

if current_project:
    projects.append(current_project)

candidates = []
for p in projects:
    if p['type'] == 'disaster':
        started_2022 = False
        for info in p['start_info']:
            if "2022" in info:
                if "Begin Construction" in info:
                    started_2022 = True
        
        if not started_2022:
             if re.search(r"Begin Construction.*?2022", p['raw'], re.IGNORECASE):
                 started_2022 = True
        
        if started_2022:
            candidates.append(p['name'])

total = 0
matched = []
for item in funding_data:
    if item['Project_Name'] in candidates:
        total += int(item['Amount'])
        matched.append(item['Project_Name'])

print("__RESULT__:")
print(json.dumps({"total_funding": total, "matched_projects": matched}))"""

env_args = {'var_function-call-7451822493204456003': 'file_storage/function-call-7451822493204456003.json', 'var_function-call-4857704780297180574': 'file_storage/function-call-4857704780297180574.json'}

exec(code, env_args)

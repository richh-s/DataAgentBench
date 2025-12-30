code = """import json
import re

with open(locals()['var_function-call-4857704780297180574'], 'r') as f:
    civic_docs = json.load(f)

full_text = chr(10).join([doc['text'] for doc in civic_docs])
lines = full_text.splitlines()

# Re-run extraction for debugging
projects = []
current_type = "capital" 
current_project = None
bullets = ["(cid:190)", "(cid:131)"]
clean_lines = [l.strip() for l in lines if l.strip()]

i = 0
while i < len(clean_lines):
    line = clean_lines[i]
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
        if "Disaster" in line: current_type = "disaster"
        else: current_type = "capital"
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
        if current_project: projects.append(current_project)
        p_name = line
        p_type = current_type
        if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name: p_type = "disaster"
        current_project = {"name": p_name, "type": p_type, "start_info": [], "raw": ""}
        i += 1
        continue
    if current_project:
        current_project["raw"] += line + " "
        if "Begin Construction" in line or "Start" in line or "Advertise" in line:
            current_project["start_info"].append(line)
    i += 1
if current_project: projects.append(current_project)

target_names = ["Clover Heights Storm Drain (FEMA Project)", "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)"]
debug_info = {}

for p in projects:
    if p['name'] in target_names:
        debug_info[p['name']] = {"start_info": p['start_info'], "raw_snippet": p['raw'][:200]}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-7451822493204456003': 'file_storage/function-call-7451822493204456003.json', 'var_function-call-4857704780297180574': 'file_storage/function-call-4857704780297180574.json', 'var_function-call-10043203154635613879': {'total_funding': 450000, 'matched_projects': ['Clover Heights Storm Drain (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)']}}

exec(code, env_args)

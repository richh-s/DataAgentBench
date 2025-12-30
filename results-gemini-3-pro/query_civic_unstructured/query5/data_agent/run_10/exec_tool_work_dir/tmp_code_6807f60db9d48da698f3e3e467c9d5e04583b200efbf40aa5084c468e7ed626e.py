code = """import json
import re

with open(locals()['var_function-call-4857704780297180574'], 'r') as f:
    civic_docs = json.load(f)

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
        current_project = {"name": p_name, "raw": ""}
        i += 1
        continue
    if current_project:
        current_project["raw"] += line + " "
    i += 1
if current_project: projects.append(current_project)

target = "Clover Heights Storm Drain (FEMA Project)"
result = ""
for p in projects:
    if p['name'] == target:
        result = p['raw']
        break

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7451822493204456003': 'file_storage/function-call-7451822493204456003.json', 'var_function-call-4857704780297180574': 'file_storage/function-call-4857704780297180574.json', 'var_function-call-10043203154635613879': {'total_funding': 450000, 'matched_projects': ['Clover Heights Storm Drain (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)']}, 'var_function-call-3541645533462830078': {'Clover Heights Storm Drain (FEMA Project)': {'start_info': [], 'raw_snippet': '(cid:190) Project Description: This project consists of design and construction of a few storm drains on Clover Heights. The existing storm drain facility ends at the intersection of Clover Heights an'}, 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)': {'start_info': ['(cid:131) Begin Construction: Spring 2022'], 'raw_snippet': '(cid:190) Project Description: This project consists of repairing damage storm drain facilities and roadway embankments that were damaged by the Woolsey Fire. (cid:190) Estimated Schedule: (cid:131) C'}}}

exec(code, env_args)

code = """import json
import re
from datetime import datetime

with open(locals()['var_function-call-7451822493204456003'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-4857704780297180574'], 'r') as f:
    civic_docs = json.load(f)

def get_date(filename):
    match = re.search(r"(\d{8})", filename)
    if match:
        d_str = match.group(1)
        try:
            return datetime.strptime(d_str, "%m%d%Y").timestamp()
        except:
            return 0
    return 0

all_projects = []

for doc in civic_docs:
    d_date = get_date(doc['filename'])
    text = doc['text']
    lines = text.splitlines()
    
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
            if current_project:
                current_project['doc_date'] = d_date
                all_projects.append(current_project)
            p_name = line
            p_type = current_type
            if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name: p_type = "disaster"
            current_project = {"name": p_name, "type": p_type, "start_info": [], "raw": ""}
            i += 1
            continue
        
        if current_project:
            current_project["raw"] += line + " "
            if "Begin Construction" in line or "Start" in line or "Advertise" in line or "Completed" in line:
                current_project["start_info"].append(line)
        i += 1
    
    if current_project:
        current_project['doc_date'] = d_date
        all_projects.append(current_project)

# Sort by date desc
all_projects.sort(key=lambda x: x['doc_date'], reverse=True)

latest_projects = {}
for p in all_projects:
    name = p['name']
    if name not in latest_projects:
        latest_projects[name] = p

candidates = []
for name, p in latest_projects.items():
    if p['type'] == 'disaster':
        started_2022 = False
        for info in p['start_info']:
            if "2022" in info:
                if "Begin Construction" in info or "Start" in info:
                    started_2022 = True
        
        if not started_2022:
             if re.search(r"Begin Construction.*?2022", p['raw'], re.IGNORECASE):
                 started_2022 = True
             elif re.search(r"Start.*?2022", p['raw'], re.IGNORECASE):
                 started_2022 = True

        if started_2022:
            candidates.append(name)

total = 0
matched = []
for item in funding_data:
    if item['Project_Name'] in candidates:
        total += int(item['Amount'])
        matched.append(item['Project_Name'])

print("__RESULT__:")
print(json.dumps({"total": total, "matched": matched}))"""

env_args = {'var_function-call-7451822493204456003': 'file_storage/function-call-7451822493204456003.json', 'var_function-call-4857704780297180574': 'file_storage/function-call-4857704780297180574.json', 'var_function-call-10043203154635613879': {'total_funding': 450000, 'matched_projects': ['Clover Heights Storm Drain (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)']}, 'var_function-call-3541645533462830078': {'Clover Heights Storm Drain (FEMA Project)': {'start_info': [], 'raw_snippet': '(cid:190) Project Description: This project consists of design and construction of a few storm drains on Clover Heights. The existing storm drain facility ends at the intersection of Clover Heights an'}, 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)': {'start_info': ['(cid:131) Begin Construction: Spring 2022'], 'raw_snippet': '(cid:190) Project Description: This project consists of repairing damage storm drain facilities and roadway embankments that were damaged by the Woolsey Fire. (cid:190) Estimated Schedule: (cid:131) C'}}, 'var_function-call-2311566345612501718': '(cid:190) Project Description: This project consists of design and construction of a few storm drains on Clover Heights. The existing storm drain facility ends at the intersection of Clover Heights and Harvester Road. During storms, this intersection floods and causes debris to block the road. An extended storm '}

exec(code, env_args)

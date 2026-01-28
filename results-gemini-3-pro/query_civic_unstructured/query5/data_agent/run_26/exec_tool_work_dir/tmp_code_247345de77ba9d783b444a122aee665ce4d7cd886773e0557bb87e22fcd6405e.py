code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

total_funding = 0
matched_projects = []

# Identify header sections by finding their indices
cap_header = "Capital Improvement Projects"
dis_header = "Disaster Recovery Projects"
header_indices = []

pos = 0
while True:
    idx = text.find(cap_header, pos)
    if idx == -1: break
    header_indices.append((idx, "capital"))
    pos = idx + 1

pos = 0
while True:
    idx = text.find(dis_header, pos)
    if idx == -1: break
    header_indices.append((idx, "disaster"))
    pos = idx + 1

header_indices.sort(key=lambda x: x[0])

for project_name, amount in funding_map.items():
    # Search for project name in text
    # Use simple find
    idx = text.find(project_name)
    if idx != -1:
        # Determine section
        section = "capital"
        for h_idx, h_type in header_indices:
            if h_idx < idx:
                section = h_type
            else:
                break
        
        is_disaster = False
        if "disaster" in section:
            is_disaster = True
        if "(FEMA" in project_name or "(CalOES" in project_name or "CalJPIA" in project_name:
            is_disaster = True
            
        if not is_disaster:
            continue
            
        # Check start date in context
        # Look at next 1000 chars
        context = text[idx:idx+1000]
        
        started_2022 = False
        if "2022" in project_name:
            started_2022 = True
        
        # Check for Begin Construction or Advertise with 2022
        # regex is safer for finding the specific phrase
        if re.search(r"Begin [cC]onstruction.*2022", context):
            started_2022 = True
        elif re.search(r"Advertise.*2022", context):
            started_2022 = True
        elif re.search(r"awarded the contract.*2022", context):
            started_2022 = True
            
        if started_2022:
            total_funding += amount
            matched_projects.append(project_name)

print("__RESULT__:")
print(json.dumps({"projects": matched_projects, "total": total_funding}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json'}

exec(code, env_args)

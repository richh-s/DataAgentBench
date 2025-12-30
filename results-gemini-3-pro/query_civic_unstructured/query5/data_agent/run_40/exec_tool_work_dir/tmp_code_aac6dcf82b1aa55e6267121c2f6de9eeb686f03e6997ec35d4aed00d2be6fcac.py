code = """import json
import re

with open(locals()['var_function-call-5820662165936257699'], 'r') as f:
    docs = json.load(f)
with open(locals()['var_function-call-3158343219585157662'], 'r') as f:
    funding = json.load(f)

# Normalize Funding Names
project_data = {}

def normalize(s):
    # Remove (...) containing FEMA, CalOES, CalJPIA
    s = re.sub(r'\s*\([^)]*(FEMA|CalOES|CalJPIA)[^)]*\)', '', s, flags=re.IGNORECASE)
    return " ".join(s.split())

for record in funding:
    name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    
    base_name = normalize(name)
    # Check if original name had disaster indications that regex removed
    # or if regex didn't change it but it had them?
    # Actually, simply checking if suffix was present in original
    is_disaster_db = (base_name != " ".join(name.split())) 
    
    if base_name not in project_data:
        project_data[base_name] = {'amounts': [], 'is_disaster_db': False}
    
    project_data[base_name]['amounts'].append(amount)
    if is_disaster_db:
        project_data[base_name]['is_disaster_db'] = True

# Scanning Text
found_projects = {} 

for doc in docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_project = None
    current_section_is_disaster = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Detect Header
        if "Disaster Recovery Projects" in line:
            current_section_is_disaster = True
            current_project = None
            continue
        if "Capital Improvement Projects" in line:
            current_section_is_disaster = False
            current_project = None
            continue
            
        # Detect Project Name
        # Normalize text line too
        line_clean = normalize(line)
        
        matched = None
        for pname in project_data:
            if line_clean.lower() == pname.lower():
                matched = pname
                break
        
        if matched:
            current_project = matched
            if current_project not in found_projects:
                found_projects[current_project] = {'started_2022': False, 'is_disaster_header': False}
            
            if current_section_is_disaster:
                found_projects[current_project]['is_disaster_header'] = True
            continue
        
        # Analyze Project Content
        if current_project:
            # Check Start Date
            if re.search(r"(Begin|Start)\s+(Construction|Work|Design|Project)?.*2022", line, re.IGNORECASE):
                found_projects[current_project]['started_2022'] = True

# Calculate Total
total_funding = 0
qualified_projects = []

for name, info in found_projects.items():
    p_data = project_data[name]
    is_disaster = p_data['is_disaster_db'] or info['is_disaster_header']
    started_2022 = info['started_2022']
    
    if is_disaster and started_2022:
        total = sum(p_data['amounts'])
        total_funding += total
        qualified_projects.append({'name': name, 'amount': total})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'projects': qualified_projects}))"""

env_args = {'var_function-call-11109060141973558233': 'file_storage/function-call-11109060141973558233.json', 'var_function-call-6297926792442028306': ['Funding'], 'var_function-call-3158343219585157662': 'file_storage/function-call-3158343219585157662.json', 'var_function-call-5820662165936257699': 'file_storage/function-call-5820662165936257699.json', 'var_function-call-2253573425082995640': {'total_funding': 253000, 'projects': [{'name': '2021 Annual Street Maintenance', 'amount': 24000}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': 44000}, {'name': 'Malibu Park Drainage Improvements', 'amount': 17000}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000}]}, 'var_function-call-10458114493715273550': {'total_funding': 168000, 'projects': [{'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000}]}, 'var_function-call-16165825527719341058': {'total_funding': 168000, 'projects': [{'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000}]}}

exec(code, env_args)

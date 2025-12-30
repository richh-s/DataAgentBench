code = """import json
import re

# Load files
with open(locals()['var_function-call-5820662165936257699'], 'r') as f:
    docs = json.load(f)
with open(locals()['var_function-call-3158343219585157662'], 'r') as f:
    funding = json.load(f)

# Normalize Funding Names
project_data = {}
disaster_suffixes = ["(FEMA Project)", "(CalOES Project)", "(CalJPIA Project)", "(FEMA/CalOES Project)", "(FEMA)", "(CalOES)"]

for record in funding:
    name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    
    base_name = name
    is_disaster_db = False
    
    for suffix in disaster_suffixes:
        if suffix in name:
            is_disaster_db = True
            base_name = name.replace(suffix, "").strip()
            break
            
    base_name = " ".join(base_name.split())
    
    if base_name not in project_data:
        project_data[base_name] = {'amounts': [], 'is_disaster_db': False}
    
    project_data[base_name]['amounts'].append(amount)
    if is_disaster_db:
        project_data[base_name]['is_disaster_db'] = True

# Scanning Text
found_projects = {} 
disaster_keywords = ["FEMA", "CalOES", "Disaster", "Woolsey Fire", "Emergency"]

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
        line_clean = " ".join(line.split())
        matched = None
        for pname in project_data:
            if line_clean.lower() == pname.lower():
                matched = pname
                break
        
        if matched:
            current_project = matched
            if current_project not in found_projects:
                found_projects[current_project] = {'started_2022': False, 'is_disaster_text': False}
            
            if current_section_is_disaster:
                found_projects[current_project]['is_disaster_text'] = True
            continue
        
        # Analyze Project Content
        if current_project:
            # Check keywords
            for kw in disaster_keywords:
                if kw in line:
                    found_projects[current_project]['is_disaster_text'] = True
            
            # Check Start Date
            # Broad regex for start date
            if re.search(r"(Begin|Start)\s+(Construction|Work|Design|Project)?.*2022", line, re.IGNORECASE):
                found_projects[current_project]['started_2022'] = True

# Calculate Total
total_funding = 0
qualified_projects = []

for name, info in found_projects.items():
    p_data = project_data[name]
    is_disaster = p_data['is_disaster_db'] or info['is_disaster_text']
    started_2022 = info['started_2022']
    
    if is_disaster and started_2022:
        total = sum(p_data['amounts'])
        total_funding += total
        qualified_projects.append({'name': name, 'amount': total})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'projects': qualified_projects}))"""

env_args = {'var_function-call-11109060141973558233': 'file_storage/function-call-11109060141973558233.json', 'var_function-call-6297926792442028306': ['Funding'], 'var_function-call-3158343219585157662': 'file_storage/function-call-3158343219585157662.json', 'var_function-call-5820662165936257699': 'file_storage/function-call-5820662165936257699.json'}

exec(code, env_args)

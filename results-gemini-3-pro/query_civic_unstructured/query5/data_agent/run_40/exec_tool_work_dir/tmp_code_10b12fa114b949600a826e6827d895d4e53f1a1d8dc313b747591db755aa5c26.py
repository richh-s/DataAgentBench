code = """import json
import re

# Load data
with open(locals()['var_function-call-5820662165936257699'], 'r') as f:
    docs = json.load(f)
with open(locals()['var_function-call-3158343219585157662'], 'r') as f:
    funding = json.load(f)

# Normalize and Map Funding
# Structure: base_name -> {'amounts': [], 'is_disaster_db': False}
project_data = {}
disaster_suffixes = ["(FEMA Project)", "(CalOES Project)", "(CalJPIA Project)", "(FEMA/CalOES Project)", "(FEMA)", "(CalOES)"]

for record in funding:
    name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    
    # Determine base name and disaster status from DB name
    base_name = name
    is_disaster_db = False
    
    for suffix in disaster_suffixes:
        if suffix in name:
            is_disaster_db = True
            base_name = name.replace(suffix, "").strip()
            break
            
    # Clean base name (remove extra spaces)
    base_name = " ".join(base_name.split())
    
    if base_name not in project_data:
        project_data[base_name] = {'amounts': [], 'is_disaster_db': False}
    
    project_data[base_name]['amounts'].append(amount)
    if is_disaster_db:
        project_data[base_name]['is_disaster_db'] = True

# Helper to find projects in text
# We scan lines. If a line matches a base_name, we start capturing context until next project or section.
found_projects = {} # base_name -> {'started_2022': Bool, 'is_disaster_text': Bool}

# Keywords
disaster_keywords = ["FEMA", "CalOES", "Disaster", "Woolsey Fire", "Emergency"]

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_section_header = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a section header (heuristic: Capital Projects or Disaster Projects)
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            current_section_header = line
            current_project = None
            continue
            
        # Check if line is a project name
        # We check against project_data keys
        # Use exact match (case insensitive)
        line_clean = " ".join(line.split())
        
        # Check for match
        # To avoid false positives, maybe length > 5?
        matched_name = None
        for name in project_data:
            if line_clean.lower() == name.lower():
                matched_name = name
                break
        
        if matched_name:
            current_project = matched_name
            if current_project not in found_projects:
                found_projects[current_project] = {'started_2022': False, 'is_disaster_text': False}
            
            # Check if current section header implies disaster
            if "Disaster Recovery Projects" in current_section_header:
                found_projects[current_project]['is_disaster_text'] = True
            
            continue
            
        # If we are inside a project section, analyze content
        if current_project:
            # Check for disaster keywords
            for kw in disaster_keywords:
                if kw in line:
                    found_projects[current_project]['is_disaster_text'] = True
            
            # Check for start date
            # Patterns: "Begin Construction: <Date>", "Start Date: <Date>"
            # We look for "2022" in such lines.
            if "Begin Construction" in line or "Start Date" in line:
                if "2022" in line:
                    found_projects[current_project]['started_2022'] = True

# Calculate Total Funding
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

code = """import json
import sqlite3
import re

# Load funding data
funding_file = locals()['var_function-call-10486156171359470717']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
docs_file = locals()['var_function-call-11751913869658535097']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = "\n".join([d['text'] for d in civic_docs])

# Define statuses and sections
sections = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started"
}

def clean_name(name):
    # Regex without backslashes: space* ( ... )$
    return re.sub(r'[ \t]*[(].*?[)]$', '', name).strip()

project_funding_map = {}
for record in funding_data:
    full_name = record['Project_Name']
    base_name = clean_name(full_name)
    if base_name not in project_funding_map:
        project_funding_map[base_name] = []
    project_funding_map[base_name].append(record)

section_positions = []
for header, status in sections.items():
    pattern = re.escape(header)
    for match in re.finditer(pattern, full_text, re.IGNORECASE):
        section_positions.append({'start': match.start(), 'name': header, 'status': status})

section_positions.sort(key=lambda x: x['start'])
section_positions.append({'start': len(full_text), 'name': 'END', 'status': None})

results = []
all_base_names = list(project_funding_map.keys())
all_base_names.sort(key=len, reverse=True)

for i in range(len(section_positions) - 1):
    section = section_positions[i]
    next_section = section_positions[i+1]
    
    section_text = full_text[section['start']:next_section['start']]
    section_status = section['status']
    
    matches = []
    for base_name in all_base_names:
        idx = section_text.find(base_name)
        if idx != -1:
            matches.append({'name': base_name, 'start': idx})
            
    # Sort matches by Start ASC, then Length DESC
    matches.sort(key=lambda x: (x['start'], -len(x['name'])))
    
    valid_matches = []
    last_end = -1
    for m in matches:
        if m['start'] >= last_end:
            valid_matches.append(m)
            last_end = m['start'] + len(m['name'])
    
    for k in range(len(valid_matches)):
        match = valid_matches[k]
        start = match['start']
        end_of_block = valid_matches[k+1]['start'] if k+1 < len(valid_matches) else len(section_text)
        block_text = section_text[start:end_of_block]
        
        status = section_status
        if status == "construction":
            lower_block = block_text.lower()
            if "construction was completed" in lower_block or "notice of completion" in lower_block:
                status = "completed"
        
        keywords = ['emergency', 'fema', 'fire', 'disaster']
        is_relevant_text = any(kw in block_text.lower() for kw in keywords)
        
        base_name = match['name']
        funding_records = project_funding_map.get(base_name, [])
        
        for record in funding_records:
            full_name = record['Project_Name']
            is_relevant_name = any(kw in full_name.lower() for kw in keywords)
            
            if is_relevant_text or is_relevant_name:
                results.append({
                    "Project Name": full_name,
                    "Funding Source": record['Funding_Source'],
                    "Amount": record['Amount'],
                    "Status": status
                })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8394565906188942673': 'file_storage/function-call-8394565906188942673.json', 'var_function-call-10486156171359470717': 'file_storage/function-call-10486156171359470717.json', 'var_function-call-11751913869658535097': 'file_storage/function-call-11751913869658535097.json'}

exec(code, env_args)

code = """import json
import re

# Load data
funding_path = locals()['var_function-call-15640139870961926103']
civic_path = locals()['var_function-call-15640139870961922644']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

funding_map = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

extracted_projects = []

def parse_document_detailed(text):
    lines = text.splitlines()
    projects = []
    
    current_project = None
    current_text = []
    
    header_pattern = r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*(?:\((.*)\))?'
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if re.match(header_pattern, line, re.IGNORECASE):
            if current_project:
                projects.append({'name': current_project, 'text': "\n".join(current_text)})
            current_project = None
            current_text = []
            i += 1
            continue
            
        is_project_start = False
        for offset in range(1, 6):
            if i + offset >= len(lines): break
            next_l = lines[i+offset].strip()
            if ("Updates:" in next_l or "Project Description:" in next_l or "Project Schedule:" in next_l) and ("Updates:" not in line):
                is_project_start = True
                break
        
        if is_project_start:
            if current_project:
                 projects.append({'name': current_project, 'text': "\n".join(current_text)})
            current_project = line
            current_text = []
            i += 1
        else:
            if current_project:
                current_text.append(line)
            i += 1
            
    if current_project:
        projects.append({'name': current_project, 'text': "\n".join(current_text)})
        
    return projects

all_projects = []
for doc in civic_data:
    all_projects.extend(parse_document_detailed(doc['text']))

matches = []
for p in all_projects:
    text = p['text']
    name = p['name']
    
    # Use \\n for newline in replace
    text_normalized = text.replace('\\n', ' ')
    
    if re.search(r'Begin Construction:.*2022', text_normalized, re.IGNORECASE):
        matches.append(name)
        continue
        
    if re.search(r'Design.*(commence|begin|start).*2022', text_normalized, re.IGNORECASE):
        matches.append(name)
        continue
        
    if re.search(r'Advertis.*2022', text_normalized, re.IGNORECASE):
        matches.append(name)
        continue
        
    if re.search(r'Kickoff.*2022', text_normalized, re.IGNORECASE):
        matches.append(name)
        continue

    if re.search(r'construction beginning in.*2022', text_normalized, re.IGNORECASE):
        matches.append(name)
        continue

disaster_matches = []
for name in matches:
    if "FEMA" in name or "CalOES" in name or "CalJPIA" in name or "Woolsey" in name:
        disaster_matches.append(name)

disaster_matches = list(set(disaster_matches))

total = 0
found = []
not_found = []

for name in disaster_matches:
    clean_name = name.strip()
    if clean_name in funding_map:
        total += funding_map[clean_name]
        found.append(clean_name)
    else:
        not_found.append(clean_name)

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "found_projects": found,
    "not_found": not_found
}))"""

env_args = {'var_function-call-15640139870961926103': 'file_storage/function-call-15640139870961926103.json', 'var_function-call-15640139870961922644': 'file_storage/function-call-15640139870961922644.json', 'var_function-call-4280233803932826645': {'total_funding': 91000.0, 'matched_projects': [{'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000.0}], 'missing_projects': []}, 'var_function-call-15849578272413360394': 'file_storage/function-call-15849578272413360394.json', 'var_function-call-2056573886096391775': [{'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'mentions': [' It is anticipated that the final design will be complete by February 2022', ' The project will be advertised for construction bids with construction beginning in April 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design will commence during the Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Storm Drain Master Plan (FEMA Project)', 'mentions': [' (cid:190) Estimated Schedule: (cid:131) Completion Date: Spring 2022 Page 6 of 6 Agenda Item # 4']}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'mentions': [' (cid:190) Project Schedule (cid:131) Complete Design: April 2022 (cid:131) Advertise: Spring 2022 (cid:131) Begin Construction: Spring 2022 Page 5 of 8 Agenda Item # 4']}, {'name': 'damaged by the Woolsey Fire.', 'mentions': [' It is anticipated that the final design will be complete by March 2022', ' project will be advertised for construction bids with construction beginning in Spring 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design has begun and preliminary design should be completed by Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'mentions': [' (cid:131) The Kickoff meeting for the Steering Committee was held on March 17, 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'mentions': [' The project was accepted by the Council on January 24, 2022 in Page 8 of 8 Agenda Item # 4']}]}

exec(code, env_args)

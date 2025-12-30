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

def get_projects(text):
    lines = text.splitlines()
    found_projects = []
    
    current_section = "Unknown"
    
    # Heuristic: Store the last seen "Project Name candidate"
    # A candidate is a line that looks like a name.
    # When we hit a "Start 2022" line, the last candidate is the project.
    
    last_candidate = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check Section
        if re.match(r'^(Capital Improvement Projects|Disaster Recovery Projects)', line, re.IGNORECASE):
            current_section = line
            last_candidate = None
            continue
            
        # Check date match
        is_start_2022 = False
        if "2022" in line:
            # Check keywords
            if re.search(r'Begin Construction', line, re.IGNORECASE): is_start_2022 = True
            elif re.search(r'Design.*(commence|begin|start)', line, re.IGNORECASE): is_start_2022 = True
            elif re.search(r'Advertis', line, re.IGNORECASE): is_start_2022 = True
            elif re.search(r'Kickoff', line, re.IGNORECASE): is_start_2022 = True
            elif re.search(r'construction beginning', line, re.IGNORECASE): is_start_2022 = True
            
        if is_start_2022 and last_candidate:
            # We found a start date for the last candidate
            p_type = "capital"
            if "disaster" in current_section.lower():
                p_type = "disaster"
            
            # Check name suffixes
            name = last_candidate
            if "FEMA" in name or "CalOES" in name or "CalJPIA" in name or "Woolsey" in name:
                p_type = "disaster"
            
            found_projects.append({
                'name': name,
                'type': p_type,
                'line': line
            })
            continue

        # Determine if this line is a potential project name
        # It shouldn't be a keyword line
        if "Updates:" in line or "Project Description:" in line or "Project Schedule:" in line or "(cid:" in line:
            continue
        # Also skip small noise
        if len(line) < 5: continue
        # Skip date lines or page numbers
        if "Page" in line and "Agenda" in line: continue
        
        # Otherwise, assume it's a name
        last_candidate = line

    return found_projects

all_candidates = []
for doc in civic_data:
    all_candidates.extend(get_projects(doc['text']))

# Filter Disaster
disaster_projects = [p for p in all_candidates if p['type'] == 'disaster']

# Deduplicate by name
unique_disaster = {}
for p in disaster_projects:
    unique_disaster[p['name']] = p

# Match Funding
total = 0
matched = []
missing = []

for name, p in unique_disaster.items():
    if name in funding_map:
        total += funding_map[name]
        matched.append(name)
    else:
        missing.append(name)

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "matched": matched,
    "missing": missing,
    "details": list(unique_disaster.values())
}))"""

env_args = {'var_function-call-15640139870961926103': 'file_storage/function-call-15640139870961926103.json', 'var_function-call-15640139870961922644': 'file_storage/function-call-15640139870961922644.json', 'var_function-call-4280233803932826645': {'total_funding': 91000.0, 'matched_projects': [{'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000.0}], 'missing_projects': []}, 'var_function-call-15849578272413360394': 'file_storage/function-call-15849578272413360394.json', 'var_function-call-2056573886096391775': [{'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'mentions': [' It is anticipated that the final design will be complete by February 2022', ' The project will be advertised for construction bids with construction beginning in April 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design will commence during the Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Storm Drain Master Plan (FEMA Project)', 'mentions': [' (cid:190) Estimated Schedule: (cid:131) Completion Date: Spring 2022 Page 6 of 6 Agenda Item # 4']}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'mentions': [' (cid:190) Project Schedule (cid:131) Complete Design: April 2022 (cid:131) Advertise: Spring 2022 (cid:131) Begin Construction: Spring 2022 Page 5 of 8 Agenda Item # 4']}, {'name': 'damaged by the Woolsey Fire.', 'mentions': [' It is anticipated that the final design will be complete by March 2022', ' project will be advertised for construction bids with construction beginning in Spring 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design has begun and preliminary design should be completed by Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'mentions': [' (cid:131) The Kickoff meeting for the Steering Committee was held on March 17, 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'mentions': [' The project was accepted by the Council on January 24, 2022 in Page 8 of 8 Agenda Item # 4']}], 'var_function-call-2641073418365439178': {'total': 0, 'found_projects': [], 'not_found': []}, 'var_function-call-3790710361129771328': ['(cid:190) Updates: Construction was completed November 2022. Notice of completion', '(cid:131) Construction was completed, November 2022', '(cid:131) Construction was completed, November 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', '(cid:131) Begin Construction: Summer/Winter 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) Begin Construction: March 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}

exec(code, env_args)

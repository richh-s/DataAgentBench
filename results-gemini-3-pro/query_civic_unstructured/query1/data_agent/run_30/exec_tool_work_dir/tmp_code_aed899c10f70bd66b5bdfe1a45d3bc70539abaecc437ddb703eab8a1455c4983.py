code = """import json

funding_key = 'var_function-call-3513875169581502759'
civic_key = 'var_function-call-3513875169581504334'

with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)

funding_map = {}
for record in funding_data:
    name = record['Project_Name'].strip()
    try:
        amount = float(record['Amount'])
    except:
        amount = 0.0
    if name not in funding_map:
        funding_map[name] = 0.0
    funding_map[name] += amount

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_section = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Section Transitions
        if "Capital Improvement Projects (Design)" in line:
            current_section = "DESIGN"
            i += 1
            continue
        
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Capital Improvement Projects (Completed)" in line or \
           "Disaster Recovery Projects" in line:
            current_section = None
            # Do not continue immediately, as this line is just a header switch.
            # But we increment i at loop end.
        
        if current_section == "DESIGN":
            if not line:
                i += 1
                continue
            
            # Skip noise
            if line.startswith("Page ") or "Agenda Item" in line:
                i += 1
                continue
            if "(cid:" in line:
                i += 1
                continue
            if "Updates:" in line or "Project Schedule:" in line:
                i += 1
                continue
            
            # Look ahead logic
            is_valid = False
            for offset in range(1, 10): # Look slightly further
                if i + offset >= len(lines):
                    break
                nxt = lines[i+offset].strip()
                if not nxt:
                    continue
                if "(cid:" in nxt:
                    # Valid if it has Updates, Description, Project, Schedule
                    # Also "Status" or "Work" maybe?
                    # Sticking to the most common ones seen in preview
                    lower_nxt = nxt.lower()
                    if "updates" in lower_nxt or "description" in lower_nxt or "project" in lower_nxt or "schedule" in lower_nxt:
                        is_valid = True
                    break
                else:
                    # Hit text before bullet
                    if "Agenda Item" in nxt or "Page " in nxt:
                        continue
                    break # Another text line implies current line wasn't the header for the bullet
            
            if is_valid:
                capital_design_projects.add(line)
        
        i += 1

count = 0
matches = []
for proj in capital_design_projects:
    if proj in funding_map:
        if funding_map[proj] > 50000:
            count += 1
            matches.append(proj)

print("__RESULT__:")
print(json.dumps({"count": count, "matches": sorted(matches)}))"""

env_args = {'var_function-call-3513875169581502759': 'file_storage/function-call-3513875169581502759.json', 'var_function-call-3513875169581504334': 'file_storage/function-call-3513875169581504334.json', 'var_function-call-9967115425159319167': {'count': 10, 'matches': ['Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs', 'Outdoor Warning Signs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH at Trancas Canyon Road Right Turn Lane', 'PCH Median Improvements Project', 'Civic Center Stormwater Diversion Structure'], 'extracted': ["Council's direction.", 'scheduled for the April 11, 2022 Council meeting.', 'management.', 'to review', 'Malibu Canyon Road Traffic Study', 'amenities such as trash cans, benches, tables, and restrooms.', 'Trancas Canyon Park Playground', 'Clover Heights Storm Drainage Improvements', 'agreement will be sent to City Council in March.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Signal Synchronization System Improvements Project', 'feasible traffic safety improvements can be constructed at this location.', 'construction bids.', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'to finalize plans and specifications', 'Latigo Canyon Road Retaining Wall Repair Project', 'the Spring 2023.', 'Malibu Bluffs Park South Walkway Repairs', 'management services was approved by Council on March 14, 2022.', 'project and will submit to the County for review.', 'Civic Center Water Treatment Facility Phase 2', 'Malibu Park Drainage Improvements', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Metro.', 'Outdoor Warning Signs', 'review by the Council.', 'Permanent Skate Park', 'the agreement.', 'Storm Drain Master Plan', 'bidding.', 'overall project costs.', 'PCH at Trancas Canyon Road Right Turn Lane', 'Bluffs Park Shade Structure', 'property owners.', 'Westward Beach Road Improvements Project', 'shade structures at Malibu Bluffs Park.', 'or phasing out the project', 'the County and will be finalizing the design.', 'will begin in conjunction with the PCH Median Improvement', 'March 2022', 'project', 'advertised for construction bids shortly after this date.', 'PCH Median Improvements Project', 'sending this project out to bid during the Spring of 2022.', 'Civic Center Stormwater Diversion Structure', 'Marie Canyon Green Streets', 'cleared the project.', 'assessment district will be created.']}, 'var_function-call-18370033897855845366': ['upcoming Capital Improvement Projects and Disaster Recovery Projects.', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Completed)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects and Disaster Recovery Projects Status']}

exec(code, env_args)

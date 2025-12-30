code = """import json

# Load funding results
with open(locals()['var_function-call-2752695128907644383'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-10485844614487521069'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding for > 50,000
funded_projects = {}
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        pass

design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.splitlines()
    in_section = False
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        if "Capital Improvement Projects (Design)" in line:
            in_section = True
            continue
            
        if in_section:
            if "Capital Improvement Projects (" in line and "Design" not in line:
                in_section = False
            if "Disaster Recovery Projects" in line:
                in_section = False
            if line.startswith("Capital Improvement Projects") and "Design" not in line:
                 in_section = False
            if "Public Works Commission" in line:
                 in_section = False

            if not in_section:
                continue
                
            # Extraction logic
            is_project = False
            lookahead_count = 0
            for j in range(i + 1, len(lines)):
                next_l = lines[j].strip()
                if not next_l:
                    continue
                lookahead_count += 1
                if lookahead_count > 3:
                    break
                
                if "Updates:" in next_l or "Project Description:" in next_l or "Project Updates:" in next_l:
                    is_project = True
                    break
                if "(cid:190)" in next_l:
                     if "Updates" in next_l or "Project Description" in next_l:
                         is_project = True
                     break
            
            if is_project:
                p_name = line
                # Filter out garbage
                if len(p_name) > 3 and "Page " not in p_name and "Agenda Item" not in p_name and not p_name.startswith("(cid:131)"):
                    design_projects.add(p_name)

# Matching logic
matches = set()
matched_extracted = set()
matched_funding_keys = set()
normalized_funding = {k.lower(): k for k in funded_projects.keys()}

for dp in design_projects:
    dp_norm = dp.lower()
    
    found = False
    # 1. Exact match or Substring
    for fname_norm, original_name in normalized_funding.items():
        if fname_norm == dp_norm or fname_norm in dp_norm or dp_norm in fname_norm:
            matches.add(original_name)
            matched_extracted.add(dp)
            matched_funding_keys.add(fname_norm)
            found = True
            # Keep looking? No, if we found a match for this extracted project, good.
            # But maybe one extracted project matches multiple funding entries? (Unlikely)
            # Or multiple extracted projects match the same funding entry? (Possible)
            break
            
unmatched_extracted = list(design_projects - matched_extracted)
# Get unmatched funding > 50k
unmatched_funding = [v for k, v in normalized_funding.items() if k not in matched_funding_keys]

print("__RESULT__:")
print(json.dumps({
    "count": len(matches), 
    "matches": sorted(list(matches)), 
    "unmatched_extracted": sorted(unmatched_extracted),
    "unmatched_funding_count": len(unmatched_funding)
}))"""

env_args = {'var_function-call-2752695128907644383': 'file_storage/function-call-2752695128907644383.json', 'var_function-call-2752695128907641442': 'file_storage/function-call-2752695128907641442.json', 'var_function-call-10485844614487521069': 'file_storage/function-call-10485844614487521069.json', 'var_function-call-5225985024774178468': {'count': 1, 'matches': ['Trancas Canyon Park Playground Resurfacing'], 'extracted_projects': ['Marie Canyon Green Streets', 'Trancas Canyon Park Playground']}, 'var_function-call-1470612970295318818': {'count': 11, 'matches': ['Civic Center Stormwater Diversion Structure', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Outdoor Warning Signs', 'PCH Median Improvements Project', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Storm Drain Master Plan', 'Trancas Canyon Park Playground Resurfacing', 'Westward Beach Road Drainage Improvements Project'], 'extracted_projects': ['(cid:131) Advertise: Spring 2023', '(cid:131) Complete Design: Fall 2023', '(cid:131) Begin Construction: To be determined', '(cid:131) Advertise: July 2021', '(cid:131) Award Contract and Begin Construction: Summer 2022', '(cid:131) Complete Design: Summer 2023', '(cid:131) Begin Construction: Spring 2023', 'Westward Beach Road Repair Project', 'Latigo Canyon Road Retaining Wall Repair Project', '2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH at Trancas Canyon Road Right Turn Lane', 'Trancas Canyon Park Playground', 'Bluffs Park Shade Structure', '(cid:131) Begin Construction: Summer/Winter 2022', '(cid:190) Project Description: This project consists of installing a new westbound right', 'Storm Drain Master Plan', '(cid:190) Project Description: This project will consist of a traffic study on Malibu', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Begin Construction: Winter 2024', 'shade structures at Malibu Bluffs Park.', '(cid:131) Begin Construction: Summer 2022', 'Malibu Canyon Road Traffic Study', '(cid:131) Complete Design: Spring 2021', 'Malibu Bluffs Park South Walkway Repairs', '(cid:131) Begin Construction: Spring/Summer 2022', 'PCH Signal Synchronization System Improvements Project', '(cid:131) Award Contract and Begin Construction: September 2021', '(cid:131) Begin Construction: April 2021', 'Westward Beach Road Improvements Project', 'Commission meeting for project direction due to concerns regarding', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'Clover Heights Storm Drainage Improvements', '(cid:131) Complete Design: December 2021', 'Outdoor Warning Signs', 'Marie Canyon Green Streets', '(cid:131) Begin Construction: Estimated Summer 2021', '(cid:131) Complete Design: Spring 2022', 'Westward Beach Road Drainage Improvements Project', '(cid:131) Begin Construction: March 2022', 'Civic Center Water Treatment Facility Phase 2', '(cid:190) Project Description: This project consists of the installation of four single-post', 'to Malibu Bluffs Park. The project would include parking and additional site', 'City will be issuing a RFQ/P for design services in the summer of 2023', '(cid:131) Complete Design: Spring 2023', '(cid:131) Advertise: Summer 2023', '(cid:131) Begin Construction: Fall 2022', 'permanent skate park located on the Crummer/Case Court parcel adjacent', '(cid:131) Advertise for Bidding: December 2022', 'sirens height and feedback from residents and the community.', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', '(cid:131) Advertise: Spring/Summer 2022', 'Permanent Skate Park', '(cid:131) Advertise: Fall 2023', '(cid:131) Complete Design: March 2022', '(cid:131) Complete Design: April 2021', 'feasible traffic safety improvements can be constructed at this location.', 'PCH Median Improvements Project', 'Resources review.', '(cid:131) Complete Design: February 2022', 'turn lane at the intersection of PCH and Trancas Canyon Road.', '(cid:131) Begin Construction: Summer 2023', '(cid:131) Begin Construction: Fall 2023', '(cid:131) Begin Construction: Spring 2022', 'Malibu Park Drainage Improvements', '(cid:131) Advertise: Summer 2022', 'Civic Center Stormwater Diversion Structure', '(cid:131) Begin Construction: Summer 2021', '(cid:131) Begin Construction: Fall 2021', 'amenities such as trash cans, benches, tables, and restrooms.', 'the County.', 'schedule will be developed upon the completion of the Cultural']}}

exec(code, env_args)

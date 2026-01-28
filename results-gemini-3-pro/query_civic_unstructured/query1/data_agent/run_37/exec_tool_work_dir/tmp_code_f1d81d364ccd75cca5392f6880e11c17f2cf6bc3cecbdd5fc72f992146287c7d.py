code = """import json

# Get file paths from local variables
funding_file_path = locals()['var_function-call-2838577088197188033']
civic_file_path = locals()['var_function-call-11182446621266237343']

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

high_funding_projects = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    high_funding_projects[name.lower()] = name

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

doc_text = civic_docs[0]['text']
lines = doc_text.splitlines()

design_header = "Capital Improvement Projects (Design)"
construction_header = "Capital Improvement Projects (Construction)"
not_started_header = "Capital Improvement Projects (Not Started)"

in_design = False
extracted_names = []

for line in lines:
    clean_line = line.strip()
    if not clean_line:
        continue
        
    if design_header in clean_line:
        in_design = True
        continue
    
    if construction_header in clean_line or not_started_header in clean_line:
        in_design = False
        break
        
    if in_design:
        lower_line = clean_line.lower()
        if clean_line.startswith("(cid:"): continue
        if clean_line.startswith("Updates:"): continue
        if clean_line.startswith("Project Schedule:"): continue
        if clean_line.startswith("Page "): continue
        if clean_line.startswith("Agenda Item"): continue
        if lower_line.startswith("prepared by"): continue
        if lower_line.startswith("approved by"): continue
        if lower_line.startswith("date prepared"): continue
        if lower_line.startswith("estimated schedule"): continue
        if "Complete Design" in clean_line: continue
        if "Advertise" in clean_line: continue
        if "Begin Construction" in clean_line: continue
        
        extracted_names.append(clean_line)

matched_pairs = []
matches_set = set()

for name in extracted_names:
    name_lower = name.lower()
    found = False
    
    # Try exact match first
    if name_lower in high_funding_projects:
        db_name = high_funding_projects[name_lower]
        matched_pairs.append((name, db_name))
        matches_set.add(db_name)
        found = True
    else:
        # Try containment
        for db_name_lower, db_name_original in high_funding_projects.items():
            if name_lower in db_name_lower or db_name_lower in name_lower:
                matched_pairs.append((name, db_name_original))
                matches_set.add(db_name_original)
                found = True
                break
    
print("__RESULT__:")
print(json.dumps({"count": len(matches_set), "pairs": matched_pairs}))"""

env_args = {'var_function-call-2838577088197188033': 'file_storage/function-call-2838577088197188033.json', 'var_function-call-2838577088197188526': 'file_storage/function-call-2838577088197188526.json', 'var_function-call-7878716980368608955': ['civic_docs'], 'var_function-call-11182446621266237343': 'file_storage/function-call-11182446621266237343.json', 'var_function-call-11192819882122169413': {'count': 12, 'matches': ['Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Bluffs Park South Walkway', 'Birdview Avenue Improvements (CalOES Project)', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Clover Heights Storm Drain', 'Storm Drain Master Plan', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'Outdoor Warning Signs', 'Trancas Canyon Park Playground Resurfacing'], 'unmatched': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'and rejected all bids due to a budget shortfall', 'or phasing out the project', 'Westward Beach Road Repair Project', 'comments mid-April. This project required their review since the project', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'cleared the project.', 'to finalize plans and specifications', 'been finalized and incorporated into GIS.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Resources review for the SRF funding application', 'schedule will be developed upon the completion of the Cultural', 'Resources review.', 'the Spring 2023.', 'Commission meeting for project direction due to concerns regarding', 'sirens height and feedback from residents and the community.', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'feasible traffic safety improvements can be constructed at this location.', 'City will be issuing a RFQ/P for design services in the summer of 2023']}}

exec(code, env_args)

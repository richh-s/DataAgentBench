code = """import json
import difflib

funding_path = locals()['var_function-call-7838865705427955035']
civic_path = locals()['var_function-call-5237099237942450066']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Funding map: Name -> Amount
funding_map = {}
for row in funding_data:
    try:
        funding_map[row['Project_Name'].strip()] = float(row['Amount'])
    except:
        pass

extracted_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    in_design = False
    buffer_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects (Design)" in line:
            in_design = True
            buffer_line = None
            continue
            
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            in_design = False
            continue
            
        if in_design:
            # Check for specific detail markers to confirm previous line was name
            if "(cid:190) Updates:" in line or "Updates:" in line or \
               "(cid:190) Project Description:" in line or "Project Description:" in line:
                if buffer_line:
                    extracted_projects.add(buffer_line)
                    buffer_line = None
            else:
                # Filter out obvious non-names
                if line.startswith("(cid:131)") or line.startswith("Page") or "Agenda Item" in line:
                    continue
                if line.startswith("Date prepared:") or line.startswith("Meeting date:"):
                    continue
                # Also filter out lines that start with (cid:190) but aren't Updates/Desc
                # (e.g. Project Schedule)
                if line.startswith("(cid:190)"):
                    continue
                    
                buffer_line = line

# Matching logic
count = 0
matched_projects = []

for proj in extracted_projects:
    amount = 0
    match_name = None
    
    # Exact match
    if proj in funding_map:
        amount = funding_map[proj]
        match_name = proj
    else:
        # Fuzzy match attempt
        # 1. Try removing "2022" prefix
        if proj.startswith("2022 "):
            sub = proj[5:]
            if sub in funding_map:
                amount = funding_map[sub]
                match_name = sub
        
        # 2. Try simple substring or difflib
        if not match_name:
            # Look for keys that share significant words
            # or use get_close_matches
            close = difflib.get_close_matches(proj, funding_map.keys(), n=1, cutoff=0.6)
            if close:
                # Check if it's a plausible match
                # e.g. "Clover Heights Storm Drainage Improvements" vs "Clover Heights Storm Drain"
                match_name = close[0]
                amount = funding_map[match_name]
    
    if match_name and amount > 50000:
        count += 1
        matched_projects.append((proj, match_name, amount))

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "matches": matched_projects,
    "extracted_total": len(extracted_projects)
}))"""

env_args = {'var_function-call-13459136201759015403': ['Funding'], 'var_function-call-13459136201759017542': ['civic_docs'], 'var_function-call-7838865705427955035': 'file_storage/function-call-7838865705427955035.json', 'var_function-call-7838865705427954030': 'file_storage/function-call-7838865705427954030.json', 'var_function-call-5237099237942450066': 'file_storage/function-call-5237099237942450066.json', 'var_function-call-15210746741909145379': {'matches': 10, 'projects': ['Civic Center Stormwater Diversion Structure', 'Storm Drain Master Plan', 'Permanent Skate Park', 'PCH Median Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Outdoor Warning Signs', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Malibu Bluffs Park South Walkway Repairs', 'PCH at Trancas Canyon Road Right Turn Lane']}, 'var_function-call-11996557301364829638': {'extracted_projects': ['Westward Beach Road Repair Project', 'project and will submit to the County for review.', 'PCH at Trancas Canyon Road Right Turn Lane', 'the Spring 2023.', 'Malibu Bluffs Park South Walkway Repairs', 'to review', 'cleared the project.', 'Westward Beach Road Improvements Project', 'amenities such as trash cans, benches, tables, and restrooms.', 'shade structures at Malibu Bluffs Park.', 'agreement will be sent to City Council in March.', 'PCH Median Improvements Project', 'Trancas Canyon Park Playground', 'project', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'PCH Signal Synchronization System Improvements Project', 'Permanent Skate Park', 'Latigo Canyon Road Retaining Wall Repair Project', 'Resources review for the SRF funding application', 'Clover Heights Storm Drainage Improvements', 'Civic Center Water Treatment Facility Phase 2', 'Storm Drain Master Plan', 'the County and will be finalizing the design.', 'sending this project out to bid during the Spring of 2022.', 'scheduled for the April 11, 2022 Council meeting.', 'Marie Canyon Green Streets', 'will begin in conjunction with the PCH Median Improvement', 'review by the Council.', 'feasible traffic safety improvements can be constructed at this location.', 'or phasing out the project', 'management.', 'management services was approved by Council on March 14, 2022.', '2022 Morning View Resurfacing & Storm Drain Improvements', "Council's direction.", 'Metro.', 'construction bids.', 'the agreement.', 'assessment district will be created.', 'Outdoor Warning Signs', 'evaluating the project costs.', 'Malibu Park Drainage Improvements', 'advertised for construction bids shortly after this date.', 'Westward Beach Road Drainage Improvements Project', 'March 2022', 'property owners.', 'bidding.', 'Bluffs Park Shade Structure', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'overall project costs.', 'Civic Center Stormwater Diversion Structure', 'Malibu Canyon Road Traffic Study', 'to finalize plans and specifications'], 'funding_samples': ['Civic Center Stormwater Diversion Structure ($64000.0)', 'Clover Heights Storm Drain ($53000.0)', 'Latigo Canyon Road Culvert Repairs ($57000.0)', 'Latigo Canyon Road Retaining Wall Repair Project ($97000.0)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project) ($91000.0)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project) ($78000.0)', 'PCH at Trancas Canyon Road Right Turn Lane ($90000.0)', 'Trancas Canyon Park Planting and Irrigation Repairs ($78000.0)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project) ($92000.0)', 'Trancas Canyon Park Playground Resurfacing ($65000.0)', 'Trancas Canyon Park Slope Stabilization Project ($68000.0)', 'Trancas Playground Resurfacing ($90000.0)', 'Westward Beach Road Drainage Improvements Project ($87000.0)', 'Westward Beach Road Shoulder Repairs (CalOES Project) ($77000.0)']}}

exec(code, env_args)

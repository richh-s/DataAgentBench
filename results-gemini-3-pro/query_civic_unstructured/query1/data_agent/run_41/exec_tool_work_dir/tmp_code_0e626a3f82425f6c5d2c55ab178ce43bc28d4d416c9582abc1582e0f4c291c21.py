code = """import json
import re

# Load funding data
with open(locals()['var_function-call-11382907056012316849'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-11382907056012318432'], 'r') as f:
    civic_docs = json.load(f)

# Get all funding keys > 50k
funded_high = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data if float(item['Amount']) > 50000}
all_funded = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

# Scan text for headers and extracting again carefully
capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    in_design = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check for headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            if "(Design)" in line:
                in_design = True
            else:
                in_design = False
            # print(f"Header found: {line} -> In Design: {in_design}")
        
        if in_design:
            # Check if this line is a project
            # Must be followed by (cid:190) Updates:
            # Let's peek
            j = i + 1
            has_update = False
            while j < len(lines):
                nl = lines[j].strip()
                if not nl:
                    j += 1
                    continue
                if "(cid:190) Updates:" in nl or "(cid:190) Project Description:" in nl:
                    has_update = True
                break
            
            if has_update:
                # Exclude lines that are headers themselves (if logic fails)
                if "Capital Improvement Projects" not in line:
                     capital_design_projects.add(line)

# Clean up extracted projects
# Some might be "turn lane..." which is text.
# The "turn lane" one in previous output: "turn lane at the intersection of PCH and Trancas Canyon Road."
# This is likely a continuation of a description?
# "PCH at Trancas Canyon Road Right Turn Lane" is the project.
# The "turn lane..." line might be text that happened to be followed by Updates?
# Or maybe I am misinterpreting.
# Let's filter by checking if it looks like a Title (mostly capitalized?).
# "turn lane at..." is lowercase.
# Project names are usually Title Case.

final_design_projects = []
for p in capital_design_projects:
    if p[0].islower():
        continue # skip lowercase starts
    if len(p) < 5:
        continue
    final_design_projects.append(p)

# Manual matching check
matches = set()
debug_unmatched = []

for proj in final_design_projects:
    # Exact
    if proj in funded_high:
        matches.append(proj)
        continue
    
    # Fuzzy
    matched_key = None
    # Check substring against ALL funded high
    for db_key in funded_high:
        # Check if one is substring of other
        # Remove year from proj
        clean_proj = re.sub(r'^\d{4}\s+', '', proj)
        
        # Check overlap
        if clean_proj == db_key:
            matched_key = db_key
        elif clean_proj in db_key and len(clean_proj) > 10:
            matched_key = db_key
        elif db_key in clean_proj and len(db_key) > 10:
            matched_key = db_key
            
        # Specific overrides
        if "Slope" in proj and "Slope" in db_key and "Trancas" in proj and "Trancas" in db_key:
            matched_key = db_key
        if "Westward Beach Road" in proj and "Repair" in proj and "Shoulder" in db_key:
            matched_key = db_key
        
        if matched_key:
            matches.add(matched_key)
            break
    
    if not matched_key:
        debug_unmatched.append(proj)

print("__RESULT__:")
print(json.dumps({
    "matches": list(matches),
    "count": len(matches),
    "unmatched": debug_unmatched
}))"""

env_args = {'var_function-call-11382907056012316849': 'file_storage/function-call-11382907056012316849.json', 'var_function-call-11382907056012318432': 'file_storage/function-call-11382907056012318432.json', 'var_function-call-9551194131001190579': {'extracted_projects': ['and rejected all bids due to a budget shortfall', 'Marie Canyon Green Streets', 'bidding.', 'management.', 'project and will submit to the County for review.', 'or phasing out the project', '2022 Morning View Resurfacing & Storm Drain Improvements', 'construction bids.', 'advertised for construction bids shortly after this date.', 'PCH Median Improvements Project'], 'matches': ['PCH Median Improvements Project'], 'match_count': 1, 'unmatched': ['Unmatched extracted: and rejected all bids due to a budget shortfall', 'Unmatched extracted: Marie Canyon Green Streets', 'Unmatched extracted: bidding.', 'Unmatched extracted: management.', 'Unmatched extracted: project and will submit to the County for review.', 'Unmatched extracted: or phasing out the project', 'Unmatched extracted: 2022 Morning View Resurfacing & Storm Drain Improvements', 'Unmatched extracted: construction bids.', 'Unmatched extracted: advertised for construction bids shortly after this date.']}, 'var_function-call-1287713992563794267': {'extracted': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'PCH at Trancas Canyon Road Right Turn Lane', 'shade structures at Malibu Bluffs Park.', 'Outdoor Warning Signs', 'Westward Beach Road Drainage Improvements Project', 'Storm Drain Master Plan', 'Westward Beach Road Improvements Project', 'PCH Median Improvements Project', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Bluffs Park Shade Structure', 'PCH Signal Synchronization System Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'amenities such as trash cans, benches, tables, and restrooms.', 'Malibu Park Drainage Improvements', 'Trancas Canyon Park Playground', 'Marie Canyon Green Streets', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Westward Beach Road Repair Project', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drainage Improvements'], 'matches': ['Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Westward Beach Road Drainage Improvements Project', 'Storm Drain Master Plan', 'Trancas Canyon Park Playground Resurfacing', 'Clover Heights Storm Drain', 'PCH Median Improvements Project', 'Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'Civic Center Stormwater Diversion Structure', 'Latigo Canyon Road Retaining Wall Repair Project', 'PCH at Trancas Canyon Road Right Turn Lane'], 'count': 12, 'unmatched': ['Unmatched: 2022 Morning View Resurfacing & Storm Drain Improvements', 'Unmatched: shade structures at Malibu Bluffs Park.', 'Unmatched: Westward Beach Road Improvements Project', 'Unmatched: Trancas Canyon Park Upper and Lower Slopes Repair', 'Unmatched: Bluffs Park Shade Structure', 'Unmatched: PCH Signal Synchronization System Improvements Project', 'Unmatched: Civic Center Water Treatment Facility Phase 2', 'Unmatched: amenities such as trash cans, benches, tables, and restrooms.', 'Unmatched: Malibu Park Drainage Improvements', 'Unmatched: Marie Canyon Green Streets', 'Unmatched: turn lane at the intersection of PCH and Trancas Canyon Road.', 'Unmatched: Westward Beach Road Repair Project']}}

exec(code, env_args)

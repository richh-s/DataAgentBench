code = """import json
import re

# Load Funding Data
path_funding = locals()['var_function-call-13808490642390448201']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

funded_projects = {}
for item in funding_data:
    amt = float(item['Amount'])
    if amt > 50000:
        funded_projects[item['Project_Name'].strip()] = amt

# Load Civic Docs
path_docs = locals()['var_function-call-4985696884690537041']
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Find latest document based on filename date (MMDDYYYY)
latest_date = 0
latest_docs = []

for doc in civic_docs:
    fname = doc['filename']
    # Extract 8 digits
    match = re.search(r'(\d{2})(\d{2})(\d{4})', fname)
    if match:
        month, day, year = match.groups()
        date_int = int(year + month + day)
        if date_int > latest_date:
            latest_date = date_int
            latest_docs = [doc]
        elif date_int == latest_date:
            latest_docs.append(doc)

# If no date found, use all (fallback)
if not latest_docs:
    latest_docs = civic_docs

extracted = []

for doc in latest_docs:
    text = doc['text']
    
    # 1. Isolate Design Section
    # Find "Capital Improvement Projects (Design)"
    marker = "Capital Improvement Projects (Design)"
    idx = text.find(marker)
    if idx == -1:
        continue
        
    start_search = idx + len(marker)
    
    # Find next section start
    end_idx = -1
    for stop_m in ["Capital Improvement Projects (Construction)", 
                   "Capital Improvement Projects (Not Started)", 
                   "Disaster Recovery Projects",
                   "Capital Improvement Projects (Completed)"]: # Added Completed just in case
        stop_i = text.find(stop_m, start_search)
        if stop_i != -1:
            if end_idx == -1 or stop_i < end_idx:
                end_idx = stop_i
    
    if end_idx == -1:
        subtext = text[start_search:]
    else:
        subtext = text[start_search:end_idx]
        
    lines = [l.strip() for l in subtext.splitlines() if l.strip()]
    
    # 2. Extract Lines
    for i in range(len(lines) - 1):
        curr = lines[i]
        nxt = lines[i+1]
        
        # Heuristics
        if "Page " in curr or "Agenda Item" in curr:
            continue
        
        # Identify Project Name line by lookahead
        if "Updates:" in nxt or "Project Schedule" in nxt or "(cid:" in nxt: # cid check for safety if Updates missing
             # Double check curr is not a bullet itself
             if not curr.startswith("(cid:") and not curr.startswith("Updates:"):
                 extracted.append(curr)

extracted = list(set(extracted))

# 3. Match with Funding
matches = set()
misses = []

for p in extracted:
    # Exact match
    if p in funded_projects:
        matches.add(p)
        continue
    
    # Substring match (Bidirectional)
    found = False
    for fp in funded_projects:
        # Check if fp is substring of p (e.g. "Clover Heights Storm Drain" in "Clover Heights Storm Drainage Improvements")
        # OR p is substring of fp (e.g. "Trancas Canyon Park Playground" in "Trancas Canyon Park Playground Resurfacing")
        if fp in p or p in fp:
            matches.add(fp)
            found = True
            # Don't break, find all potential matches? No, one is enough to count this extracted item.
            # But we record the FUNDED project name.
            break
            
    if not found:
        misses.append(p)

res = {
    "count": len(matches),
    "matches": list(matches),
    "misses": misses,
    "latest_date": latest_date,
    "extracted_count": len(extracted)
}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-13808490642390448090': ['Funding'], 'var_function-call-13808490642390448201': 'file_storage/function-call-13808490642390448201.json', 'var_function-call-13808490642390448312': 'file_storage/function-call-13808490642390448312.json', 'var_function-call-4985696884690537041': 'file_storage/function-call-4985696884690537041.json', 'var_function-call-3625127041230537600': {'count': 9, 'matches': ['Civic Center Stormwater Diversion Structure', 'Malibu Bluffs Park South Walkway Repairs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Outdoor Warning Signs', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Permanent Skate Park'], 'misses': ['assessment district will be created.', 'cleared the project.', 'management.', 'Westward Beach Road Improvements Project', 'bidding.', 'to finalize plans and specifications', "Council's direction.", '(cid:131) City working with consultant on the design of the shoulder repairs', 'to review', '(cid:131) Staff has submitted a request for Federal funding', 'Civic Center Water Treatment Facility Phase 2', 'Westward Beach Road Repair Project', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'management services was approved by Council on March 14, 2022.', 'project and will submit to the County for review.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'feasible traffic safety improvements can be constructed at this location.', 'property owners.', '(cid:131) Next public community meeting is scheduled for March 25th.', '(cid:131) Project is scheduled to go out to bid next week.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Trancas Canyon Park Playground', '(cid:131) Consultant is working on final design documents.', 'the County and will be finalizing the design.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Clover Heights Storm Drainage Improvements', 'shade structures at Malibu Bluffs Park.', 'will begin in conjunction with the PCH Median Improvement', 'advertised for construction bids shortly after this date.', 'construction bids.', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'amenities such as trash cans, benches, tables, and restrooms.', '(cid:131) Plans and specifications are being finalized by consultant', 'PCH Signal Synchronization System Improvements Project', 'Malibu Park Drainage Improvements', 'Marie Canyon Green Streets', 'the agreement.', 'project will begin in conjunction with the PCH Median Improvement', 'or phasing out the project', 'agreement will be sent to City Council in March.']}}

exec(code, env_args)

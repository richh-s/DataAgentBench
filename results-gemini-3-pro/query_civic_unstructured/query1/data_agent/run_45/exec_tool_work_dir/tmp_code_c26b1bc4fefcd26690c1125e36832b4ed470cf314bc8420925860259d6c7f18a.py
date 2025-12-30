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

# Find latest document
latest_date = 0
latest_docs = []
for doc in civic_docs:
    fname = doc['filename']
    match = re.search(r'(\d{2})(\d{2})(\d{4})', fname)
    if match:
        month, day, year = match.groups()
        date_int = int(year + month + day)
        if date_int > latest_date:
            latest_date = date_int
            latest_docs = [doc]
        elif date_int == latest_date:
            latest_docs.append(doc)
if not latest_docs:
    latest_docs = civic_docs

extracted = []
for doc in latest_docs:
    text = doc['text']
    marker = "Capital Improvement Projects (Design)"
    idx = text.find(marker)
    if idx == -1: continue
    start_search = idx + len(marker)
    
    end_idx = -1
    for stop_m in ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects", "Capital Improvement Projects (Completed)"]:
        stop_i = text.find(stop_m, start_search)
        if stop_i != -1:
            if end_idx == -1 or stop_i < end_idx:
                end_idx = stop_i
    
    if end_idx == -1: subtext = text[start_search:]
    else: subtext = text[start_search:end_idx]
        
    lines = [l.strip() for l in subtext.splitlines() if l.strip()]
    for i in range(len(lines) - 1):
        curr = lines[i]
        nxt = lines[i+1]
        if "Page " in curr or "Agenda Item" in curr: continue
        # Filter garbage
        if len(curr) < 5: continue
        if not (curr[0].isupper() or curr[0].isdigit()): continue
        
        if "Updates:" in nxt or "Project Schedule" in nxt or "(cid:" in nxt:
             if not curr.startswith("(cid:") and not curr.startswith("Updates:"):
                 extracted.append(curr)

extracted = list(set(extracted))

matches = set()
misses = []

def normalize(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

for p in extracted:
    p_norm = normalize(p)
    found = False
    for fp in funded_projects:
        fp_norm = normalize(fp)
        # Check containment
        if fp_norm in p_norm or p_norm in fp_norm:
            matches.add(fp)
            found = True
            break
    if not found:
        misses.append(p)

print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": list(matches), "misses": misses}))"""

env_args = {'var_function-call-13808490642390448090': ['Funding'], 'var_function-call-13808490642390448201': 'file_storage/function-call-13808490642390448201.json', 'var_function-call-13808490642390448312': 'file_storage/function-call-13808490642390448312.json', 'var_function-call-4985696884690537041': 'file_storage/function-call-4985696884690537041.json', 'var_function-call-3625127041230537600': {'count': 9, 'matches': ['Civic Center Stormwater Diversion Structure', 'Malibu Bluffs Park South Walkway Repairs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Outdoor Warning Signs', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Permanent Skate Park'], 'misses': ['assessment district will be created.', 'cleared the project.', 'management.', 'Westward Beach Road Improvements Project', 'bidding.', 'to finalize plans and specifications', "Council's direction.", '(cid:131) City working with consultant on the design of the shoulder repairs', 'to review', '(cid:131) Staff has submitted a request for Federal funding', 'Civic Center Water Treatment Facility Phase 2', 'Westward Beach Road Repair Project', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'management services was approved by Council on March 14, 2022.', 'project and will submit to the County for review.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'feasible traffic safety improvements can be constructed at this location.', 'property owners.', '(cid:131) Next public community meeting is scheduled for March 25th.', '(cid:131) Project is scheduled to go out to bid next week.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Trancas Canyon Park Playground', '(cid:131) Consultant is working on final design documents.', 'the County and will be finalizing the design.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Clover Heights Storm Drainage Improvements', 'shade structures at Malibu Bluffs Park.', 'will begin in conjunction with the PCH Median Improvement', 'advertised for construction bids shortly after this date.', 'construction bids.', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'amenities such as trash cans, benches, tables, and restrooms.', '(cid:131) Plans and specifications are being finalized by consultant', 'PCH Signal Synchronization System Improvements Project', 'Malibu Park Drainage Improvements', 'Marie Canyon Green Streets', 'the agreement.', 'project will begin in conjunction with the PCH Median Improvement', 'or phasing out the project', 'agreement will be sent to City Council in March.']}, 'var_function-call-12863113400310437927': {'count': 12, 'matches': ['Malibu Bluffs Park South Walkway Repairs', 'Outdoor Warning Signs', 'Trancas Canyon Park Playground Resurfacing', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Retaining Wall Repair Project', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Clover Heights Storm Drain', 'Malibu Canyon Road Traffic Study', 'project_471'], 'misses': ['Trancas Canyon Park Upper and Lower Slopes Repair', 'the Spring 2023.', 'and rejected all bids due to a budget shortfall', 'to finalize plans and specifications', 'been finalized and incorporated into GIS.', 'feasible traffic safety improvements can be constructed at this location.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'cleared the project.', 'Westward Beach Road Repair Project', 'project and will submit to the County for review.', 'Civic Center Water Treatment Facility Phase 2', 'Resources review for the SRF funding application', 'or phasing out the project'], 'latest_date': 20230322, 'extracted_count': 25}}

exec(code, env_args)

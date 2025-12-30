code = """import json

fund_key = 'var_function-call-1599065279211733274'
docs_key = 'var_function-call-1599065279211735013'

with open(locals()[fund_key], 'r') as f:
    funding = json.load(f)
with open(locals()[docs_key], 'r') as f:
    docs = json.load(f)

funded_map = {}
for x in funding:
    try:
        s = str(x.get('Amount', '0')).replace(',', '').replace('$', '')
        amt = float(s)
        nm = x.get('Project_Name', '').strip()
        funded_map[nm] = amt
    except:
        pass

projects = set()
marker = "Capital Improvement Projects (Design)"
next_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

for d in docs:
    txt = d.get('text', '')
    parts = txt.split(marker)
    if len(parts) < 2: continue
    relevant = parts[1]
    min_idx = len(relevant)
    for nm in next_markers:
        idx = relevant.find(nm)
        if idx != -1 and idx < min_idx:
            min_idx = idx
    section = relevant[:min_idx]
    
    lines = [l.strip() for l in section.splitlines() if l.strip()]
    for i in range(len(lines) - 1):
        line = lines[i]
        nxt = lines[i+1]
        is_name = False
        if "Updates:" in nxt or "Project Description:" in nxt or "Project Updates:" in nxt:
            is_name = True
        if is_name:
            if not line.startswith("(cid:") and "Page " not in line and "Agenda Item" not in line:
                projects.add(line)

matches = set()
debug_matches = []

# Exact and Fuzzy
for p in projects:
    # 1. Exact
    found = False
    for fn, amt in funded_map.items():
        if fn.lower() == p.lower():
            if amt > 50000:
                matches.add(fn)
                debug_matches.append(f"Exact: {fn} ({amt})")
            found = True
            break
    
    if found: continue

    # 2. Substring
    for fn, amt in funded_map.items():
        # Check if one contains the other substantially
        # e.g. "Clover Heights Storm Drain" vs "Clover Heights Storm Drainage Improvements"
        # Common prefix?
        if fn.lower() in p.lower() or p.lower() in fn.lower():
            # Check for significant overlap
            if len(fn) > 10 and len(p) > 10:
                if amt > 50000:
                    matches.add(fn)
                    debug_matches.append(f"Fuzzy: {fn} matches {p} ({amt})")
                found = True
                # Don't break immediately, might be better match?
                # But for counting, unique funding project is enough.
                break

print("__RESULT__:")
print(json.dumps({
    "count": len(matches),
    "matches": list(matches),
    "debug_matches": debug_matches
}))"""

env_args = {'var_function-call-1599065279211733274': 'file_storage/function-call-1599065279211733274.json', 'var_function-call-1599065279211735013': 'file_storage/function-call-1599065279211735013.json', 'var_function-call-3315802796629298163': {'count': 1, 'projects': ['PCH Median Improvements Project']}, 'var_function-call-16876239856465075778': {'count': 1, 'matches': ['PCH Median Improvements Project'], 'extracted_sample': ['(cid:131) Complete Design: March 2022', '(cid:131) Complete Design: April 2021', 'bidding.', 'PCH Median Improvements Project', '(cid:131) Advertise: Fall 2023', 'and rejected all bids due to a budget shortfall', 'management.', '(cid:131) Complete Design: February 2021', 'project and will submit to the County for review.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'construction bids.', 'advertised for construction bids shortly after this date.', 'or phasing out the project', '(cid:131) Complete Design: Summer 2023', '(cid:190) Project Schedule:', 'Marie Canyon Green Streets'], 'funded_skate': ['Permanent Skate Park'], 'extracted_skate': []}, 'var_function-call-14342943867378992175': {'count': 10, 'matches': ['PCH at Trancas Canyon Road Right Turn Lane', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs', 'Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'Storm Drain Master Plan', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Malibu Bluffs Park South Walkway Repairs', 'Latigo Canyon Road Retaining Wall Repair Project'], 'debug_log': ['Section len: 4875', 'Section len: 5147', 'Section len: 2643', 'Section len: 2764', 'Section len: 5691'], 'extracted': ['Trancas Canyon Park Upper and Lower Slopes Repair', 'PCH at Trancas Canyon Road Right Turn Lane', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs', 'PCH Signal Synchronization System Improvements Project', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Permanent Skate Park', 'Westward Beach Road Improvements Project', 'Malibu Canyon Road Traffic Study', 'Storm Drain Master Plan', 'Westward Beach Road Repair Project', 'shade structures at Malibu Bluffs Park.', 'Malibu Park Drainage Improvements', 'feasible traffic safety improvements can be constructed at this location.', 'Bluffs Park Shade Structure', 'Civic Center Water Treatment Facility Phase 2', 'Marie Canyon Green Streets', 'amenities such as trash cans, benches, tables, and restrooms.', 'Clover Heights Storm Drainage Improvements', 'Trancas Canyon Park Playground', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Malibu Bluffs Park South Walkway Repairs', 'Latigo Canyon Road Retaining Wall Repair Project']}}

exec(code, env_args)

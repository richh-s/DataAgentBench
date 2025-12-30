code = """import json
import re

c_path = locals()['var_function-call-2424790631309893722']
with open(c_path, "r") as f:
    docs = json.load(f)
f_path = locals()['var_function-call-2424790631309895007']
with open(f_path, "r") as f:
    funds = json.load(f)

projs = []
split_str = "(cid:190)"
nl_char = chr(10)
current_project = None

for d in docs:
    txt = d["text"]
    chunks = txt.split(split_str)
    
    for i in range(1, len(chunks)):
        chunk_curr = chunks[i].strip()
        chunk_prev = chunks[i-1].strip()
        
        is_new = False
        if chunk_curr.startswith("Updates:") or chunk_curr.startswith("Project Description:"):
            is_new = True
        
        if is_new:
            lines = chunk_prev.split(nl_char)
            name_candidates = []
            for line in reversed(lines):
                line = line.strip()
                if not line: continue
                if "Capital Improvement Projects" in line: continue
                if "Agenda Item" in line: continue
                if "Page" in line: continue
                if "Public Works" in line: continue
                if line.endswith(":"): line = line[:-1]
                name_candidates.append(line)
                if len(name_candidates) >= 2: break 
            
            # Logic: if first candidate (last line) looks incomplete (starts lowercase), prepend second
            final_name = None
            if name_candidates:
                first = name_candidates[0]
                if len(name_candidates) > 1 and first[0].islower():
                    final_name = name_candidates[1] + " " + first
                else:
                    final_name = first
            
            if final_name:
                current_project = final_name
        
        if current_project:
            pattern = "Begin Construction:[ \t]*(.*)"
            m = re.search(pattern, chunk_curr, re.IGNORECASE)
            if m:
                dt = m.group(1).strip()
                projs.append({"n": current_project, "d": dt})

# Filter
tn = []
sp = ["March", "April", "May", "Spring"]
target = "2022"

for p in projs:
    ds = p["d"]
    if target in ds:
        found = False
        for s in sp:
            if s.lower() in ds.lower():
                found = True
        if found:
            tn.append(p)

# Unique by name
unique_tn = {}
for p in tn:
    unique_tn[p["n"]] = p["d"]

# Match
total = 0
cnt = 0
matched_names = []
f_map = {}
for r in funds:
    n = r["Project_Name"].strip()
    a = int(r["Amount"])
    # Sum duplicates?
    if n in f_map:
        f_map[n] += a
    else:
        f_map[n] = a

# Funding keys for fuzzy match
f_keys = list(f_map.keys())

for name in unique_tn:
    # Exact match
    if name in f_map:
        total += f_map[name]
        cnt += 1
        matched_names.append(name)
        continue
    
    # Fuzzy
    # 1. Startswith
    matched = False
    for fn in f_keys:
        if fn.startswith(name) or name.startswith(fn):
            total += f_map[fn]
            cnt += 1
            matched_names.append(fn)
            matched = True
            break
    if matched: continue
    
    # 2. Token overlap (for shade structure)
    # "shade structures at Malibu Bluffs Park" vs "Bluffs Park Shade Structure"
    tokens_n = set(re.findall(r"\w+", name.lower()))
    
    best_match = None
    max_overlap = 0
    for fn in f_keys:
        tokens_f = set(re.findall(r"\w+", fn.lower()))
        overlap = len(tokens_n.intersection(tokens_f))
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = fn
            
    # Threshold? e.g. 3 words or 50%
    if best_match and max_overlap >= 3:
        # Check if reasonable
        # print(f"Fuzzy matching {name} to {best_match}")
        total += f_map[best_match]
        cnt += 1
        matched_names.append(best_match)
        matched = True
    
    if not matched:
        # Unmatched
        pass

print("__RESULT__:")
print(json.dumps({"count": cnt, "total_funding": total, "projects": matched_names}))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json', 'var_function-call-11236971759880299880': 'Check OK', 'var_function-call-17499494812927848584': {'count': 0, 'total_funding': 0, 'matched_projects': []}, 'var_function-call-17213884009062758480': [], 'var_function-call-12362529833978313360': [{'n': 'project and will submit to the County for review.', 'd': 'Fall 2023'}, {'n': 'or phasing out the project', 'd': 'Fall 2023'}, {'n': '(cid:131) City working with consultant on the design of the shoulder repairs', 'd': 'Fall 2023'}, {'n': 'cleared the project.', 'd': 'Fall 2023'}, {'n': 'to finalize plans and specifications', 'd': 'Fall 2023'}, {'n': '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'd': 'Summer 2023'}, {'n': '(cid:131) Plans and specifications are being finalized by consultant', 'd': 'Summer 2023'}, {'n': 'project', 'd': 'Winter 2024'}, {'n': 'the Spring 2023.', 'd': 'Fall 2023'}, {'n': 'Engineering, Inc.', 'd': 'April 2023'}, {'n': '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', 'd': 'Summer 2023'}, {'n': 'advertised for construction bids shortly after this date.', 'd': 'Spring 2022'}, {'n': 'agreement will be sent to City Council in March.', 'd': 'Spring/Summer 2022'}, {'n': 'PCH Signal Synchronization System Improvements Project', 'd': 'Spring/Summer 2022'}, {'n': 'to review', 'd': 'Summer/Winter 2022'}, {'n': 'property owners.', 'd': 'Fall 2022'}, {'n': 'sending this project out to bid during the Spring of 2022.', 'd': 'Spring 2022'}, {'n': 'review by the Council.', 'd': 'To be determined'}, {'n': 'is finalizing the bid documents.', 'd': 'Spring 2022'}, {'n': 'timber with non-combustible materials.', 'd': 'April 2022'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Spring 2022'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Spring 2022'}, {'n': 'beginning in April 2022.', 'd': 'April 2022'}, {'n': 'started and is anticipated to be completed by the Spring of 2022.', 'd': 'Fall 2022'}, {'n': 'beginning in Fall 2022.', 'd': 'Fall 2022'}, {'n': 'bidding.', 'd': 'Summer 2021'}, {'n': 'management.', 'd': 'Fall 2021'}, {'n': '(cid:131) Consultant is working on final design documents.', 'd': 'September 2021'}, {'n': 'the agreement.', 'd': 'Estimated Summer 2021'}, {'n': 'the County and will be finalizing the design.', 'd': 'Fall 2021'}, {'n': 'assessment district will be created.', 'd': 'March 2022'}, {'n': 'overall project costs.', 'd': 'Summer 2021'}, {'n': 'maintenance of City streets.', 'd': 'Summer 2021'}, {'n': 'post shade structures at Malibu Bluffs Park', 'd': 'Fall 2021'}, {'n': 'require a vehicle impact protection device.', 'd': 'Fall 2021'}, {'n': 'Road.', 'd': 'Winter 2021'}, {'n': '(cid:131) The project consultant has started the design of the project.', 'd': 'Fall 2021'}, {'n': 'timber with non-combustible materials.', 'd': 'Summer 2021'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Summer/Fall 2021'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Summer/Fall 2021'}, {'n': 'Drainage Improvements project.', 'd': 'Summer 2021'}, {'n': 'drain towards the end of Clover Heights will help eliminate this issue.', 'd': 'Summer 2022'}, {'n': 'that was damaged by the Woolsey Fire.', 'd': 'Spring 2022'}, {'n': 'Fire.', 'd': 'Spring 2022'}, {'n': 'bidding.', 'd': 'Summer 2021'}, {'n': 'management.', 'd': 'Fall 2021'}, {'n': '(cid:131) Consultant is working on final design documents.', 'd': 'September 2021'}, {'n': 'the agreement.', 'd': 'Estimated Summer 2021'}, {'n': 'the County and will be finalizing the design.', 'd': 'Fall 2021'}, {'n': '(cid:131) Next public community meeting is scheduled for March 25th.', 'd': 'March 2022'}, {'n': '(cid:131) Project is scheduled to go out to bid next week.', 'd': 'April 2021'}, {'n': 'maintenance of City streets.', 'd': 'Summer 2021'}, {'n': 'post shade structures at Malibu Bluffs Park', 'd': 'Fall 2021'}, {'n': 'require a vehicle impact protection device.', 'd': 'Fall 2021'}, {'n': 'Road.', 'd': 'Winter 2021'}, {'n': '(cid:131) The project consultant has started the design of the project.', 'd': 'Fall 2021'}, {'n': 'timber with non-combustible materials.', 'd': 'Summer 2021'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Summer/Fall 2021'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Summer/Fall 2021'}, {'n': 'Drainage Improvements project.', 'd': 'Summer 2021'}, {'n': 'drain towards the end of Clover Heights will help eliminate this issue.', 'd': 'Summer 2022'}, {'n': 'that was damaged by the Woolsey Fire.', 'd': 'Spring 2022'}, {'n': 'Fire.', 'd': 'Spring 2022'}, {'n': 'construction bids.', 'd': 'Summer 2022'}, {'n': 'management services was approved by Council on March 14, 2022.', 'd': 'Summer 2022'}, {'n': 'will begin in conjunction with the PCH Median Improvement', 'd': 'Summer 2022'}, {'n': "Council's direction.", 'd': 'Fall/Winter 2022'}, {'n': 'property owners.', 'd': 'Spring 2023'}, {'n': 'scheduled for the April 11, 2022 Council meeting.', 'd': 'Spring 2022'}, {'n': 'review by the Council.', 'd': 'To be determined'}, {'n': 'is finalizing the bid documents.', 'd': 'Summer 2022'}, {'n': 'timber with non-combustible materials.', 'd': 'Spring 2022'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Summer 2022'}, {'n': '(cid:131) The project consultant has started the design of this project.', 'd': 'Summer 2022'}, {'n': 'beginning in Spring 2022.', 'd': 'Spring 2022'}, {'n': 'of 2022.', 'd': 'Fall 2022'}, {'n': 'beginning in Fall 2022.', 'd': 'Fall 2022'}], 'var_function-call-17689966053437681354': {'count': 10, 'total_funding': 564000, 'matched': ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'PCH Median Improvements Project', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Civic Center Water Treatment Facility Phase 2', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'PCH Signal Synchronization System Improvements Project', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)'], 'unmatched': ['damaged by the Woolsey Fire.', 'shade structures at Malibu Bluffs Park.']}}

exec(code, env_args)

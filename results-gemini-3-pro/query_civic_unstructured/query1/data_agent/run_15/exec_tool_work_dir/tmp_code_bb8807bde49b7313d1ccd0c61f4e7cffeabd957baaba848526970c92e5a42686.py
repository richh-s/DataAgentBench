code = """import json

fund_key = 'var_function-call-1599065279211733274'
docs_key = 'var_function-call-1599065279211735013'

with open(locals()[fund_key], 'r') as f:
    funding = json.load(f)
with open(locals()[docs_key], 'r') as f:
    docs = json.load(f)

funded_norm = {}
for x in funding:
    try:
        s = str(x.get('Amount', '0')).replace(',', '').replace('$', '')
        if float(s) > 50000:
            nm = x.get('Project_Name', '').strip()
            funded_norm[nm.lower()] = nm
    except:
        pass

projects = set()
marker = "Capital Improvement Projects (Design)"
next_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

debug_log = []

for d in docs:
    txt = d.get('text', '')
    
    parts = txt.split(marker)
    if len(parts) < 2:
        continue
    
    relevant = parts[1]
    
    min_idx = len(relevant)
    for nm in next_markers:
        idx = relevant.find(nm)
        if idx != -1 and idx < min_idx:
            min_idx = idx
            
    section = relevant[:min_idx]
    debug_log.append(f"Section len: {len(section)}")
    
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

final_matches = []
for p in projects:
    if p.lower() in funded_norm:
        final_matches.append(funded_norm[p.lower()])

print("__RESULT__:")
print(json.dumps({
    "count": len(final_matches),
    "matches": final_matches,
    "debug_log": debug_log,
    "extracted": list(projects)
}))"""

env_args = {'var_function-call-1599065279211733274': 'file_storage/function-call-1599065279211733274.json', 'var_function-call-1599065279211735013': 'file_storage/function-call-1599065279211735013.json', 'var_function-call-3315802796629298163': {'count': 1, 'projects': ['PCH Median Improvements Project']}, 'var_function-call-16876239856465075778': {'count': 1, 'matches': ['PCH Median Improvements Project'], 'extracted_sample': ['(cid:131) Complete Design: March 2022', '(cid:131) Complete Design: April 2021', 'bidding.', 'PCH Median Improvements Project', '(cid:131) Advertise: Fall 2023', 'and rejected all bids due to a budget shortfall', 'management.', '(cid:131) Complete Design: February 2021', 'project and will submit to the County for review.', '2022 Morning View Resurfacing & Storm Drain Improvements', 'construction bids.', 'advertised for construction bids shortly after this date.', 'or phasing out the project', '(cid:131) Complete Design: Summer 2023', '(cid:190) Project Schedule:', 'Marie Canyon Green Streets'], 'funded_skate': ['Permanent Skate Park'], 'extracted_skate': []}}

exec(code, env_args)

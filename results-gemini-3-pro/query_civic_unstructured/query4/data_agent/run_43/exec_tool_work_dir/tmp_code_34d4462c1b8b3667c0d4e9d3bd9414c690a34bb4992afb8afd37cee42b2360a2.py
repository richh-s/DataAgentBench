code = """import json
import re

civic_docs_path = locals()['var_function-call-12607651032579543164']
funding_path = locals()['var_function-call-5868675038188901918']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        found_marker = False
        
        # Look ahead
        for offset in range(1, 5):
            if i + offset < len(lines):
                nl = lines[i+offset].strip()
                # Check for (cid:...) Updates/Description
                if '(cid:' in nl and ('Updates' in nl or 'Project Description' in nl):
                    found_marker = True
                    break
            else:
                break
        
        if found_marker:
            if "Capital Improvement Projects" in line:
                continue
            
            p_name = line
            start_date = None
            
            scan_idx = i + 1
            while scan_idx < len(lines):
                sline = lines[scan_idx].strip()
                if 'Begin Construction:' in sline:
                    start_date = sline.split('Begin Construction:')[1].strip()
                    break
                
                # Check for other markers to stop
                if scan_idx > i + 5 and '(cid:' in sline and ('Updates' in sline or 'Project Description' in sline):
                    break
                
                if scan_idx - i > 50:
                    break
                    
                scan_idx += 1
            
            projects.append({'name': p_name, 'start_date': start_date})

# Filter
matches = []
for p in projects:
    sd = p['start_date']
    if sd:
        sd_lower = sd.lower()
        if 'spring 2022' in sd_lower:
            matches.append(p['name'])
        elif '2022' in sd_lower:
            if 'march' in sd_lower or 'april' in sd_lower or 'may' in sd_lower:
                matches.append(p['name'])
            if '2022-03' in sd_lower or '2022-04' in sd_lower or '2022-05' in sd_lower:
                matches.append(p['name'])

unique_matches = list(set(matches))

# Funding
def norm(s):
    return "".join([c.lower() for c in s if c.isalnum()])

funding_map = {}
for item in funding_data:
    funding_map[norm(item['Project_Name'])] = item['Amount']

total_funding = 0
matched_projects = []

for name in unique_matches:
    n_name = norm(name)
    matched_amount = 0
    
    if n_name in funding_map:
        matched_amount = funding_map[n_name]
    else:
        # fuzzy
        for k, v in funding_map.items():
            if n_name in k or k in n_name:
                matched_amount = v
                break
    
    if matched_amount > 0:
        total_funding += matched_amount
        matched_projects.append(name)

print("__RESULT__:")
print(json.dumps({
    "count": len(matched_projects),
    "total_funding": total_funding,
    "projects": matched_projects,
    "debug_matches": matches,
    "debug_all": projects[:5]
}))"""

env_args = {'var_function-call-14853737414132312257': ['Funding'], 'var_function-call-14853737414132313422': 'file_storage/function-call-14853737414132313422.json', 'var_function-call-5868675038188901918': 'file_storage/function-call-5868675038188901918.json', 'var_function-call-12607651032579543164': 'file_storage/function-call-12607651032579543164.json'}

exec(code, env_args)

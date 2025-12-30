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
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for marker in next few lines
        found_marker = False
        
        # Look ahead
        for offset in range(1, 5):
            if i + offset < len(lines):
                nl = lines[i+offset].strip()
                # Use regex to match the marker
                if re.match(r'^\(cid:\d+\)\s*Updates', nl) or re.match(r'^\(cid:\d+\)\s*Project Description', nl):
                    found_marker = True
                    break
            else:
                break
        
        if found_marker:
            if "Capital Improvement Projects" in line:
                continue
            
            p_name = line
            start_date = None
            
            # Scan forward for start date
            scan_idx = i + 1
            while scan_idx < len(lines):
                sline = lines[scan_idx].strip()
                # Check for start date
                # "Begin Construction: ..."
                m = re.search(r'Begin Construction:\s*(.*)', sline, re.IGNORECASE)
                if m:
                    start_date = m.group(1).strip()
                    break
                
                # Stop at next marker
                if re.match(r'^\(cid:\d+\)\s*Updates', sline) and scan_idx > i + 5: 
                    # Only stop if it's far enough, though markers are usually right after name.
                    # Wait, we want to stop at the NEXT project's marker.
                    # The current project has a marker too.
                    # The marker is usually at i+offset.
                    # So if we see a marker after the initial one, it's a new project.
                    break
                
                # Also stop if we see a line that looks like a project name (hard to define)
                # Just limiting the search window is safer?
                # Usually project block is < 50 lines.
                if scan_idx - i > 50:
                    break
                    
                scan_idx += 1
            
            projects.append({'name': p_name, 'start_date': start_date})

# Filter for Spring 2022
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
            # check YYYY-MM
            if '2022-03' in sd_lower or '2022-04' in sd_lower or '2022-05' in sd_lower:
                matches.append(p['name'])

unique_matches = list(set(matches))

# Calculate funding
total_funding = 0
matched_count = 0
matched_details = []

# Funding lookup
# Create a normalized map
def norm(s):
    return re.sub(r'\W+', '', s).lower()

funding_map = {}
for item in funding_data:
    funding_map[norm(item['Project_Name'])] = item['Amount']

for name in unique_matches:
    n_name = norm(name)
    amount = 0
    matched = False
    
    if n_name in funding_map:
        amount = funding_map[n_name]
        matched = True
    else:
        # Fuzzy match
        for f_name, f_amt in funding_map.items():
            if n_name in f_name or f_name in n_name:
                amount = f_amt
                matched = True
                break
    
    if matched:
        total_funding += amount
        matched_count += 1
        matched_details.append(name)

print("__RESULT__:")
print(json.dumps({
    "count": matched_count,
    "total_funding": total_funding,
    "projects": matched_details,
    "debug_all_projects_with_dates": [p for p in projects if p['start_date']]
}))"""

env_args = {'var_function-call-14853737414132312257': ['Funding'], 'var_function-call-14853737414132313422': 'file_storage/function-call-14853737414132313422.json', 'var_function-call-5868675038188901918': 'file_storage/function-call-5868675038188901918.json', 'var_function-call-12607651032579543164': 'file_storage/function-call-12607651032579543164.json'}

exec(code, env_args)

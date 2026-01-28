code = """import json
import re

# Load data
with open(locals()['var_function-call-14460790621414043355'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-16841234129096573312'], 'r') as f:
    funding_data = json.load(f)

# Sort civic_docs by date descending
def get_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        return match.group(1)
    return "00000000"

civic_docs.sort(key=lambda x: get_date(x['filename']), reverse=True)

projects = []
# Regex for headers
header_re = re.compile(r'Capital Improvement Projects \((Design|Construction|Not Started)\)', re.IGNORECASE)

for doc in civic_docs:
    fname = doc['filename']
    date = get_date(fname)
    text = doc['text']
    lines = text.split('\n')
    current_status = None
    buffer_name = None
    buffer_text = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for Section Header
        match = header_re.search(line)
        if match:
            current_status = match.group(1).lower()
            if current_status == "construction":
                current_status = "construction_section"
            elif current_status == "not started":
                current_status = "not started"
            i += 1
            continue
            
        # Check for Project Start
        # We look ahead for "(cid:190)" or unicode 3/4
        # In JSON strings passed here, we need to be careful with unicode
        # The file loaded via json.load handles it.
        # We check if next line contains the bullet and "Updates"
        if i + 1 < len(lines):
            next_line = lines[i+1]
            # Check for bullet
            has_bullet = "(cid:190)" in next_line or "\u00be" in next_line
            if has_bullet and ("Updates" in next_line or "Project Description" in next_line):
                # Found a project start
                if buffer_name:
                    projects.append({
                        'name': buffer_name,
                        'status_context': current_status,
                        'text': "\n".join(buffer_text),
                        'date': date
                    })
                
                buffer_name = line
                buffer_text = []
                i += 2 
                continue
            
        if buffer_name:
            buffer_text.append(line)
        
        i += 1

    if buffer_name:
        projects.append({
            'name': buffer_name,
            'status_context': current_status,
            'text': "\n".join(buffer_text),
            'date': date
        })

# Deduplicate: Keep latest
latest_projects = {}
for p in projects:
    name_norm = p['name'].strip().lower()
    if not name_norm: continue
    if name_norm not in latest_projects:
        latest_projects[name_norm] = p
    else:
        # Compare dates (MMDDYYYY)
        # Convert to YYYYMMDD
        d1 = p['date']
        d2 = latest_projects[name_norm]['date']
        d1_s = d1[4:] + d1[:2] + d1[2:4] # YYYY MM DD
        d2_s = d2[4:] + d2[:2] + d2[2:4]
        if d1_s > d2_s:
            latest_projects[name_norm] = p

relevant_projects = []
for name_norm, p in latest_projects.items():
    p_text = p['text'].lower()
    p_name = p['name']
    p_name_lower = p_name.lower()
    
    is_relevant = False
    if 'fema' in p_name_lower or 'emergency' in p_name_lower:
        is_relevant = True
    if 'fema' in p_text or 'emergency' in p_text:
        is_relevant = True
        
    if not is_relevant:
        continue
        
    status = "unknown"
    if p['status_context'] == 'design':
        status = 'design'
    elif p['status_context'] == 'not started':
        status = 'not started'
    elif p['status_context'] == 'construction_section':
        if 'completed' in p_text or 'notice of completion' in p_text:
            status = 'completed'
        elif 'under construction' in p_text:
            status = 'under construction'
        else:
            status = 'under construction' # Default for construction section

    clean_name = p_name.strip()
    relevant_projects.append({
        'extracted_name': clean_name,
        'status': status
    })

final_results = []
for rp in relevant_projects:
    for fund in funding_data:
        fund_name = fund['Project_Name']
        # Check if extracted name is contained in funding name
        if rp['extracted_name'].lower() in fund_name.lower(): 
            final_results.append({
                "Project_Name": fund_name,
                "Funding_Source": fund['Funding_Source'],
                "Amount": fund['Amount'],
                "Status": rp['status']
            })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-16841234129096573312': 'file_storage/function-call-16841234129096573312.json', 'var_function-call-16841234129096575269': 'file_storage/function-call-16841234129096575269.json', 'var_function-call-1647785278935459272': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-14460790621414043355': 'file_storage/function-call-14460790621414043355.json'}

exec(code, env_args)

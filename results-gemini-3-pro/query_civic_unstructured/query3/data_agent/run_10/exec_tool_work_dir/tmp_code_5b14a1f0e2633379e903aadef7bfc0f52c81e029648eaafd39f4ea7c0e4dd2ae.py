code = """import json
import re

with open(locals()['var_function-call-14460790621414043355'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-16841234129096573312'], 'r') as f:
    funding_data = json.load(f)

def get_date(filename):
    match = re.search(r'(\d{8})', filename)
    return match.group(1) if match else "00000000"

civic_docs.sort(key=lambda x: get_date(x['filename']), reverse=True)

projects = []
header_re = re.compile(r'Capital Improvement Projects [(](Design|Construction|Not Started)[)]', re.IGNORECASE)

for doc in civic_docs:
    fname = doc['filename']
    date = get_date(fname)
    text = doc['text']
    lines = text.split(chr(10)) 
    
    current_status = None
    buffer_name = None
    buffer_text = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        match = header_re.search(line)
        if match:
            current_status = match.group(1).lower()
            if current_status == "construction":
                current_status = "construction_section"
            elif current_status == "not started":
                current_status = "not started"
            i += 1
            continue
            
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if ("(cid:190)" in next_line or chr(190) in next_line) and ("Updates" in next_line or "Project Description" in next_line):
                if buffer_name:
                    projects.append({'name': buffer_name, 'status_context': current_status, 'text': chr(10).join(buffer_text), 'date': date})
                buffer_name = line
                buffer_text = []
                i += 2
                continue
        
        if buffer_name:
            buffer_text.append(line)
        i += 1
    if buffer_name:
        projects.append({'name': buffer_name, 'status_context': current_status, 'text': chr(10).join(buffer_text), 'date': date})

latest_projects = {}
for p in projects:
    name_norm = p['name'].strip().lower()
    if not name_norm: continue
    if name_norm not in latest_projects:
        latest_projects[name_norm] = p
    else:
        d1 = p['date']
        d2 = latest_projects[name_norm]['date']
        d1_s = d1[4:] + d1[:2] + d1[2:4]
        d2_s = d2[4:] + d2[:2] + d2[2:4]
        if d1_s > d2_s:
            latest_projects[name_norm] = p

relevant_projects = []
for name_norm, p in latest_projects.items():
    p_text = p['text'].lower()
    p_name = p['name']
    
    is_relevant = False
    if 'fema' in p_name.lower() or 'emergency' in p_name.lower():
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
            status = 'under construction'

    relevant_projects.append({'extracted_name': p_name.strip(), 'status': status})

final_results = []
for rp in relevant_projects:
    for fund in funding_data:
        fund_name = fund['Project_Name']
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

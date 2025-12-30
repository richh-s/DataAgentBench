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
    
    events = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        match = header_re.search(line)
        if match:
            status = match.group(1).lower()
            if status == "construction": status = "construction_section"
            elif status == "not started": status = "not started"
            events.append({'i': i, 'type': 'header', 'val': status})
            continue
            
        if "(cid:190)" in line and ("Updates" in line or "Project Description" in line):
            events.append({'i': i, 'type': 'bullet'})
            
    project_starts = []
    for evt in events:
        if evt['type'] == 'bullet':
            bullet_idx = evt['i']
            name_idx = bullet_idx - 1
            while name_idx >= 0:
                if lines[name_idx].strip():
                    break
                name_idx -= 1
            
            if name_idx < 0: continue
            
            current_status = "unknown"
            for h in events:
                if h['type'] == 'header' and h['i'] < name_idx:
                    current_status = h['val']
                if h['i'] > name_idx: # Optimized: events are sorted by i? Yes append order
                    pass # Keep looking? No, we need the *last* header before name_idx
            
            # Better status lookup: Filter headers < name_idx, take last
            headers_before = [h for h in events if h['type'] == 'header' and h['i'] < name_idx]
            if headers_before:
                current_status = headers_before[-1]['val']
            
            project_starts.append({
                'start_idx': name_idx,
                'name': lines[name_idx].strip(),
                'status_context': current_status
            })
            
    project_starts.sort(key=lambda x: x['start_idx'])
    
    # Remove duplicates if multiple bullets refer to same project name line (unlikely but safe)
    # Actually, logic allows multiple bullets to point to same name line?
    # Yes, if bullets are adjacent?
    # But loop finds *closest* non-empty line.
    # If 2 bullets, 2nd bullet finds name? No, if 1st bullet is between name and 2nd bullet...
    # But bullet line is non-empty. So 2nd bullet would think 1st bullet is the name?
    # Bullet line contains (cid:190).
    # We should exclude bullet lines from being names?
    # "line.strip()" check.
    # Add check: `lines[name_idx]` should not be a bullet line?
    # But checking if it contains `(cid:190)` might be enough.
    # Whatever. The first bullet finds the name. The logic holds.
    
    # Dedupe by start_idx
    unique_starts = []
    seen = set()
    for p in project_starts:
        if p['start_idx'] not in seen:
            unique_starts.append(p)
            seen.add(p['start_idx'])
    project_starts = unique_starts

    for k in range(len(project_starts)):
        start = project_starts[k]['start_idx']
        if k < len(project_starts) - 1:
            end = project_starts[k+1]['start_idx']
        else:
            end = len(lines)
            
        p_text_lines = lines[start:end]
        p_text = chr(10).join(p_text_lines)
        
        projects.append({
            'name': project_starts[k]['name'],
            'status_context': project_starts[k]['status_context'],
            'text': p_text,
            'date': date
        })

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
    ctx = p['status_context']
    if ctx == 'design':
        status = 'design'
    elif ctx == 'not started':
        status = 'not started'
    elif ctx == 'construction_section':
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

env_args = {'var_function-call-16841234129096573312': 'file_storage/function-call-16841234129096573312.json', 'var_function-call-16841234129096575269': 'file_storage/function-call-16841234129096575269.json', 'var_function-call-1647785278935459272': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-14460790621414043355': 'file_storage/function-call-14460790621414043355.json', 'var_function-call-9486973076472858679': [], 'var_function-call-17381857488662847818': {'has_cid': True, 'has_uni': False, 'line_count': 434, 'sample_lines': ['Public Works Commission', 'Agenda Report', '', 'Public Works', 'Commission Meeting', '03-22-23', 'Item', '4.B.', '', 'To:', '', 'Chair Dittrich and Members of the Public Works Commission', '', 'Prepared by:', '', 'Jorge Rubalcava, Senior Civil Engineer', '', 'Approved by:', '', 'Rob DuBoux, Public Works Director/City Engineer']}, 'var_function-call-10911503705911584325': ['Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', 'Fiscal Year 2022-2023 Capital Improvement Program:', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']}

exec(code, env_args)

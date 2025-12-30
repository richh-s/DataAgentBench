code = """import json

with open(locals()['var_function-call-16869852261944468410'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2108232826166806416'], 'r') as f:
    funding_data = json.load(f)

projects = []
keywords = ['emergency', 'fema']

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_status = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if "Capital Improvement Projects (Design)" in line:
            current_status = "design"
            i += 1
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_status = "construction"
            i += 1
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "not_started"
            i += 1
            continue
            
        is_project_start = False
        
        # Look ahead for marker
        # Marker is 'Updates:' or 'Project Description:'
        for offset in range(1, 4):
            if i + offset < len(lines):
                l = lines[i+offset].strip()
                if "Updates:" in l or "Project Description:" in l:
                    is_project_start = True
                    break
        
        if is_project_start and current_status and line:
             p_name = line
             p_text_lines = []
             j = i
             while j < len(lines):
                 if "Capital Improvement Projects (" in lines[j]:
                     break
                 
                 # Check for next project start
                 is_next = False
                 if j > i:
                     for offset in range(1, 4):
                         if j + offset < len(lines):
                             l = lines[j+offset].strip()
                             if "Updates:" in l or "Project Description:" in l:
                                 # Ensure it is not part of current text (e.g. nested?)
                                 # Assuming headers are distinct
                                 # Also check if lines[j] (the name candidate) is not empty
                                 if lines[j].strip():
                                     is_next = True
                                     break
                 if is_next:
                     break
                 
                 p_text_lines.append(lines[j])
                 j += 1
             
             p_text = "\n".join(p_text_lines)
             
             final_status = current_status
             p_text_lower = p_text.lower()
             if current_status == "construction":
                 if "construction was completed" in p_text_lower or "notice of completion" in p_text_lower:
                     final_status = "completed"
                 elif "completed" in p_text_lower and "under construction" not in p_text_lower:
                     final_status = "completed"
                 elif "under construction" in p_text_lower:
                     final_status = "construction"
             
             projects.append({
                 "Project_Name": p_name,
                 "text": p_text,
                 "status": final_status
             })
             
             i = j
             continue
        
        i += 1

final_results = []

for p in projects:
    p_name = p['Project_Name']
    p_text_lower = p['text'].lower()
    
    is_relevant = False
    for k in keywords:
        if k in p_name.lower() or k in p_text_lower:
            is_relevant = True
            break
            
    p_funding = []
    has_fema_funding = False
    
    for f in funding_data:
        f_name = f['Project_Name']
        f_name_lower = f_name.lower()
        
        match = False
        # Relaxed matching
        if p_name.lower() in f_name_lower or f_name_lower in p_name.lower():
            match = True
            
        if match:
            p_funding.append(f)
            if 'fema' in f_name_lower or 'emergency' in f_name_lower:
                has_fema_funding = True
    
    if is_relevant or has_fema_funding:
        if not p_funding:
            final_results.append({
                "Project_Name": p_name,
                "Funding_Source": None,
                "Amount": None,
                "Status": p['status']
            })
        else:
            for pf in p_funding:
                final_results.append({
                    "Project_Name": pf['Project_Name'],
                    "Funding_Source": pf['Funding_Source'],
                    "Amount": pf['Amount'],
                    "Status": p['status']
                })

print("__RESULT__:")
print(json.dumps(final_results, indent=2))"""

env_args = {'var_function-call-4927192058268625758': ['civic_docs'], 'var_function-call-4927192058268625809': ['Funding'], 'var_function-call-2108232826166805977': 'file_storage/function-call-2108232826166805977.json', 'var_function-call-2108232826166806416': 'file_storage/function-call-2108232826166806416.json', 'var_function-call-16869852261944468410': 'file_storage/function-call-16869852261944468410.json'}

exec(code, env_args)

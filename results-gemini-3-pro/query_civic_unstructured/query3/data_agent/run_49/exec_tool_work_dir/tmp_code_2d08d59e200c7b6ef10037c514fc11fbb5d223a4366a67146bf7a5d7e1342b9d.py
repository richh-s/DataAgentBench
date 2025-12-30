code = """import json

# Load extracted data
with open(locals()['var_function-call-17911160366985572279'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-5314689848264008089'], 'r') as f:
    funding_data = json.load(f)

projects_extracted = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_status = "Unknown"
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Check for Headers
        if "Capital Improvement Projects (Design)" in line:
            current_status = "design"
            i += 1
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_status = "construction"
            i += 1
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "not started"
            i += 1
            continue
            
        # Check for Project Title
        # Look ahead for (cid:190)
        j = i + 1
        next_line = ""
        while j < len(lines):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
            j += 1
            
        if next_line.startswith("(cid:190)"):
            # Found a project
            project_name = line
            
            # Extract block
            block_lines = [line]
            k = i + 1
            while k < len(lines):
                l_strip = lines[k].strip()
                # Stop if next header
                if "Capital Improvement Projects (" in l_strip:
                    break
                
                # Stop if next project
                # Look ahead from k
                m = k + 1
                next_l_strip = ""
                while m < len(lines):
                    if lines[m].strip():
                        next_l_strip = lines[m].strip()
                        break
                    m += 1
                
                if next_l_strip.startswith("(cid:190)") and l_strip:
                    break
                
                block_lines.append(lines[k])
                k += 1
            
            full_text = "\n".join(block_lines)
            
            # Refine status
            status = current_status
            lower_text = full_text.lower()
            if status == "construction":
                if "construction was completed" in lower_text or "notice of completion" in lower_text:
                    status = "completed"
            
            projects_extracted.append({
                "name": project_name,
                "status": status,
                "text": full_text
            })
            
            i = k
        else:
            i += 1

results = []
seen = set()

for p in projects_extracted:
    p_name = p['name'].strip()
    p_text = p['text'].lower()
    p_status = p['status']
    
    is_related_text = "emergency" in p_text or "fema" in p_text
    
    matched_funding = []
    for f in funding_data:
        f_name = f['Project_Name'].strip()
        # Clean f_name of trailing spaces or artifacts?
        
        # Logic: 
        # 1. Exact
        # 2. F starts with P (suffix)
        
        if f_name == p_name:
            matched_funding.append(f)
        elif f_name.startswith(p_name) and ("(FEMA" in f_name or "(CalOES" in f_name or "(CalJPIA" in f_name):
            matched_funding.append(f)
            
    is_related_funding = any("FEMA" in f['Project_Name'] for f in matched_funding)
    
    if is_related_text or is_related_funding:
        if matched_funding:
            for f in matched_funding:
                # Deduplicate
                key = (f['Project_Name'], f['Funding_Source'], f['Amount'], p_status)
                if key not in seen:
                    results.append({
                        "Project_Name": f['Project_Name'],
                        "Funding_Source": f['Funding_Source'],
                        "Amount": f['Amount'],
                        "Status": p_status
                    })
                    seen.add(key)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5314689848264011546': 'file_storage/function-call-5314689848264011546.json', 'var_function-call-5314689848264008089': 'file_storage/function-call-5314689848264008089.json', 'var_function-call-17911160366985572279': 'file_storage/function-call-17911160366985572279.json'}

exec(code, env_args)

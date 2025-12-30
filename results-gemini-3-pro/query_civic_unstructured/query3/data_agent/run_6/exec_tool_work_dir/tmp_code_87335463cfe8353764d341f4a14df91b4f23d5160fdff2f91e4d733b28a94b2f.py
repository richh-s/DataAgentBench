code = """import json

# keys
key_funding = 'var_function-call-15202175332951554163'
key_docs = 'var_function-call-15202175332951553736'

with open(locals()[key_funding], 'r') as f:
    funding_list = json.load(f)

with open(locals()[key_docs], 'r') as f:
    docs_list = json.load(f)

# Normalize projects
extracted = []

for doc in docs_list:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_section = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Section detection
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            current_section = line
            i += 1
            continue
            
        # Project detection
        # Look for "Updates:" or "Project Description:" or "Project Updates:" in the NEXT line
        # Use simple string checks
        is_project = False
        if i + 1 < len(lines):
            nxt = lines[i+1].strip()
            if "Updates:" in nxt or "Project Description:" in nxt or "Project Updates:" in nxt:
                is_project = True
        
        if is_project and line:
            p_name = line
            
            # extract block
            block = []
            j = i + 1
            while j < len(lines):
                sub = lines[j].strip()
                # Check for new section
                if "Capital Improvement Projects" in sub or "Disaster Recovery Projects" in sub:
                    break
                # Check for new project
                if j + 1 < len(lines):
                    sub_nxt = lines[j+1].strip()
                    if ("Updates:" in sub_nxt or "Project Description:" in sub_nxt or "Project Updates:" in sub_nxt) and sub:
                        break
                block.append(sub)
                j += 1
            
            block_str = " ".join(block)
            
            # Check keywords
            combo = (p_name + " " + block_str).lower()
            if "emergency" in combo or "fema" in combo:
                # Determine status
                status = "Unknown"
                sec_lower = (current_section or "").lower()
                blk_lower = block_str.lower()
                
                if "design" in sec_lower:
                    status = "design"
                elif "not started" in sec_lower:
                    status = "not started"
                elif "construction" in sec_lower:
                    if "completed" in blk_lower and "currently under construction" not in blk_lower:
                        status = "completed"
                    elif "notice of completion" in blk_lower:
                        status = "completed"
                    else:
                        status = "construction" # Or 'completed'? Use 'construction' for accuracy.
                
                extracted.append({"Project_Name": p_name, "Status": status})
            
            i = j
        else:
            i += 1

# Join
results = []
f_map = {x['Project_Name']: x for x in funding_list}
f_map_low = {x['Project_Name'].lower(): x for x in funding_list}

for p in extracted:
    nm = p['Project_Name']
    rec = f_map.get(nm)
    if not rec:
        rec = f_map_low.get(nm.lower())
    
    if rec:
        # Create result entry
        # Check duplicate
        exists = False
        for r in results:
            if r['Project_Name'] == rec['Project_Name']:
                exists = True
                break
        if not exists:
            results.append({
                "Project_Name": rec['Project_Name'],
                "Funding_Source": rec['Funding_Source'],
                "Amount": rec['Amount'],
                "Status": p['Status']
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8043042587493176858': ['Funding'], 'var_function-call-8043042587493178041': ['civic_docs'], 'var_function-call-15202175332951554163': 'file_storage/function-call-15202175332951554163.json', 'var_function-call-15202175332951553736': 'file_storage/function-call-15202175332951553736.json'}

exec(code, env_args)

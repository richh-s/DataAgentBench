code = """import json

with open(locals()['var_function-call-2028314322626917702'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10132172204667131329'], 'r') as f:
    civic_docs = json.load(f)

extracted = []

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_status = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            if "Design" in line:
                current_status = "design"
            elif "Construction" in line:
                current_status = "construction"
            elif "Not Started" in line:
                current_status = "not started"
            elif "Completed" in line:
                current_status = "completed"
            i += 1
            continue
        
        # Project Detection
        is_project = False
        j = i + 1
        # Skip empty lines to find next content
        while j < len(lines) and not lines[j].strip():
            j += 1
        
        if j < len(lines):
            next_start = lines[j].strip()
            # Check for bullet points or keywords
            if next_start.startswith("Updates:") or next_start.startswith("Project Description:") or next_start.startswith("(cid:"):
                is_project = True
        
        if is_project and current_status:
            p_name = line
            # Extract block
            block_lines = []
            k = j
            while k < len(lines):
                l = lines[k].strip()
                # Check for Header
                if ("Capital Improvement Projects" in l or "Disaster Recovery Projects" in l) and ("(" in l and ")" in l):
                    break
                
                # Check for New Project Name
                # A line is a new project name if IT is followed by bullet, AND it's not a bullet itself.
                # Only check if l is not empty and not bullet
                if l and not l.startswith("Updates:") and not l.startswith("Project Description:") and not l.startswith("(cid:"):
                    # Check its next line
                    m = k + 1
                    while m < len(lines) and not lines[m].strip():
                        m += 1
                    if m < len(lines):
                        ns = lines[m].strip()
                        if ns.startswith("Updates:") or ns.startswith("Project Description:") or ns.startswith("(cid:"):
                            # Found new project start at l
                            break
                
                block_lines.append(l)
                k += 1
            
            block_text = " ".join(block_lines)
            
            # Status Check
            status = current_status
            if status == "construction":
                if "completed" in block_text.lower() and ("construction was completed" in block_text.lower() or "notice of completion" in block_text.lower()):
                    status = "completed"
            
            extracted.append({
                "name": p_name,
                "text": block_text,
                "status": status
            })
            
            i = k
            continue
            
        i += 1

# Filter and Join
final_results = []
seen = set()

for p in extracted:
    content = (p['name'] + " " + p['text']).lower()
    if 'emergency' in content or 'fema' in content:
        p_name_norm = p['name'].lower().replace('(fema project)', '').replace('project', '').strip()
        # Simplify name for matching: remove common words? No, be careful.
        # "Latigo Canyon Road Retaining Wall Repair"
        
        for f in funding_data:
            f_name = f['Project_Name']
            f_name_norm = f_name.lower().replace('(fema project)', '').replace('(caloes project)', '').replace('(fema/caloes project)', '').replace('(fema)', '').replace('project', '').strip()
            
            # Robust Matching
            # Check if one is substring of another
            match = False
            if p_name_norm == f_name_norm:
                match = True
            elif p_name_norm in f_name_norm and len(p_name_norm) > 10:
                match = True
            elif f_name_norm in p_name_norm and len(f_name_norm) > 10:
                match = True
            
            # Special case for "Outdoor Warning Sirens" vs "Outdoor Warning Signs" (Signs is 64, Sirens is 65)
            # "Signs" vs "Sirens".
            # If p_name is "Outdoor Warning Signs", f_name "Outdoor Warning Sirens" should NOT match.
            # Substring matching might be dangerous if names are very similar.
            # "Outdoor Warning Sirens" in "Outdoor Warning Sirens - Design" -> Yes.
            
            if match:
                # Add to results
                item = {
                    "Project_Name": f['Project_Name'],
                    "Funding_Source": f['Funding_Source'],
                    "Amount": f['Amount'],
                    "Status": p['status']
                }
                # Create a unique key
                key = (item['Project_Name'], item['Funding_Source'], str(item['Amount']), item['Status'])
                if key not in seen:
                    seen.add(key)
                    final_results.append(item)

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-2105256659697284702': ['civic_docs'], 'var_function-call-2105256659697283933': ['Funding'], 'var_function-call-2028314322626917702': 'file_storage/function-call-2028314322626917702.json', 'var_function-call-2028314322626917971': 'file_storage/function-call-2028314322626917971.json', 'var_function-call-4575957102787257553': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-10132172204667131329': 'file_storage/function-call-10132172204667131329.json'}

exec(code, env_args)

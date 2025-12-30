code = """import json
import re

funding_path = locals()['var_function-call-3669555105511177724']
civic_path = locals()['var_function-call-3669555105511175475']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Funding map
funding_map = {item['Project_Name'].strip(): item for item in funding_data if item.get('Project_Name')}

results = []
relevance_triggers = ["emergency", "fema"]

for doc in civic_data:
    text = doc.get('text', '')
    # Handle bullet points
    # (cid:190) and (cid:131)
    bullet1 = chr(40) + 'cid:190' + chr(41)
    bullet2 = chr(40) + 'cid:131' + chr(41)
    text = text.replace(bullet1, 'BULLET1').replace(bullet2, 'BULLET2')
    
    # Split lines
    lines = [l.strip() for l in text.split(chr(10)) if l.strip()]
    
    current_type = None
    current_status_hint = "design"
    
    found_projects = []
    
    curr_name = None
    curr_lines = []
    
    in_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            if curr_name:
                found_projects.append((curr_name, current_type, current_status_hint, curr_lines))
                curr_name = None
                curr_lines = []
            
            in_section = True
            if "Capital Improvement Projects" in line:
                current_type = "capital"
            else:
                current_type = "disaster"
            
            if "(Design)" in line:
                current_status_hint = "design"
            elif "(Construction)" in line:
                current_status_hint = "construction"
            elif "(Not Started)" in line:
                current_status_hint = "not started"
            else:
                current_status_hint = "design"
            
            i += 1
            continue
            
        if not in_section:
            i += 1
            continue
            
        # Project Detection
        is_bullet = line.startswith('BULLET')
        # Meta lines to skip
        is_meta = line.startswith('Page ') or line.startswith('Agenda Item') or line.startswith('Subject:') or line.startswith('Date ') or line.startswith('To:')
        
        if not is_bullet and not is_meta:
            # Assume new project if not bullet and not meta
            if curr_name:
                found_projects.append((curr_name, current_type, current_status_hint, curr_lines))
            
            curr_name = line
            curr_lines = []
        else:
            if curr_name:
                curr_lines.append(line)
        i += 1
        
    if curr_name:
        found_projects.append((curr_name, current_type, current_status_hint, curr_lines))

    # Process
    for pname, ptype, phint, plines in found_projects:
        full_text = " ".join(plines)
        combined = (pname + " " + full_text).lower()
        
        # Filter Relevance
        is_relevant = False
        for trig in relevance_triggers:
            if trig in combined:
                is_relevant = True
                break
        
        if not is_relevant:
            continue
            
        # Determine Status
        status = phint
        if status == "construction":
            if "completed" in full_text.lower() or "notice of completion" in full_text.lower():
                status = "completed"
            else:
                status = "design" # Map active construction to design
        
        # Get Funding
        f_rec = funding_map.get(pname)
        if not f_rec:
            # Clean pname of suffixes
            # e.g. " (FEMA Project)"
            pname_clean = pname
            # Remove parenthesis at end
            if '(' in pname:
                pname_clean = pname.split('(')[0].strip()
            
            f_rec = funding_map.get(pname_clean)
            
            if not f_rec:
                # Try finding key in pname
                for k, v in funding_map.items():
                    if k in pname or pname in k:
                        if len(k) > 10:
                            f_rec = v
                            break

        results.append({
            "Project_Name": pname,
            "Funding_Source": f_rec['Funding_Source'] if f_rec else None,
            "Amount": f_rec['Amount'] if f_rec else None,
            "Status": status
        })

# Deduplicate
unique_results = []
seen = set()
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_function-call-3669555105511177724': 'file_storage/function-call-3669555105511177724.json', 'var_function-call-3669555105511175475': 'file_storage/function-call-3669555105511175475.json'}

exec(code, env_args)

code = """import json
import re

k_fund = "var_function-call-15202175332951554163"
k_docs = "var_function-call-15202175332951553736"

with open(locals()[k_fund], "r") as f:
    funds = json.load(f)

with open(locals()[k_docs], "r") as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    txt = doc.get("text", "")
    lines = txt.splitlines()
    
    events = [] # (index, type, content)
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Check Section
        if "Projects" in line and ("Capital" in line or "Disaster" in line):
            events.append((i, "SECTION", line))
            i += 1
            continue
            
        # Check Project
        # Look ahead for marker
        # Scan forward for next non-empty line
        j = i + 1
        marker_found = False
        while j < len(lines):
            nxt = lines[j].strip()
            if not nxt:
                j += 1
                continue
            
            if "Updates:" in nxt or "Project Description:" in nxt or "Project Updates:" in nxt:
                marker_found = True
            break
        
        if marker_found:
            events.append((i, "PROJECT", line))
            # Skip the marker line? No, let the text extraction handle it (it's part of the text block)
            # Actually, the marker is part of the project description.
            # So next event search starts at i+1
            i += 1 
        else:
            i += 1
            
    # Process events
    current_sec = "not started"
    
    for k in range(len(events)):
        idx, ev_type, content = events[k]
        
        if ev_type == "SECTION":
            current_sec = content
        elif ev_type == "PROJECT":
            p_name = content
            
            # Determine end index
            if k + 1 < len(events):
                end_idx = events[k+1][0]
            else:
                end_idx = len(lines)
            
            # Extract text
            block_lines = lines[idx+1 : end_idx]
            block_str = " ".join([l.strip() for l in block_lines])
            
            # Determine Status
            st = "not started"
            sl = current_sec.lower()
            if "design" in sl:
                st = "design"
            elif "not started" in sl:
                st = "not started"
            elif "completed" in sl:
                st = "completed"
            elif "construction" in sl:
                if "completed" in block_str.lower() and "under construction" not in block_str.lower():
                    st = "completed"
                else:
                    st = "construction"
            
            # Add to list
            extracted_projects.append({
                "name": p_name,
                "status": st,
                "full_text": (p_name + " " + block_str).lower()
            })

# Matching
final_results = []
seen = set()

for f in funds:
    f_name = f['Project_Name']
    
    # Check funding name relevancy
    f_is_rel = 'fema' in f_name.lower() or 'emergency' in f_name.lower()
    
    # Clean name for matching
    f_clean = re.sub(r'\(.*?\)', '', f_name).lower()
    f_tokens = set(re.findall(r'\w+', f_clean))
    
    # Find match in extracted
    match = None
    best_score = 0
    
    for p in extracted_projects:
        p_clean = re.sub(r'\(.*?\)', '', p['name']).lower()
        p_tokens = set(re.findall(r'\w+', p_clean))
        
        if not f_tokens or not p_tokens: continue
        
        common = f_tokens.intersection(p_tokens)
        score = len(common) / max(len(f_tokens), len(p_tokens))
        
        if score > 0.8 and score > best_score:
            best_score = score
            match = p
    
    # Check doc relevancy
    p_is_rel = False
    status = "not started"
    if match:
        status = match['status']
        if 'fema' in match['full_text'] or 'emergency' in match['full_text']:
            p_is_rel = True
            
    if f_is_rel or p_is_rel:
        if f['Funding_ID'] not in seen:
            final_results.append({
                "Project_Name": f_name,
                "Funding_Source": f['Funding_Source'],
                "Amount": f['Amount'],
                "Status": status
            })
            seen.add(f['Funding_ID'])

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-8043042587493176858': ['Funding'], 'var_function-call-8043042587493178041': ['civic_docs'], 'var_function-call-15202175332951554163': 'file_storage/function-call-15202175332951554163.json', 'var_function-call-15202175332951553736': 'file_storage/function-call-15202175332951553736.json', 'var_function-call-7586344906067482996': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'Unknown'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'Unknown'}], 'var_function-call-13099508405464978163': {'extracted_count': 13, 'extracted_samples': [['Capital Improvement Projects (Design)', 'Trancas Canyon Park Playground'], ['Capital Improvement Projects (Construction)', 'Marie Canyon Green Streets'], ['Capital Improvement Projects (Construction)', 'Point Dume Walkway Repairs'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Disaster Projects (Design)', 'Birdview Avenue Improvements (CalOES Project)'], ['Disaster Projects (Completed)', 'Citywide Guardrail Replacement'], ['Disaster Projects (Completed)', 'Malibu Park Storm Drain Repairs'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Disaster Projects (Completed)', 'Citywide Guardrail Replacement'], ['Disaster Projects (Completed)', 'Malibu Park Storm Drain Repairs'], ['Disaster Projects (Completed)', 'Birdview Avenue Improvements (CalOES Project)']], 'funding_samples': ['Birdview Avenue Improvements (FEMA/CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)']}}

exec(code, env_args)

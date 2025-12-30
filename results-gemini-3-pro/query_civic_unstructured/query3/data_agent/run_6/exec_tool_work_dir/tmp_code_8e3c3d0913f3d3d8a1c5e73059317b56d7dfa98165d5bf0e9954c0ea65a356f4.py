code = """import json
import re

k_fund = "var_function-call-15202175332951554163"
k_docs = "var_function-call-15202175332951553736"

with open(locals()[k_fund], "r") as f:
    funds = json.load(f)

with open(locals()[k_docs], "r") as f:
    docs = json.load(f)

# Helper to clean name for matching
def get_core_name(name):
    # Remove contents in parenthesis
    name = re.sub(r'\(.*?\)', '', name)
    # Remove punctuation
    name = re.sub(r'[^\w\s]', '', name)
    # Lowercase
    name = name.lower()
    # Sort tokens
    tokens = sorted(name.split())
    return " ".join(tokens)

# Parse Docs
extracted = []

for d in docs:
    txt = d.get("text", "")
    lines = txt.splitlines()
    
    section = "not started" # Default section
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
            
        # Section Header Detection
        if "Projects" in line and ("Capital" in line or "Disaster" in line):
            section = line
            i += 1
            continue
        
        # Project Name Detection
        # Check if next non-empty line is a marker
        j = i + 1
        is_proj = False
        while j < len(lines):
            nxt = lines[j].strip()
            if not nxt:
                j += 1
                continue
            if "Updates:" in nxt or "Project Description:" in nxt or "Project Updates:" in nxt:
                is_proj = True
            break # Only check the immediate next non-empty
        
        if is_proj:
            p_name = line
            
            # Extract block
            # Consume from j onwards
            block_lines = []
            k = j
            while k < len(lines):
                sub = lines[k].strip()
                if "Projects" in sub and ("Capital" in sub or "Disaster" in sub):
                    break # New section
                
                # Check for start of NEXT project
                # We need to look ahead again
                m = k + 1
                is_next_proj = False
                while m < len(lines):
                    sub_nxt = lines[m].strip()
                    if not sub_nxt:
                        m += 1
                        continue
                    if ("Updates:" in sub_nxt or "Project Description:" in sub_nxt or "Project Updates:" in sub_nxt) and sub:
                        # 'sub' is the name of the next project
                        is_next_proj = True
                    break
                
                if is_next_proj:
                    break
                
                block_lines.append(sub)
                k += 1
            
            block_str = " ".join(block_lines)
            
            # Determine Status from Section
            st = "not started"
            sl = section.lower()
            if "design" in sl:
                st = "design"
            elif "completed" in sl:
                st = "completed"
            elif "construction" in sl:
                # Check text for completion
                if "completed" in block_str.lower() and "under construction" not in block_str.lower():
                    st = "completed"
                else:
                    st = "completed" # Wait, hint said 'design', 'completed', 'not started'. 
                                   # If it's under construction, and I must choose, 'design' is wrong. 'Not started' is wrong.
                                   # 'Completed' is wrong.
                                   # Maybe I should just say "construction" and let the user deal with it, or mapping to "design" (active)?
                                   # Re-reading HINTS: "Projects have three statuses: 'design', 'completed', 'not started'".
                                   # This implies I should map.
                                   # Maybe "Construction" is not a status in the database logic?
                                   # But the document has a "Construction" header.
                                   # If I must pick one of the 3:
                                   # If under construction -> "design" (implementation phase)?
                                   # Or maybe the hint is just listing examples?
                                   # I'll stick to the Section name if it's 'Construction', or map to 'completed' if finished.
                                   # I will output 'construction' if I find it, to be accurate. 
                                   # The prompt asks "What are the ... statuses ...", not "Which of the 3 statuses...".
                                   # The hint describes the data, not strictly constraining the output vocabulary if the data says otherwise.
                                   st = "construction" # I'll use this if not completed.
            
            extracted.append({
                "raw_name": p_name,
                "core_name": get_core_name(p_name),
                "status": st,
                "full_text": (p_name + " " + block_str).lower()
            })
            
            i = k
        else:
            i += 1

# Join and Filter
final_list = []
seen_ids = set()

# Process all Funding entries
for f in funds:
    f_name = f['Project_Name']
    f_core = get_core_name(f_name)
    
    # Check if related to FEMA/Emergency
    is_fema_fund = 'fema' in f_name.lower() or 'emergency' in f_name.lower()
    
    # Find matching doc project
    match_doc = None
    for d in extracted:
        # Try core name match
        # Check if one core name contains the other (tokens)
        # e.g. "birdview avenue improvements" in "birdview avenue improvements caloes project"
        # Since I sorted tokens, "avenue birdview improvements" == "avenue birdview improvements"
        # But "caloes" might be extra.
        # Use set intersection?
        d_core = d['core_name']
        
        # Exact core match
        if f_core == d_core:
            match_doc = d
            break
        
        # If not, check token overlap
        ft = set(f_core.split())
        dt = set(d_core.split())
        if not ft or not dt: continue
        
        # If funding name has 'fema', maybe doc name doesn't.
        # Overlap should be high.
        common = ft.intersection(dt)
        if len(common) / len(ft) > 0.8 or len(common) / len(dt) > 0.8:
            match_doc = d
            break
    
    # Check relevancy in Doc
    is_fema_doc = False
    if match_doc:
        if 'fema' in match_doc['full_text'] or 'emergency' in match_doc['full_text']:
            is_fema_doc = True
            
    if is_fema_fund or is_fema_doc:
        # We want this project
        status = "not started" # Default if not found in doc?
        if match_doc:
            status = match_doc['status']
        
        # avoid duplicates
        if f['Funding_ID'] not in seen_ids:
            final_list.append({
                "Project_Name": f_name,
                "Funding_Source": f['Funding_Source'],
                "Amount": f['Amount'],
                "Status": status
            })
            seen_ids.add(f['Funding_ID'])

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-8043042587493176858': ['Funding'], 'var_function-call-8043042587493178041': ['civic_docs'], 'var_function-call-15202175332951554163': 'file_storage/function-call-15202175332951554163.json', 'var_function-call-15202175332951553736': 'file_storage/function-call-15202175332951553736.json', 'var_function-call-7586344906067482996': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'Unknown'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'Unknown'}], 'var_function-call-13099508405464978163': {'extracted_count': 13, 'extracted_samples': [['Capital Improvement Projects (Design)', 'Trancas Canyon Park Playground'], ['Capital Improvement Projects (Construction)', 'Marie Canyon Green Streets'], ['Capital Improvement Projects (Construction)', 'Point Dume Walkway Repairs'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Disaster Projects (Design)', 'Birdview Avenue Improvements (CalOES Project)'], ['Disaster Projects (Completed)', 'Citywide Guardrail Replacement'], ['Disaster Projects (Completed)', 'Malibu Park Storm Drain Repairs'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Capital Improvement Projects (Design)', 'Marie Canyon Green Streets'], ['Disaster Projects (Completed)', 'Citywide Guardrail Replacement'], ['Disaster Projects (Completed)', 'Malibu Park Storm Drain Repairs'], ['Disaster Projects (Completed)', 'Birdview Avenue Improvements (CalOES Project)']], 'funding_samples': ['Birdview Avenue Improvements (FEMA/CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)']}}

exec(code, env_args)

code = """import json

# Load data
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
        
        # Check for project marker "Updates:" or "Project Description:"
        # We look for the marker, then look backward for the name.
        # But iterating forward is easier.
        # Check if line i+2 or i+1 contains the marker.
        is_project_start = False
        marker_line = -1
        
        # Look ahead up to 3 lines
        for offset in range(1, 4):
            if i + offset < len(lines):
                l = lines[i+offset].strip()
                if ("Updates:" in l or "Project Description:" in l) and ("cid" in l or "\u00be" in l or "(" in l):
                    # Found marker
                    marker_line = i + offset
                    is_project_start = True
                    break
        
        if is_project_start and current_status and line:
             # line is likely the Project Name
             p_name = line
             
             # Capture text
             p_text_lines = []
             j = i
             while j < len(lines):
                 # Stop at next section
                 if "Capital Improvement Projects (" in lines[j]:
                     break
                 # Stop at next project
                 # Check if lines[j] is a name of next project?
                 # It's hard to distinguish name from text without looking ahead.
                 # But we can check if lines[j+1..3] has a marker
                 is_next = False
                 if j > i: # Don't stop at current project start
                     for offset in range(1, 4):
                         if j + offset < len(lines):
                             l = lines[j+offset].strip()
                             # Be careful not to match the current project's body as a new project
                             # Project starts with a Name (text) followed by Marker.
                             # If we see [Text] -> [Marker], then [Text] is a new project.
                             if ("Updates:" in l or "Project Description:" in l) and ("cid" in l or "(" in l):
                                 # Potential new project found at j
                                 is_next = True
                                 break
                 if is_next and lines[j].strip(): 
                     break
                 
                 p_text_lines.append(lines[j])
                 j += 1
             
             p_text = "\n".join(p_text_lines)
             
             # Status logic
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

# Filter and join
final_results = []
# Normalize
def norm(s): return s.lower().replace("(fema project)", "").replace("(caloes project)", "").replace("(fema/caloes project)", "").strip()

for p in projects:
    p_name = p['Project_Name']
    p_text_lower = p['text'].lower()
    
    is_relevant = any(k in p_name.lower() for k in keywords) or any(k in p_text_lower for k in keywords)
    
    p_funding = []
    has_fema_funding = False
    
    # Try to find funding
    for f in funding_data:
        f_name = f['Project_Name']
        f_name_lower = f_name.lower()
        
        # Match logic
        # Check if one contains the other
        match = False
        if p_name.lower() in f_name_lower or f_name_lower in p_name.lower():
            # Check length ratio to avoid spurious matches?
            match = True
        
        # Or check prefix
        if f_name_lower.startswith(p_name.lower()) or p_name.lower().startswith(f_name_lower):
            match = True
            
        if match:
            p_funding.append(f)
            if 'fema' in f_name_lower or 'emergency' in f_name_lower:
                has_fema_funding = True
    
    if is_relevant or has_fema_funding:
        if not p_funding:
             final_results.append({
                "Project_Name": p_name,
                "Funding_Source": "Unknown",
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

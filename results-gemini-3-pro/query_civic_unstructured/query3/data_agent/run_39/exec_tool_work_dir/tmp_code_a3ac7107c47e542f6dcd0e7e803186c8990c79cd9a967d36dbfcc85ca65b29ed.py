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
    lines = text.split('\n')
    
    current_status = None
    
    # We need to group lines into projects
    # Scan for project starts
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Section Header
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
            
        # Check Project Start
        # Look ahead for (cid:190) Updates or Project Description
        # The pattern seems to be: Name, empty line, (cid:190) Updates...
        # So if lines[i] is name, lines[i+1] is empty, lines[i+2] starts with (cid:190)
        
        is_project = False
        if i + 2 < len(lines):
            check_line = lines[i+2].strip()
            if check_line.startswith('(cid:') and ('Updates' in check_line or 'Project Description' in check_line):
                is_project = True
        
        # Sometimes there might be more empty lines or none?
        # Let's check i+1 too
        if not is_project and i + 1 < len(lines):
            check_line = lines[i+1].strip()
            if check_line.startswith('(cid:') and ('Updates' in check_line or 'Project Description' in check_line):
                 is_project = True
                 
        if is_project and current_status:
            p_name = line
            # Capture text until next project or section
            # For simplicity, capture until next line that looks like a project start or section
            # Actually, just capture everything and let the loop proceed?
            # We need to store the text to check for keywords and "completed" status.
            
            # Start collecting text
            p_text_lines = [line]
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                # Check if next_line is a new section
                if "Capital Improvement Projects (" in next_line:
                    break
                # Check if next_line is a new project
                # Use same logic: does j+2 have (cid:...)
                is_next_project = False
                if j + 2 < len(lines):
                    l2 = lines[j+2].strip()
                    if l2.startswith('(cid:') and ('Updates' in l2 or 'Project Description' in l2):
                        is_next_project = True
                if not is_next_project and j + 1 < len(lines):
                    l1 = lines[j+1].strip()
                    if l1.startswith('(cid:') and ('Updates' in l1 or 'Project Description' in l1):
                        is_next_project = True
                
                if is_next_project and len(next_line) > 0: # New project name found
                    break
                
                p_text_lines.append(lines[j])
                j += 1
            
            p_text = "\n".join(p_text_lines)
            
            # Determine Status
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
            
            i = j # Move to next project
            continue
        
        i += 1

# Filter and Join
final_results = []

for p in projects:
    p_name = p['Project_Name']
    p_text_lower = p['text'].lower()
    p_name_lower = p_name.lower()
    
    is_relevant = any(k in p_name_lower for k in keywords) or any(k in p_text_lower for k in keywords)
    
    p_funding = []
    has_fema_funding = False
    
    for f in funding_data:
        f_name = f['Project_Name']
        f_name_lower = f_name.lower()
        
        match = False
        if f_name_lower == p_name_lower:
            match = True
        elif f_name_lower.startswith(p_name_lower):
            match = True
        elif p_name_lower.startswith(f_name_lower):
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

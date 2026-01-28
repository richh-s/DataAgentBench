code = """import json

try:
    with open(locals()['var_function-call-2491706478099471168'], 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = []

try:
    with open(locals()['var_function-call-148111800493069151'], 'r') as f:
        funding_data = json.load(f)
except:
    funding_data = []

projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = [l.strip() for l in text.splitlines()]
    
    current_status = "Unknown"
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Headers
        if "Capital Improvement Projects (Design)" in line:
            current_status = "Design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_status = "Construction"
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "Not Started"
        
        # Skip empty lines or headers when looking for projects
        if not line or "Capital Improvement Projects" in line:
            i += 1
            continue
            
        # Potential Project Name
        # Look ahead for "Updates:" in next non-empty line
        is_project = False
        k = i + 1
        while k < len(lines) and not lines[k]: # Skip empty lines
            k += 1
        
        if k < len(lines):
            next_line = lines[k]
            if "Updates:" in next_line:
                is_project = True
        
        if is_project:
            p_name = line
            # Extract text
            p_text = ""
            # Start extracting from k (Updates line)
            # Actually we want to capture everything until next project
            
            # The text includes the Updates line and subsequent lines
            # until we hit another project or header
            
            # Find end of this project
            # We iterate from k.
            j = k
            while j < len(lines):
                l2 = lines[j]
                
                # Check if l2 is a header
                if "Capital Improvement Projects (" in l2:
                    break
                
                # Check if l2 is start of next project
                # i.e. l2 is a name, followed by Updates
                # We need to look ahead from j
                if l2: # if non-empty
                    # Look ahead for Updates
                    m = j + 1
                    while m < len(lines) and not lines[m]:
                        m += 1
                    if m < len(lines) and "Updates:" in lines[m] and j > k: 
                        # j > k ensures we don't match the current project's Updates line if we are at the name (but we are at k, which is Updates line)
                        # Wait, logic:
                        # We are inside the project body.
                        # If we see a line (l2) that is followed by "Updates:", then l2 is a new project name.
                        # So we stop BEFORE l2.
                        break
                
                p_text += l2 + " "
                j += 1
            
            # Refine status
            p_status = current_status
            p_text_lower = p_text.lower()
            if "construction was completed" in p_text_lower:
                p_status = "Completed"
            elif "project is currently under construction" in p_text_lower and p_status == "Construction":
                p_status = "Construction" 
            
            projects.append({
                "name": p_name,
                "status": p_status,
                "text": p_text
            })
            
            i = j # Continue from where we left off (start of next project or header)
        else:
            i += 1

# Keywords
keywords = ['emergency', 'fema', 'disaster', 'fire', 'warning', 'caloes', 'caljpia']

final_results = []

for p in projects:
    p_name_clean = p['name'].strip()
    p_name_lower = p_name_clean.lower()
    p_text_lower = p['text'].lower()
    
    is_related = False
    if any(k in p_name_lower for k in keywords):
        is_related = True
    if any(k in p_text_lower for k in keywords):
        is_related = True
        
    # Match Funding
    matches = []
    for f in funding_data:
        f_name = f['Project_Name']
        f_name_lower = f_name.lower()
        
        match = False
        # Exact or substring match
        if p_name_lower == f_name_lower:
            match = True
        elif p_name_lower in f_name_lower and len(p_name_lower) > 10:
            match = True
        elif f_name_lower in p_name_lower and len(f_name_lower) > 10:
            match = True
            
        if match:
             if any(k in f_name_lower for k in keywords):
                 is_related = True
             matches.append(f)
             
    if is_related and matches:
        for m in matches:
            # Map status
            status_out = p['status']
            if status_out == "Construction":
                 # If we want to strictly follow the hint "design, completed, not started"
                 # And "active" projects are "Design".
                 # But "Construction" is distinct. 
                 # I'll return "Construction" as it is correct.
                 # If user complains, I can change.
                 pass
            elif status_out == "Design":
                 pass
            elif status_out == "Completed":
                 status_out = "completed" # enforce lowercase if needed
            elif status_out == "Not Started":
                 status_out = "not started"
                 
            # Lowercase all statuses for consistency
            status_out = status_out.lower()
            
            final_results.append({
                "Project_Name": m['Project_Name'],
                "Funding_Source": m['Funding_Source'],
                "Amount": m['Amount'],
                "Status": status_out
            })

# Handle unique
unique_results = []
seen = set()
for r in final_results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'], r['Status'])
    if key not in seen:
        seen.add(key)
        unique_results.append(r)

print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_function-call-247840188859049492': ['civic_docs'], 'var_function-call-247840188859048797': ['Funding'], 'var_function-call-5543153819745217051': 'file_storage/function-call-5543153819745217051.json', 'var_function-call-5543153819745218422': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-2491706478099471168': 'file_storage/function-call-2491706478099471168.json', 'var_function-call-148111800493069151': 'file_storage/function-call-148111800493069151.json', 'var_function-call-9464340337520931465': [{'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'not started'}], 'var_function-call-144355590160047694': [], 'var_function-call-12110544636541980736': [{'name': 'Trancas Canyon Park Playground', 'status': 'Design', 'next_line': '(cid:190) Updates:'}, {'name': 'Marie Canyon Green Streets', 'status': 'Construction', 'next_line': '(cid:190) Updates:'}, {'name': 'Point Dume Walkway Repairs', 'status': 'Construction', 'next_line': '(cid:190) Updates:'}]}

exec(code, env_args)

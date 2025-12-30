code = """import json

# Access file paths
file_civic = locals()['var_function-call-15771920902434159033']
file_funding = locals()['var_function-call-13220906500236783647']

with open(file_civic, 'r') as f:
    civic_docs = json.load(f)
    
with open(file_funding, 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_status = None
    
    # We will iterate lines.
    # We maintain a buffer of "potential title lines".
    # When we hit a "Start of Project Block" marker (e.g. "Updates:", "Project Description:", "(cid:190)"),
    # we assume the *last* non-empty line in buffer is the Title.
    # The lines before that in the buffer belong to the *previous* project's description.
    
    buffer = []
    
    # But we need to handle Headers changing the status.
    
    # Group lines by status first?
    # Or just track status as we go.
    
    # Let's try:
    # 1. Identify Headers.
    # 2. Identify Project Starts.
    
    # We'll assign a 'tag' to each line: 'header', 'marker', 'content'.
    tagged_lines = []
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        # Check Header
        if "Capital Improvement Projects" in line_stripped or "Disaster Recovery Projects" in line_stripped:
            if "(" in line_stripped and ")" in line_stripped:
                 tagged_lines.append(('header', line_stripped))
            else:
                 tagged_lines.append(('header', line_stripped)) # Treat as header anyway
            continue
            
        # Check Marker
        if line_stripped.startswith("Updates:") or line_stripped.startswith("Project Description:") or "(cid:190)" in line_stripped or line_stripped.startswith("•"):
            tagged_lines.append(('marker', line_stripped))
            continue
            
        tagged_lines.append(('content', line_stripped))

    # Now process tagged lines
    current_status = "unknown"
    current_project = None # {name, desc_lines, status}
    
    final_projects = []
    
    # We iterate. If we see a Header, update status.
    # If we see a Marker, it means the *previous* content line was the Title of a NEW project.
    # And the lines *before* that Title belonged to the PREVIOUS project.
    
    # This assumes Title is always 1 line.
    
    # We need to buffer content lines since the last marker/header.
    content_buffer = []
    
    for tag, text in tagged_lines:
        if tag == 'header':
            # Finish previous project
            if current_project:
                # Add remaining buffer to description?
                # No, buffer belongs to previous project? 
                # Wait. Structure:
                # Header
                # Title
                # Marker
                # Desc
                # Title
                # Marker
                # Desc
                
                # If we hit Header, the `content_buffer` (lines since last marker) 
                # might be [Desc..., Title (of next? No, header ends section)].
                # Actually, Header usually ends the description of the last project.
                # So content_buffer should be appended to current_project description.
                current_project['desc_lines'].extend(content_buffer)
                final_projects.append(current_project)
                current_project = None
                content_buffer = []

            # Update status
            if "(" in text and ")" in text:
                current_status = text.split("(")[1].split(")")[0].lower()
            else:
                current_status = "unknown"
                
        elif tag == 'marker':
            # We found a marker (start of description).
            # The Title should be the last line in content_buffer.
            if content_buffer:
                title = content_buffer.pop() # Take last line as title
                
                # The remaining content_buffer belongs to the *previous* project (if any)
                if current_project:
                    current_project['desc_lines'].extend(content_buffer)
                    final_projects.append(current_project)
                
                # Start new project
                current_project = {
                    "name": title,
                    "desc_lines": [text], # Start desc with marker
                    "status": current_status
                }
                content_buffer = []
            else:
                # Marker without preceding title?
                # Maybe continuation of previous description?
                if current_project:
                    current_project['desc_lines'].append(text)
                else:
                    # Orphan marker?
                    pass
                    
        elif tag == 'content':
            # Avoid Page numbers etc
            if text.startswith("Page") or text.startswith("Agenda Item"):
                continue
            content_buffer.append(text)

    # End
    if current_project:
        current_project['desc_lines'].extend(content_buffer)
        final_projects.append(current_project)

    projects = []
    for p in final_projects:
        name = p['name']
        desc = " ".join(p['desc_lines'])
        status = p['status']
        projects.append({'Project_Name': name, 'description': desc, 'status': status})

final_results = []
seen = set()

for p in projects:
    name = p['Project_Name']
    desc = p['description']
    status = p['status']
    
    if "construction was completed" in desc.lower():
        status = "completed"
    
    text_blob = (name + " " + desc).lower()
    
    # Extract topics/check keywords
    if "emergency" in text_blob or "fema" in text_blob:
        if name in seen:
            continue
        seen.add(name)
        
        funding = funding_map.get(name)
        if not funding:
             candidates = [v for k,v in funding_map.items() if k.startswith(name)]
             if candidates:
                 funding = candidates[0]
        
        f_source = funding['Funding_Source'] if funding else "N/A"
        f_amount = funding['Amount'] if funding else "N/A"
        
        final_results.append({
            "Project_Name": name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-4008715317058091339': 'file_storage/function-call-4008715317058091339.json', 'var_function-call-4008715317058091730': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15771920902434159033': 'file_storage/function-call-15771920902434159033.json', 'var_function-call-13220906500236783647': 'file_storage/function-call-13220906500236783647.json', 'var_function-call-15319677722088380488': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'completed'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'completed'}]}

exec(code, env_args)

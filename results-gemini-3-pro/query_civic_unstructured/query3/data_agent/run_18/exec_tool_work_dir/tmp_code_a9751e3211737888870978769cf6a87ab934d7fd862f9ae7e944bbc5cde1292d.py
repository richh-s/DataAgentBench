code = """import json
import pandas as pd

# Load data
funding_path = locals()['var_function-call-400742028544773800']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

docs_path = locals()['var_function-call-400742028544771257']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

extracted_projects = {}

for doc in docs_data:
    text = doc['text']
    lines = text.split(chr(10))
    
    current_status = None
    current_project = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Identify Section Headers
        if 'Capital Improvement Projects' in line or 'Disaster Recovery Projects' in line:
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'construction_section'
            elif '(Not Started)' in line:
                current_status = 'not started'
            # Check for other statuses if needed
            i += 1
            continue
            
        # Identify Project Name
        # Heuristic: Line is not empty, next non-empty line starts with marker
        if line and current_status:
            # Check if this line is a page header/footer artifact
            if 'Agenda Item' in line or ('Page' in line and 'of' in line):
                i += 1
                continue
            
            # Look ahead
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            is_project = False
            if j < len(lines):
                next_line = lines[j].strip()
                # Markers: (cid:190) is U+00BE (fraction 3/4), often used as bullet?
                # Actually in the preview it showed (cid:190).
                if '(cid:190)' in next_line or next_line.startswith('Updates:'):
                    is_project = True
            
            if is_project:
                # Save previous
                if current_project:
                    extracted_projects[current_project['name']] = current_project
                
                current_project = {
                    'name': line,
                    'status': current_status,
                    'text': ''
                }
                i += 1
                continue

        if current_project:
            current_project['text'] += line + ' '
        
        i += 1
    
    if current_project:
        extracted_projects[current_project['name']] = current_project

# Process statuses and joining
results = []
extracted_map = {k.lower(): v for k, v in extracted_projects.items()}

# Keywords for filtering
keywords = ['emergency', 'fema']

for idx, row in df_funding.iterrows():
    f_name = row['Project_Name']
    f_source = row['Funding_Source']
    f_amount = row['Amount']
    
    # Clean f_name for matching
    base_name = f_name
    suffixes = ['(FEMA Project)', '(CalOES Project)', '(FEMA/CalOES Project)', '(FEMA)', '(CalJPIA Project)']
    for s in suffixes:
        if base_name.endswith(s) or base_name.endswith(s.strip()):
            base_name = base_name.replace(s, '').strip()
    
    match = extracted_map.get(base_name.lower())
    # Try exact match if base didn't work (in case suffix is part of name? unlikely)
    if not match:
        match = extracted_map.get(f_name.lower())
    
    status = 'Unknown'
    text_content = ''
    
    if match:
        raw_status = match['status']
        text_content = match['text']
        
        if raw_status == 'construction_section':
            lower_text = text_content.lower()
            if 'completed' in lower_text and 'construction' in lower_text:
                status = 'completed'
            elif 'notice of completion' in lower_text:
                status = 'completed'
            else:
                status = 'under construction' # or 'design' if forced?
        else:
            status = raw_status
    else:
        # If not found in docs, check if it has FEMA in name
        pass

    # Determine relevance
    is_relevant = False
    # Check name
    if any(k in f_name.lower() for k in keywords):
        is_relevant = True
    # Check text content
    if text_content and any(k in text_content.lower() for k in keywords):
        is_relevant = True
    
    if is_relevant:
        # If status is unknown, but name says FEMA, we should include it.
        # Can we infer status?
        # If we didn't find it in the docs, maybe it's "not started" or "completed" or just missing from report?
        # The prompt says "extract ... status". If extracting fails, maybe "not started"?
        # But if we found no text, we can't be sure.
        # However, if we don't output it, we miss "FEMA" projects.
        # Let's verify if "Unknown" is acceptable.
        # Or maybe I should list it as "not started" if it's in the Funding table but not in the Status Report?
        # That's a big assumption.
        # Let's check the preview again.
        # "Clover Heights Storm Drain (FEMA Project)" -> ID 22.
        # "Clover Heights Storm Drainage Improvements" -> ID 23.
        # The text had "Clover Heights Storm Drainage Improvements".
        # If I matched ID 23 to text, I get status.
        # ID 22 "Clover Heights Storm Drain (FEMA Project)" matches base name "Clover Heights Storm Drain".
        # Text name is "Clover Heights Storm Drainage Improvements".
        # "Drain" vs "Drainage Improvements".
        # My clean logic uses exact string match on base name.
        # "Clover Heights Storm Drain" != "Clover Heights Storm Drainage Improvements".
        # I need fuzzy matching or check for substring?
        # "Clover Heights Storm Drain" is a substring of "Clover Heights Storm Drainage Improvements".
        # I will add a check: if base_name is substring of extracted_name (or vice versa).
        
        if status == 'Unknown':
            # Try fuzzy match
            for ext_name, ext_data in extracted_map.items():
                if base_name.lower() in ext_name or ext_name in base_name.lower():
                    # Found a potential match
                    raw_status = ext_data['status']
                    text_content = ext_data['text']
                    if raw_status == 'construction_section':
                        if 'completed' in text_content.lower() or 'notice of completion' in text_content.lower():
                            status = 'completed'
                        else:
                            status = 'under construction'
                    else:
                        status = raw_status
                    break
        
        results.append({
            "Project_Name": f_name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11967641288845648595': ['Funding'], 'var_function-call-11967641288845651132': ['civic_docs'], 'var_function-call-400742028544773800': 'file_storage/function-call-400742028544773800.json', 'var_function-call-400742028544771257': 'file_storage/function-call-400742028544771257.json'}

exec(code, env_args)

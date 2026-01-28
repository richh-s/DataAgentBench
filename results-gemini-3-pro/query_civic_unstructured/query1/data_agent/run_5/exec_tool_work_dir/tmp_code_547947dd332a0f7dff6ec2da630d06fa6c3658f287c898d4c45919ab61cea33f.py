code = """import json
import re

# Load funding results
with open(locals()['var_function-call-2752695128907644383'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-10485844614487521069'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding for > 50,000
funded_projects = {}
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        pass

# Extract design projects from civic docs
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Normalize text newlines
    text = text.replace('\r\n', '\n')
    
    # Find the section "Capital Improvement Projects (Design)"
    # We look for the start and end of the section
    start_match = re.search(r'Capital Improvement Projects \(Design\)', text, re.IGNORECASE)
    if not start_match:
        continue
        
    start_idx = start_match.end()
    
    # Find the end of the section
    # Next section could be Construction, Not Started, or Disaster Recovery
    # Or just "Capital Improvement Projects ("
    
    # We'll just look for the next "Capital Improvement Projects (" or end of file
    # But wait, the current section is "Capital Improvement Projects (Design)"
    # So we search for "Capital Improvement Projects (" starting after start_idx
    
    # Actually, better to split by logical sections if possible.
    # Let's just look for the next headers:
    next_headers = [
        r'Capital Improvement Projects \(Construction\)',
        r'Capital Improvement Projects \(Not Started\)',
        r'Disaster Recovery Projects',
        r'Public Works Commission' # End of report?
    ]
    
    end_idx = len(text)
    for header in next_headers:
        match = re.search(header, text[start_idx:], re.IGNORECASE)
        if match:
            # We found a next section, check if it's the closest one
            found_idx = start_idx + match.start()
            if found_idx < end_idx:
                end_idx = found_idx
                
    section_text = text[start_idx:end_idx]
    
    # Now extract project names
    # Strategy: split by the bullet point marker for updates
    # The marker in the text preview seems to be `(cid:190)` or unicode char. 
    # In the provided text representation, it shows as `(cid:190) Updates:` or `(cid:190) Project Description:` or just `(cid:190)`
    
    # Let's split by lines and look for lines that are followed by an "Updates" line
    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
    
    for i, line in enumerate(lines):
        # Check if this line is a project name
        # A project name should be followed by a line starting with `(cid:190)` or containing "Updates" or "Project Description"
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if '(cid:190)' in next_line or 'Updates:' in next_line or 'Project Description:' in next_line:
                # This line is likely a project name
                # Clean it
                p_name = line.strip()
                # Remove possible page numbers or garbage
                if len(p_name) > 3 and "Page" not in p_name:
                    design_projects.add(p_name)

# Now match with funded projects
matches = []
# We need to be careful about exact matching.
# Let's create a normalized map for funding
normalized_funding = {k.lower(): k for k in funded_projects.keys()}

matched_count = 0
matched_list = []

for dp in design_projects:
    dp_norm = dp.lower()
    
    # Try exact match
    if dp_norm in normalized_funding:
        original_name = normalized_funding[dp_norm]
        matches.append(original_name)
        matched_count += 1
        continue
        
    # Try with suffix removal?
    # Or check if funding name starts with this project name?
    # Funding name might be "Name (FEMA)"
    # So we check if any funding name starts with dp_norm
    
    found = False
    for fname_norm, original_name in normalized_funding.items():
        if fname_norm.startswith(dp_norm):
            matches.append(original_name)
            matched_count += 1
            found = True
            break # Match one funding record
            
    if not found:
        # Try checking if the text name is contained in the funding name (e.g. project name in text is shorter)
        pass

# Deduplicate matches
matches = list(set(matches))

print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": matches, "extracted_from_text": list(design_projects)}))"""

env_args = {'var_function-call-2752695128907644383': 'file_storage/function-call-2752695128907644383.json', 'var_function-call-2752695128907641442': 'file_storage/function-call-2752695128907641442.json', 'var_function-call-10485844614487521069': 'file_storage/function-call-10485844614487521069.json'}

exec(code, env_args)

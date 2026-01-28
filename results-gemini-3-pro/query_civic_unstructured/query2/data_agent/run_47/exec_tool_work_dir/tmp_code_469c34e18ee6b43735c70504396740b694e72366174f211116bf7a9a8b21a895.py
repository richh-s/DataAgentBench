code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-14770944468380468337'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-14241512510866870290'], 'r') as f:
    civic_docs = json.load(f)

# Helper to check if project is park related
def is_park_related(name, text_block):
    # Check name and text for keywords
    keywords = ['park', 'playground', 'recreation', 'open space', 'trail']
    name_lower = name.lower()
    text_lower = text_block.lower()
    
    # Primary check on name
    for k in keywords:
        if k in name_lower:
            return True
            
    # Secondary check? Maybe risky. The hint says "topic field contains...". 
    # Usually extraction is based on context. 
    # Let's stick to Name keywords first. 
    # "Point Dume Walkway" -> Is Point Dume a park? It is a State Beach/Preserve. 
    # But usually "park-related" implies explicit "Park" in name in these datasets.
    return False

# Helper to check completion
def check_completion(text_block):
    # Look for "completed" and "2022"
    # Phrases: "Construction was completed November 2022", "Construction was completed, November 2022"
    # "Complete Construction: November 2022" (This might be a schedule item, implying future, or past?)
    # If under "Updates" and says "Construction was completed", it's done.
    # If under "Schedule" and says "Complete Construction: [Date]", we need to check if that date is in the past relative to the document date?
    # Document date: March 22, 2023.
    # So "Complete Construction: November 2022" means it is completed.
    
    text_lower = text_block.lower()
    
    # We want "completed" in 2022.
    if '2022' not in text_lower:
        return False
        
    if 'completed' in text_lower or 'complete construction' in text_lower:
        # Check if 2022 is associated with completion
        # Simple check: if both strings exist. 
        # But beware "Design completed 2022, Construction 2023".
        # We want "Construction completed" or "Project completed".
        
        # Split into sentences or lines
        lines = text_block.split('\n')
        for line in lines:
            line_l = line.lower()
            if '2022' in line_l:
                if 'construction' in line_l and ('completed' in line_l or 'complete' in line_l):
                    return True
                if 'project' in line_l and 'completed' in line_l: # "Project completed"
                    return True
                # Specific case: "Construction was completed, November 2022"
                if 'construction was completed' in line_l:
                    return True
                    
    return False

# Parse documents
extracted_projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Iterate to find projects
    # Structure: Project Name line, then (cid:190) Updates: ...
    # We'll look for lines containing "Updates:" or "Project Description:" or "Project Schedule:"
    # And take the preceding lines as Project Name.
    
    # Better approach:
    # Identify block starts.
    # A block start is usually a line that is followed by a line starting with `(cid:190)` or `\uf0be` (if unicode).
    # Let's clean lines first.
    
    clean_lines = [l.strip() for l in lines if l.strip()]
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Check if next line is a header like "Updates:"
        is_project_header = False
        if i + 1 < len(clean_lines):
            next_line = clean_lines[i+1]
            if 'Updates:' in next_line or 'Project Description:' in next_line or 'Project Schedule:' in next_line:
                # This `line` is likely the project name.
                # But check if `line` is also a header?
                # "Capital Improvement Projects (Design)" -> Not a project name.
                # "Capital Improvement Projects (Construction)" -> Not a project name.
                if "Capital Improvement Projects" in line:
                    i += 1
                    continue
                
                project_name = line
                
                # Extract the block
                block_text = ""
                j = i + 1
                while j < len(clean_lines):
                    sub_line = clean_lines[j]
                    # Stop if we hit a new project name candidate
                    # A new project name candidate is a line followed by "Updates:" etc.
                    # But we need to be careful not to trigger on the current block's headers.
                    
                    # If we find a line that looks like a project name (followed by header)
                    # We stop.
                    if j + 1 < len(clean_lines):
                        next_sub = clean_lines[j+1]
                        if ('Updates:' in next_sub or 'Project Description:' in next_sub) and not ('Updates:' in sub_line or 'Project Description:' in sub_line or 'Project Schedule:' in sub_line):
                             # Make sure sub_line is not part of the current block (e.g. a bullet point)
                             # Bullet points often start with (cid:131)
                             if not (sub_line.startswith('(') or sub_line.startswith('\uf0be') or sub_line.startswith('\u2022')):
                                 break
                    
                    block_text += sub_line + "\n"
                    j += 1
                
                extracted_projects.append({
                    'name': project_name,
                    'text': block_text
                })
                
                i = j # Move to next project
                continue
        
        i += 1

# Filter and match
results = []
for p in extracted_projects:
    name = p['name']
    text = p['text']
    
    # Clean name (remove special chars if any)
    name = name.replace('(cid:190)', '').strip()
    
    if is_park_related(name, text):
        if check_completion(text):
            results.append(p)

# Print intermediate result to debug
print("__DEBUG_PROJECTS__:")
print(json.dumps(results, indent=2))

# Join with funding
# Need exact match on Project_Name
total_funding = 0
matched_projects = []

funding_df = pd.DataFrame(funding_data)

for p in results:
    p_name = p['name']
    # Try exact match
    match = funding_df[funding_df['Project_Name'] == p_name]
    
    if match.empty:
        # Try stripping text?
        # Sometimes names have extra spaces
        match = funding_df[funding_df['Project_Name'].str.strip() == p_name.strip()]
        
    if not match.empty:
        amount = match['Amount'].sum() # Should be one record, but sum if multiple
        total_funding += amount
        matched_projects.append({'name': p_name, 'amount': int(amount)})
    else:
        # Debug unmatched
        matched_projects.append({'name': p_name, 'amount': 0, 'status': 'Unmatched'})

print("__RESULT__:")
print(json.dumps({'matched': matched_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-18374819534709684417': 'file_storage/function-call-18374819534709684417.json', 'var_function-call-14770944468380468337': 'file_storage/function-call-14770944468380468337.json', 'var_function-call-14241512510866870290': 'file_storage/function-call-14241512510866870290.json'}

exec(code, env_args)

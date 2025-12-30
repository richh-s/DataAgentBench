code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-15201244734315748547'], 'r') as f:
    funding_data = json.load(f)

# Group funding by Project Name
funding_map = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    amount = int(entry['Amount'])
    if name not in funding_map:
        funding_map[name] = 0
    funding_map[name] += amount

# Load Civic Docs
with open(locals()['var_function-call-15201244734315749312'], 'r') as f:
    civic_docs = json.load(f)

projects_found = []

def is_disaster(text, name):
    keywords = ['FEMA', 'CalOES', 'Disaster', 'Woolsey', 'Fire', 'Emergency']
    text_check = any(k.lower() in text.lower() for k in keywords)
    name_check = any(k.lower() in name.lower() for k in keywords)
    return text_check or name_check

def extract_start_date(text):
    # Look for "Begin Construction: <Date>"
    # Or "Start Date: <Date>"
    # Or "Schedule: ... Begin Construction: <Date>"
    # The text might have newlines.
    
    # Common patterns in the preview:
    # (cid:131) Begin Construction: Fall 2023
    # (cid:131) Begin construction: April 2023
    
    matches = re.findall(r'Begin [Cc]onstruction[:\s]+([A-Za-z0-9\s,]+)', text)
    if not matches:
        matches = re.findall(r'Start [Dd]ate[:\s]+([A-Za-z0-9\s,]+)', text)
    
    # Clean up matches
    cleaned_dates = []
    for m in matches:
        # Take the first few words, e.g., "Fall 2023", "April 2023"
        # Sometimes it might pick up more text.
        # Just check if "2022" is in it.
        if '2022' in m:
            return m
    return None

# Parse Documents
for doc in civic_docs:
    text = doc['text']
    # Split text into project blocks
    # Strategy: Find lines that look like project names.
    # From preview, project names are often followed by "(cid:190) Updates:"
    # or just "(cid:190)".
    # Or use the "Capital Improvement Projects" headers to delimit sections?
    
    # Let's try splitting by the bullet point "(cid:190)" which seems to start a section for a project?
    # Actually, "(cid:190)" is used for "Updates:", "Project Schedule:", "Project Description:".
    # The line *before* the first "(cid:190)" of a block is likely the Project Name.
    
    lines = text.split('\n')
    
    current_project_name = None
    current_project_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is followed by a "(cid:190)" line (ignoring empty lines)
        # Scan ahead
        is_title = False
        for j in range(i + 1, min(i + 5, len(lines))):
            next_line = lines[j].strip()
            if not next_line:
                continue
            if next_line.startswith('(cid:190)') or next_line.startswith('¾'): # Encoding might vary
                # Found a bullet. The current line is likely the title if it's not a bullet itself.
                if not line.startswith('(cid:190)') and not line.startswith('¾'):
                    is_title = True
                break
            else:
                # If we hit text that is not a bullet, then the current line probably isn't a title
                # unless the bullet is further down?
                # Actually, in the preview:
                # Project Name
                # (cid:190) Updates:
                # So the immediate next non-empty line starts with (cid:190).
                if next_line.startswith('(cid:190)') or next_line.startswith('¾'):
                     if not line.startswith('(cid:190)') and not line.startswith('¾'):
                        is_title = True
                break
        
        if is_title:
            # Save previous project
            if current_project_name:
                full_block = "\n".join(current_project_text)
                projects_found.append({
                    'name': current_project_name,
                    'text': full_block
                })
            
            current_project_name = line
            current_project_text = []
        else:
            if current_project_name:
                current_project_text.append(line)
    
    # Add last project
    if current_project_name:
        full_block = "\n".join(current_project_text)
        projects_found.append({
            'name': current_project_name,
            'text': full_block
        })

# Filter and Match
results = []
for p in projects_found:
    name = p['name']
    text = p['text']
    
    # Check start date
    start_date = extract_start_date(text)
    if not start_date:
        continue
        
    # Check disaster
    # Check if name maps to funding and if that funding name implies disaster
    # Or if text implies disaster
    
    # Try to match name in funding_map
    # Exact match?
    funding_name = None
    if name in funding_map:
        funding_name = name
    else:
        # Try fuzzy or partial?
        # Maybe the extracted name has extra spaces or chars?
        # Let's try to find a close match in funding keys
        pass
    
    is_dis = is_disaster(text, name)
    
    if is_dis and start_date:
        amount = 0
        if funding_name:
            amount = funding_map[funding_name]
        else:
             # Try to find in funding map
             # e.g. text name: "Clover Heights Storm Drainage Improvements"
             # funding key: "Clover Heights Storm Drainage Improvements" -> Match
             pass
        
        results.append({
            'name': name,
            'start_date': start_date,
            'amount': amount,
            'is_disaster': is_dis
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15201244734315748547': 'file_storage/function-call-15201244734315748547.json', 'var_function-call-15201244734315749312': 'file_storage/function-call-15201244734315749312.json'}

exec(code, env_args)

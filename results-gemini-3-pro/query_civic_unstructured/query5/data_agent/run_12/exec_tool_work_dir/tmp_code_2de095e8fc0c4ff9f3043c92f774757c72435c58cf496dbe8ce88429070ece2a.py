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
    matches = re.findall(r'Begin [Cc]onstruction[:\s]+([A-Za-z0-9\s,]+)', text)
    if not matches:
        matches = re.findall(r'Start [Dd]ate[:\s]+([A-Za-z0-9\s,]+)', text)
    
    for m in matches:
        if '2022' in m:
            return m
    return None

# Parse Documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a title
        # A title is followed by a line starting with (cid:190)
        is_title = False
        
        # Look ahead for the bullet
        # We search a few lines ahead because sometimes there are blank lines
        found_bullet = False
        for j in range(i + 1, min(i + 5, len(lines))):
            next_l = lines[j].strip()
            if not next_l:
                continue
            if next_l.startswith('(cid:190)') or next_l.startswith('\u00be'): 
                found_bullet = True
            break # Stop at first non-empty line
            
        if found_bullet and not (line.startswith('(cid:190)') or line.startswith('\u00be')):
             is_title = True
        
        if is_title:
            if current_project_name:
                projects_found.append({
                    'name': current_project_name,
                    'text': "\n".join(current_project_text)
                })
            current_project_name = line
            current_project_text = []
        else:
            if current_project_name:
                current_project_text.append(line)

    if current_project_name:
        projects_found.append({
            'name': current_project_name,
            'text': "\n".join(current_project_text)
        })

# Match and Calculate
results = []
matched_names = []

for p in projects_found:
    name = p['name']
    text = p['text']
    
    start_date = extract_start_date(text)
    
    # Try to match name in funding_map
    funding_name = None
    if name in funding_map:
        funding_name = name
    else:
        # Try simple cleaning?
        # e.g. "Project Name (Design)" -> "Project Name"
        # Or checking if name is a substring of funding key or vice versa
        pass

    # Check for disaster keywords
    disaster = is_disaster(text, name)
    
    # If we have a start date in 2022 and it is disaster related
    if start_date and disaster:
        amount = 0
        if funding_name:
            amount = funding_map[funding_name]
        else:
            # Fallback matching
            # Check if p['name'] is in funding_map keys?
            # Or if funding_map keys are in p['name']?
            # The preview showed Funding DB names like "Clover Heights Storm Drain (FEMA Project)"
            # Text name: "Clover Heights Storm Drainage Improvements"
            # It's tricky.
            # Let's list potential candidates from funding_map
            pass
        
        results.append({
            'name': name,
            'funding_name': funding_name,
            'start_date': start_date,
            'amount': amount,
            'is_disaster': disaster
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15201244734315748547': 'file_storage/function-call-15201244734315748547.json', 'var_function-call-15201244734315749312': 'file_storage/function-call-15201244734315749312.json'}

exec(code, env_args)

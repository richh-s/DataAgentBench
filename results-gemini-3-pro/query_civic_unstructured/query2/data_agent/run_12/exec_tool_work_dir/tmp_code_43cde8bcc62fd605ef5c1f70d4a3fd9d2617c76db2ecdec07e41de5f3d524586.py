code = """import json

# keys
key_docs = 'var_function-call-12716671968640832607'
key_fund = 'var_function-call-12716671968640831510'

# Load
with open(locals()[key_docs], 'r') as f:
    civic_docs = json.load(f)
text = civic_docs[0]['text']

with open(locals()[key_fund], 'r') as f:
    funding_data = json.load(f)
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

lines = text.split('\n')
projects = []
current_project = None
buffer_text = []

# Marker string check
def is_marker(line):
    s = line.strip()
    # Check for (cid:190)
    if '(cid:190)' in s: return True
    # Check for unicode char 190
    if chr(190) in s: return True
    return False

for i, line in enumerate(lines):
    if is_marker(line):
        s = line.strip()
        # Clean marker
        clean_s = s.replace('(cid:190)', '').replace(chr(190), '').strip()
        
        # Check previous line for project name
        prev_idx = i - 1
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
            
        if prev_idx >= 0:
            potential_name = lines[prev_idx].strip()
            
            # Heuristics
            ignore = False
            if is_marker(potential_name): ignore = True
            if "Agenda Item" in potential_name: ignore = True
            if "Page " in potential_name and " of " in potential_name: ignore = True
            if "Capital Improvement Projects" in potential_name: ignore = True
            
            # Additional heuristic: Name should correspond to a key in funding_map?
            # Or at least look like a name.
            # But we only want to switch projects if it really looks like a new header.
            # The structure is Name \n Marker.
            # So if we see a marker, and the previous line is a candidate name, we switch.
            
            if not ignore:
                # Save previous
                if current_project:
                    projects.append({'name': current_project, 'text': "\n".join(buffer_text)})
                current_project = potential_name
                buffer_text = []

    if current_project:
        buffer_text.append(line)

if current_project:
    projects.append({'name': current_project, 'text': "\n".join(buffer_text)})

# Filter
target_projects = []
total_funding = 0
keywords = ['park', 'playground']

for p in projects:
    name = p['name']
    details = p['text']
    
    if not any(k in name.lower() for k in keywords):
        continue
    
    # Check completed 2022
    # Logic: look for line with 'completed' and '2022'
    relevant = False
    for l in details.split('\n'):
        l_lower = l.lower()
        if 'completed' in l_lower and '2022' in l_lower:
            relevant = True
            break
            
    if relevant:
        # Get funding
        # Try exact match first
        amount = funding_map.get(name, 0)
        if amount == 0:
            # Try fuzzy match or strip extra spaces
            # Check if name is in funding_map keys
            pass 
        
        target_projects.append({'name': name, 'amount': amount})
        total_funding += amount

print("__RESULT__:")
print(json.dumps({'target_projects': target_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-12716671968640832607': 'file_storage/function-call-12716671968640832607.json', 'var_function-call-12716671968640831510': 'file_storage/function-call-12716671968640831510.json'}

exec(code, env_args)

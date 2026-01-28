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

# Split lines
lines = text.split(chr(10))
projects = []
current_project = None
buffer_text = []

def is_marker(line):
    s = line.strip()
    if '(cid:190)' in s: return True
    if chr(190) in s: return True
    return False

for i, line in enumerate(lines):
    if is_marker(line):
        s = line.strip()
        prev_idx = i - 1
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
            
        if prev_idx >= 0:
            potential_name = lines[prev_idx].strip()
            
            ignore = False
            if is_marker(potential_name): ignore = True
            if "Agenda Item" in potential_name: ignore = True
            if "Page " in potential_name and " of " in potential_name: ignore = True
            if "Capital Improvement Projects" in potential_name: ignore = True
            
            if not ignore:
                if current_project:
                    projects.append({'name': current_project, 'text': chr(10).join(buffer_text)})
                current_project = potential_name
                buffer_text = []

    if current_project:
        buffer_text.append(line)

if current_project:
    projects.append({'name': current_project, 'text': chr(10).join(buffer_text)})

target_projects = []
total_funding = 0
keywords = ['park', 'playground']

for p in projects:
    name = p['name']
    details = p['text']
    
    # Check Topic in Name OR Details
    is_park = False
    if any(k in name.lower() for k in keywords):
        is_park = True
    elif any(k in details.lower() for k in keywords):
        # Be careful: "parking" contains "park".
        # Check whole word 'park'?
        # Regex \bpark\b or \bplayground\b
        # Or simple check and verify?
        # "Car park" -> Park? No.
        # "Park" usually refers to public park.
        # Let's check what matched.
        is_park = True
    
    if not is_park:
        continue
    
    # Check completed 2022
    relevant = False
    for l in details.split(chr(10)):
        l_lower = l.lower()
        if 'completed' in l_lower and '2022' in l_lower:
            relevant = True
            # Check for negation or future tense?
            # "expected to be completed in 2022" -> might be.
            # "Construction was completed November 2022" -> yes.
            # "Design completed 2022" -> Status "Completed" usually refers to the project status.
            # The prompt asks for "projects that were completed in 2022".
            # This usually means construction completed.
            # "Complete Design: Summer 2023" -> Not project completion.
            # If a line says "Complete Design: ... 2022", is the project completed? No, just design.
            # The header "Capital Improvement Projects (Construction)" lists projects under construction or completed.
            # Completed projects say "Construction was completed...".
            # So I should look for "Construction was completed" or similar.
            
            if "complete design" in l_lower:
                relevant = False # Reset if it's just design
            elif "construction" in l_lower and "completed" in l_lower:
                relevant = True
            elif "construction was completed" in l_lower:
                relevant = True
            else:
                # If just "completed 2022" and not design?
                # "Bluffs Park Shade Structure ... Construction was completed November 2022"
                pass
            break
            
    if relevant:
        amount = funding_map.get(name, 0)
        target_projects.append({'name': name, 'amount': amount})
        total_funding += amount

print("__RESULT__:")
print(json.dumps({'target_projects': target_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-12716671968640832607': 'file_storage/function-call-12716671968640832607.json', 'var_function-call-12716671968640831510': 'file_storage/function-call-12716671968640831510.json', 'var_function-call-6699042011993104825': {'target_projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}], 'total_funding': 21000}}

exec(code, env_args)

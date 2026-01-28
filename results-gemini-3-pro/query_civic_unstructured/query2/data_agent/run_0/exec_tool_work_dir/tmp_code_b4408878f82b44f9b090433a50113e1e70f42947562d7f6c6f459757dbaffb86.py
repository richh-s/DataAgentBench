code = """import json
import re

# Load funding data
funding_path = locals()['var_function-call-14868683301931886144']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_map = {}
for record in funding_data:
    p_name = record['Project_Name'].strip()
    amount = record['Amount']
    # Ensure amount is int
    if isinstance(amount, str):
        amount = int(amount)
        
    if p_name in funding_map:
        funding_map[p_name] += amount
    else:
        funding_map[p_name] = amount

# Load civic docs
docs_path = locals()['var_function-call-8294190329449223734']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = "\n".join([doc['text'] for doc in civic_docs])
lines = full_text.split('\n')

found_projects = []
current_lines = []
current_proj_name = None

# Known projects set for fast lookup
known_projects_set = set(funding_map.keys())

for line in lines:
    line_stripped = line.strip()
    
    # Check if this line is a project name
    if line_stripped in known_projects_set:
        # Save previous
        if current_proj_name:
            found_projects.append({'name': current_proj_name, 'text': "\n".join(current_lines)})
        
        current_proj_name = line_stripped
        current_lines = []
    else:
        if current_proj_name:
            current_lines.append(line_stripped)

# Add last
if current_proj_name:
    found_projects.append({'name': current_proj_name, 'text': "\n".join(current_lines)})

target_projects = []
total_funding = 0

for proj in found_projects:
    p_name = proj['name']
    p_text = proj['text'].lower()
    
    # Check is_park
    is_park = False
    if 'park' in p_name.lower():
        is_park = True
    else:
        # Check description for "park" as a word or "playground"
        if re.search(r'\bpark\b', p_text) or re.search(r'\bplayground\b', p_text):
            is_park = True
            
    # Check completed in 2022
    # Patterns: "completed, november 2022", "complete construction: november 2022", "completed november 2022"
    is_completed_2022 = False
    if '2022' in p_text:
        # Look for completion keywords near 2022?
        # Simple check: if "complete" and "2022" are in the text block, 
        # and specifically "complete construction" or "completed" associated with 2022.
        # But wait, "Complete Design: Summer 2022" is NOT completed construction.
        # So we must look for "Construction" AND "Complete" AND "2022" in a way that implies finish.
        
        # Valid phrases from preview:
        # "Construction was completed November 2022"
        # "Construction was completed, November 2022"
        # "Complete Construction: November 2022" (Hypothetically, actually preview shows "Complete Construction: April 2023")
        
        # So we need "complete construction" or "construction was completed" followed by date containing 2022.
        # Or "Notice of completion filed ... 2023" (implies completed recently, maybe late 2022).
        
        # Let's search for "completed" and "2022" in the same line or proximity.
        # Line-by-line check in p_text
        for subline in p_text.split('\n'):
            if '2022' in subline:
                if 'construction was completed' in subline or 'complete construction' in subline or 'construction completed' in subline:
                    is_completed_2022 = True
                    break
    
    if is_park and is_completed_2022:
        target_projects.append(p_name)
        total_funding += funding_map[p_name]

print("__RESULT__:")
print(json.dumps({
    "target_projects": target_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-8294190329449223734': 'file_storage/function-call-8294190329449223734.json', 'var_function-call-14868683301931886144': 'file_storage/function-call-14868683301931886144.json'}

exec(code, env_args)

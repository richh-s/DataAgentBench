code = """import json

# Load data
with open(locals()['var_function-call-5680067546526520620'], 'r') as f:
    civic_data = json.load(f)
    
with open(locals()['var_function-call-10418813875074106507'], 'r') as f:
    funding_data = json.load(f)

text = civic_data[0]['text']

# Base names from funding
base_names = set()
for r in funding_data:
    name = r['Project_Name']
    if "(" in name:
        base = name.split("(")[0].strip()
    else:
        base = name.strip()
    base_names.add(base)

lines = text.splitlines()
projects = []
current_project = None
current_section = ""
current_block = []

for line in lines:
    line = line.strip()
    if not line: continue
    
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
        current_section = line
        continue
        
    # Check match
    is_project = False
    lower_line = line.lower()
    for base in base_names:
        if lower_line == base.lower():
            is_project = True
            matched_name = base
            break
    
    if is_project:
        if current_project:
            projects.append({
                "name": current_project,
                "section": current_section,
                "text": " ".join(current_block)
            })
        current_project = matched_name
        current_block = []
    else:
        if current_project:
            current_block.append(line)

if current_project:
    projects.append({
        "name": current_project,
        "section": current_section,
        "text": " ".join(current_block)
    })

# Analyze projects
final_projects = []
for p in projects:
    txt = p['text']
    
    start_year = None
    
    # Check for "Begin Construction" with 2022
    if "Begin Construction" in txt:
        idx = txt.find("Begin Construction")
        snippet = txt[idx:idx+50]
        if "2022" in snippet:
            start_year = 2022
            
    # Check "Construction was completed" in 2022
    # If completed in 2022, did it start in 2022?
    # e.g. "Bluffs Park Shade Structure", completed Nov 2022.
    # It's a small project (shade structure), likely started in 2022.
    # "Marie Canyon Green Streets", completed Jan 2023. Likely started 2022.
    # "Broad Beach Road Water Quality Repair", completed Nov 2022. Likely started 2022.
    # I'll tentatively include them if no other start date contradicts.
    if "Construction was completed" in txt:
        idx = txt.find("Construction was completed")
        snippet = txt[idx:idx+50]
        if "2022" in snippet:
            # We'll flag this as potentially 2022 start
            if start_year is None:
                start_year = 2022 # Assume short duration
    
    # Check name
    if "2022" in p['name']:
        start_year = 2022

    # Determine type
    is_disaster = False
    if "Disaster" in p['section']:
        is_disaster = True
    
    final_projects.append({
        "name": p['name'],
        "start_year": start_year,
        "is_disaster": is_disaster,
        "section": p['section'],
        "text_preview": txt[:100]
    })

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json'}

exec(code, env_args)

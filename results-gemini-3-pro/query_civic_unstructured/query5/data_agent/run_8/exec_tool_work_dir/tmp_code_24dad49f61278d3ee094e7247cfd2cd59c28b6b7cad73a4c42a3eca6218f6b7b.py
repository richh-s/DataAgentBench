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
    if '(' in name:
        base = name.split('(')[0].strip()
    else:
        base = name.strip()
    base_names.add(base)

lines = text.split('\n')
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
    for base in base_names:
        if line.lower() == base.lower():
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
    
    # Check start year
    start_year = None
    
    # 1. Check for "Begin Construction: <Season> <Year>"
    # We look for 2022
    if "Begin Construction" in txt:
        idx = txt.find("Begin Construction")
        snippet = txt[idx:idx+50]
        if "2022" in snippet:
            start_year = 2022
            
    # 2. Check "Construction was completed ... 2022" -> Likely started in 2022 if short project, or before.
    # Text says: "Construction was completed November 2022. Notice of completion filed January 2023"
    # If completed in 2022, is it a project that "started in 2022"?
    # Maybe. Or maybe started in 2021.
    # Let's check if there is an explicit start date.
    # But usually, if it's completed in 2022, it was active in 2022.
    # The query is "started in 2022".
    # I will look for "Started" or "Begin".
    
    # 3. Check name
    if "2022" in p['name']:
        start_year = 2022
        
    # 4. Check "Updates: ... started ... 2022"
    # This is harder to parse without regex, but simple check:
    if "started" in txt.lower() and "2022" in txt:
        # Check proximity?
        pass

    # Determine type
    is_disaster = False
    if "Disaster" in p['section']:
        is_disaster = True
    
    # Also check if matching funding record has FEMA/CalOES
    # We need to link back to funding records.
    
    final_projects.append({
        "name": p['name'],
        "start_year": start_year,
        "is_disaster": is_disaster,
        "text_preview": txt[:200]
    })

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json'}

exec(code, env_args)

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

# Now process projects to find start dates and type
results = []
for p in projects:
    txt = p['text']
    # Look for dates
    # Simple check for '2022'
    has_2022 = '2022' in txt or '2022' in p['name']
    
    # Try to find specific start indicators
    # We want "started in 2022"
    # Patterns: "Begin Construction: ... 2022", "Construction was completed ... 2022" (implies start <= 2022)
    # "Advertise: ... 2022" (start of procurement)
    
    start_year = None
    
    # Check for "Begin Construction: <Date>"
    if "Begin Construction" in txt:
        idx = txt.find("Begin Construction")
        snippet = txt[idx:idx+50]
        if "2022" in snippet:
            start_year = 2022
        elif "2023" in snippet:
            start_year = 2023
            
    # Check for "Construction was completed"
    if "Construction was completed" in txt:
        idx = txt.find("Construction was completed")
        snippet = txt[idx:idx+50]
        if "2022" in snippet:
            # Completed in 2022 -> Started in or before 2022.
            # Does "started in 2022" include projects started before 2022?
            # Usually "projects that started in 2022" means start_date >= 2022-01-01 AND start_date <= 2022-12-31.
            # If completed in 2022, it might have started in 2021.
            # I need to be careful.
            # However, for small civic projects, they often start and end in same year.
            # Let's verify start if possible.
            pass

    # Check for "Updates: ... started"
    
    # Check for project name containing 2022
    if "2022" in p['name']:
        start_year = 2022
        
    results.append({
        "name": p['name'],
        "section": p['section'],
        "start_year": start_year,
        "text_preview": txt[:100]
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5680067546526520620': 'file_storage/function-call-5680067546526520620.json', 'var_function-call-10418813875074106507': 'file_storage/function-call-10418813875074106507.json'}

exec(code, env_args)

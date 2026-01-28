code = """import json
import pandas as pd
import re

funding_path = locals()['var_function-call-14443830636332700640']
docs_path = locals()['var_function-call-14443830636332701107']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(float)

def get_base_name(name):
    # Remove suffix in parens at the end
    base = re.sub(r'\s*\(.*?\)$', '', name)
    return base.strip()

project_map = {}
for _, row in df_funding.iterrows():
    full_name = row['Project_Name']
    base_name = get_base_name(full_name)
    if base_name not in project_map:
        project_map[base_name] = []
    project_map[base_name].append(row)

base_project_names = set(project_map.keys())
all_project_names = set(df_funding['Project_Name'].tolist())

extracted_projects = []

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_block = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        is_new_project = False
        matched_name = None
        
        # Check against base names
        if line in base_project_names:
            is_new_project = True
            matched_name = line
        elif line in all_project_names:
            is_new_project = True
            matched_name = get_base_name(line)
        
        if is_new_project:
            if current_project:
                extracted_projects.append({
                    'name': current_project,
                    'block': "\n".join(current_block)
                })
            current_project = matched_name
            current_block = []
        else:
            if current_project:
                current_block.append(line)
    
    if current_project:
        extracted_projects.append({
            'name': current_project,
            'block': "\n".join(current_block)
        })

def parse_year(text):
    match = re.search(r'20\d\d', text)
    if match:
        return match.group(0)
    return None

projects_started_2022 = []

for p in extracted_projects:
    name = p['name']
    block = p['block']
    
    start_year = None
    # Look for start indicators
    # 1. Begin Construction
    m = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9 ]+)', block)
    if m:
        start_year = parse_year(m.group(1))
    
    # 2. Start
    if not start_year:
        m = re.search(r'Start:?\s*([A-Za-z0-9 ]+)', block)
        if m:
            start_year = parse_year(m.group(1))
            
    # 3. Advertise (if no construction start found, advertise implies start of project activity)
    if not start_year:
        m = re.search(r'Advertise:?\s*([A-Za-z0-9 ]+)', block)
        if m:
            start_year = parse_year(m.group(1))

    # Check for completed date if start date not found?
    # If "Construction was completed... 2022", it started <= 2022.
    # But strictly "started in 2022" might exclude projects started in 2021.
    # Let's rely on Start/Begin/Advertise.

    # Identify if disaster
    # Check text keywords
    is_disaster_text = False
    disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey', 'Fire', 'Disaster', 'Emergency']
    for k in disaster_keywords:
        if k in block or k.upper() in block: # simple check
            is_disaster_text = True
            break
            
    # Check funding names
    has_disaster_funding = False
    funding_recs = project_map.get(name, [])
    for fr in funding_recs:
        fname = fr['Project_Name']
        if 'FEMA' in fname or 'CalOES' in fname or 'CalJPIA' in fname:
            has_disaster_funding = True
            break
            
    is_disaster = is_disaster_text or has_disaster_funding
    
    if start_year == '2022' and is_disaster:
        projects_started_2022.append(name)

unique_names = set(projects_started_2022)
total_amount = 0.0
for name in unique_names:
    recs = project_map.get(name, [])
    for r in recs:
        total_amount += r['Amount']

print("__RESULT__:")
print(json.dumps({"total_funding": total_amount, "projects": list(unique_names)}))"""

env_args = {'var_function-call-14443830636332701107': 'file_storage/function-call-14443830636332701107.json', 'var_function-call-14443830636332700640': 'file_storage/function-call-14443830636332700640.json'}

exec(code, env_args)

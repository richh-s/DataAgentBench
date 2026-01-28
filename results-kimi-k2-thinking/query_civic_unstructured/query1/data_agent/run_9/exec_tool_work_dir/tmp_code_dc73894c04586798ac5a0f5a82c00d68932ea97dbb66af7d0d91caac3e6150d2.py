code = """import json, re

# Load funding data
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:8']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map for projects > $50k
funding_map = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        project_name = record['Project_Name'].lower().strip()
        funding_map[project_name] = amount

# Extract capital design projects from civic docs
all_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text or 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Get design section
    start_marker = 'Capital Improvement Projects (Design)'
    end_markers = ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'Capital Improvement Projects (Not Started)']
    
    design_section = text.split(start_marker)[1]
    for marker in end_markers:
        if marker in design_section:
            design_section = design_section.split(marker)[0]
            break
    
    # Extract potential project names
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) < 8:
            continue
        
        # Skip unwanted lines
        if any(x in line for x in ['•', '(cid:', 'Page', 'Agenda Item', 'Project Schedule', 'Updates:', 'Complete Design', 'Advertise', 'Construction']):
            continue
        
        # Check if line looks like a project name
        if line[0].isupper() and not line.isupper():
            # Clean trailing punctuation
            clean_line = re.sub(r'[^a-zA-Z0-9\s&\-\/\(\)]$', '', line)
            if len(clean_line) > 10:
                all_design_projects.append(clean_line)

# Deduplicate
design_projects = []
seen = set()
for proj in all_design_projects:
    proj_lower = proj.lower()
    if proj_lower not in seen:
        design_projects.append(proj)
        seen.add(proj_lower)

# Find matches with funding
count = 0
matched_projects = []
seen_matches = set()

for proj in design_projects:
    proj_key = proj.lower()
    # Check for direct match
    if proj_key in funding_map:
        if proj not in seen_matches:
            count += 1
            seen_matches.add(proj)
            continue
    
    # Check for project name without suffix
    base_name = re.sub(r'\s*\([^)]*\)$', '', proj).lower().strip()
    if base_name in funding_map and proj not in seen_matches:
        count += 1
        seen_matches.add(proj)
        continue

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

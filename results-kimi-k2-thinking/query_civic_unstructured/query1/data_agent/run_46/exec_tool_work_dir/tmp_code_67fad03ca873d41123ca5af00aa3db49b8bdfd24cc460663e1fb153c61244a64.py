code = """import json, re, os

# Get file paths from variables
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:8']

# Load funding data
funding_data = json.load(open(funding_file))

# Load civic documents
civic_docs = json.load(open(civic_file))

# Build funding map for amounts > $50000
funding_names = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        name = record['Project_Name']
        # Store original name for matching
        funding_names[name.lower()] = name

# Extract capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find end of this section
    design_end = text.find('Capital Improvement Projects (Construction)', design_start)
    if design_end == -1:
        design_end = text.find('Disaster Recovery Projects', design_start)
    if design_end == -1:
        design_end = len(text)
    
    # Extract section and find project names
    section_text = text[design_start:design_end]
    lines = section_text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Filter potential project names
        if len(line) < 10 or line.startswith('(') or 'Capital Improvement' in line:
            continue
        
        # Skip disaster projects
        if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
            continue
        
        # Check if followed by project details
        if i + 1 < len(lines):
            next_chunk = '\n'.join(lines[i+1:min(i+5, len(lines))])
            if 'Updates:' in next_chunk or 'Schedule:' in next_chunk:
                # This is likely a capital project name
                keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']
                if any(kw in line.lower() for kw in keywords):
                    design_projects.add(line)

# Count projects with matching funding > $50000
matched_count = 0
matched_list = []

for project in design_projects:
    project_lower = project.lower()
    
    # Check for direct match or partial match
    for funding_name in funding_names:
        if (project_lower in funding_name or 
            funding_name in project_lower or
            project_lower.replace('project', '').strip() in funding_name):
            matched_count += 1
            matched_list.append(project)
            break

# Return final count
output = {'count': matched_count}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

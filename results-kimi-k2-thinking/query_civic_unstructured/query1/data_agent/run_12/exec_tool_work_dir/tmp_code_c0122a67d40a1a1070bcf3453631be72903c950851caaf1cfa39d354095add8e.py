code = """import json

# Get the stored results
funding_result = var_functions.query_db:0
civic_result = var_functions.query_db:1

# Read funding data
with open(funding_result, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data  
with open(civic_result, 'r') as f:
    civic_docs_data = json.load(f)

# Build funding lookup table
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[project_name] = amount

# Find design phase capital projects
design_projects_found = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Check for design section of capital projects
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker in text:
        section_start = text.find(design_marker) + len(design_marker)
        remaining_text = text[section_start:]
        
        # Find where section ends
        section_end = len(remaining_text)
        for next_section in ['Capital Improvement Projects (Construction)', 
                           'Capital Improvement Projects (Not Started)',
                           'Disaster Recovery Projects']:
            pos = remaining_text.find(next_section)
            if pos > 0 and pos < section_end:
                section_end = pos
        
        design_section = remaining_text[:section_end]
        
        # Look for project names
        for line in design_section.split('\n'):
            line = line.strip()
            
            if not line or len(line) < 5:
                continue
                
            # Skip descriptive lines
            if any(x in line for x in ['Updates:', 'Schedule:', 'Complete Design', 'Advertise', 'Begin Construction']):
                continue
                
            # Skip symbols
            if line[0] in '(-•' or line.startswith('cid:'):
                continue
            
            # Check if funded project > 50000
            if line in funding_lookup:
                design_projects_found.append(line)

# Count unique projects
unique_projects = list(set(design_projects_found))

# Create output
output = json.dumps({
    'count': len(unique_projects),
    'projects': unique_projects
})

print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)

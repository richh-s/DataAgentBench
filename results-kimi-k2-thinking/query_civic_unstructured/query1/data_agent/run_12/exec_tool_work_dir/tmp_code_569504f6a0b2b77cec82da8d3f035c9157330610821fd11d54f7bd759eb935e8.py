code = """import json
import re

# Access the stored data
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:1']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Create funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name']] = amount

# Find capital projects with design status
capital_design_projects = set()

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find Capital Improvement Projects (Design) section
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker not in text:
        continue
    
    # Extract design section
    start_idx = text.index(design_marker) + len(design_marker)
    design_section = text[start_idx:]
    
    # Find end of section
    section_end = float('inf')
    for marker in [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)', 
        'Disaster Recovery Projects',
        'Construction Projects',
        '\n\n'
    ]:
        pos = design_section.find(marker)
        if pos > 0 and pos < section_end:
            section_end = pos
    
    if section_end != float('inf'):
        design_section = design_section[:section_end]
    
    # Extract project names
    for line in design_section.split('\n'):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Skip headers and markers
        skip_patterns = ['Capital Improvement', '(cid:', 'Updates:', 'Schedule:', 'Complete Design:', 'Advertise:' , 'Begin Construction', 'Project Description:', '•', '-', '(']
        if any(pattern in line for pattern in skip_patterns) or line.startswith('('):
            continue
        
        # Check if this is a funded project
        if line in funding_lookup:
            capital_design_projects.add(line)

# Convert to final result
result = json.dumps({
    'count': len(capital_design_projects),
    'projects': sorted(list(capital_design_projects))
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)

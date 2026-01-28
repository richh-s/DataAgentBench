code = """import json
import re

# Load datasets
funding_data = locals()['var_functions.query_db:58']
civic_file = locals()['var_functions.query_db:54']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount
    
    # Also store base name without parenthetical suffixes
    base_name = project_name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find capital projects in design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the "Capital Improvement Projects (Design)" section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    if design_section_start < 0:
        continue
    
    # Get text after this header up to a reasonable limit
    text_after_header = text[design_section_start + 100:]  # Skip the header itself
    
    # Find the end of the design section (start of next major section)
    construction_section_start = text_after_header.find('Capital Improvement Projects (Construction)')
    if construction_section_start > 0:
        design_section_text = text_after_header[:construction_section_start]
    else:
        disaster_section_start = text_after_header.find('Disaster Recovery Projects')
        if disaster_section_start > 0:
            design_section_text = text_after_header[:disaster_section_start]
        else:
            design_section_text = text_after_header[:5000]  # First 5000 chars after header
    
    # Extract lines that look like project names
    lines = design_section_text.split('\n')
    for line in lines:
        line = line.strip()
        # Skip empty lines, bullet points, and metadata
        if (not line or 
            line.startswith('(') or 
            line.startswith('•') or 
            line.startswith('◦') or 
            line.startswith('-') or
            'Updates:' in line or 
            'Project Schedule:' in line or 
            'Complete Design:' in line or
            'Page' in line or 
            'Agenda Item' in line):
            continue
        
        # Project names are typically title case and not too short or too long
        if len(line) < 10 or len(line) > 200:
            continue
        
        # Clean up the line
        project_name = line.rstrip('.,:;')
        
        # Check if this project has funding > $50,000
        if project_name in funding_lookup:
            funding_amount = funding_lookup[project_name]
            if funding_amount > 50000:
                design_projects.add(project_name)

# Return the final count
result = len(design_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)

code = """import json

# Load the funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents data
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find projects with design status from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Check if this document mentions capital projects in design phase
    if 'Capital Improvement Projects (Design)' in text:
        # Extract the section
        start_pos = text.find('Capital Improvement Projects (Design)')
        section = text[start_pos:start_pos + 3000]  # Get reasonable chunk
        
        # Look for project names (they appear as separate lines, often with 'Project' in name)
        for line in section.split('\n'):
            clean_line = line.strip()
            # Filter for likely project names
            if (len(clean_line) > 10 and 
                'Project' in clean_line and 
                'fema' not in clean_line.lower() and
                'disaster' not in clean_line.lower()):
                design_projects.add(clean_line)

# Filter funding for amounts > 50000 and match with design projects
matched_projects = set()

for funding_record in funding_data:
    amount = int(funding_record['Amount'])
    if amount > 50000:
        project_name = funding_record['Project_Name']
        # Remove suffixes like (FEMA Project), (CalOES Project), etc.
        base_name = project_name.split('(')[0].strip()
        
        if base_name in design_projects:
            matched_projects.add(base_name)

# Create final result
result = {'count': len(matched_projects)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

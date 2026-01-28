code = """import json
import re

# Get the stored variables using locals()
funding_data = locals()['var_functions.query_db:5']
civic_docs_data = locals()['var_functions.query_db:8']

# Check data structures
print('FUNDING DATA')
print('count:', len(funding_data))
print('type:', type(funding_data))
print('samples:')
for i in range(min(3, len(funding_data))):
    record = funding_data[i]
    print('  ', record['Project_Name'], ': $', record['Amount'])

print('\nCIVIC DOCS')  
print('count:', len(civic_docs_data))
first_doc = civic_docs_data[0]
print('keys:', list(first_doc.keys()))

sample_text = first_doc['text']
print('text length:', len(sample_text))
print('first 200 chars:')
print(sample_text[:200])

# Now let's extract project information from the text
# Based on the sample, projects are listed with their status

def extract_projects_from_text(text):
    projects = []
    
    # Look for patterns like: Project Name (status)
    # or sections marked as "Capital Improvement Projects (Design)"
    
    # Find design projects section
    design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(|Disaster Recovery Projects \(|\Z)'
    design_match = re.search(design_pattern, text, re.DOTALL)
    
    if design_match:
        design_section = design_match.group(1)
        # Extract project names - look for lines that start with project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project names that are capitalized and not status indicators
            if line and not line.startswith('(') and not line.startswith('cid:') and len(line) > 10:
                # Remove common status markers
                clean_line = re.sub(r'\(.*\)', '', line).strip()
                if clean_line and not clean_line.endswith(':'):
                    projects.append({
                        'Project_Name': clean_line,
                        'status': 'design',
                        'type': 'capital'
                    })
    
    return projects

# Test extraction
print('\n\nEXTRACTION TEST')
if civic_docs_data:
    test_projects = extract_projects_from_text(civic_docs_data[0]['text'])
    print('Extracted', len(test_projects), 'projects')
    for p in test_projects[:10]:
        print('  -', p['Project_Name'])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

code = """import json
import re

# Load the data files
funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:2']

with open(funding_path) as f:
    funding_data = json.load(f)
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# Get high funding projects (> $50,000)
high_funding = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

# Extract design capital projects from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section (between Design and Construction headers)
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    
    if design_start != -1:
        if construction_start != -1:
            design_section = text[design_start:construction_start]
        else:
            design_section = text[design_start:]
        
        # Extract project names from lines
        lines = design_section.split('\n')
        for line in lines[1:]:  # Skip the header
            line = line.strip()
            if line and len(line) > 15 and line[0] not in ['(', '-', '•']:
                if 'Updates:' not in line and 'Schedule:' not in line:
                    clean = re.sub(r'^(cid:\d+)\s*', '', line)
                    if clean and len(clean) > 15:
                        design_projects.add(clean)

# Find projects that are both in design AND have high funding
matches = high_funding.intersection(design_projects)

# Create result
result = {
    'high_funding_total': len(high_funding),
    'design_projects_total': len(design_projects),
    'matching_total': len(matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import re

# Load data from files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Check for completion in 2022 with park in nearby context
        if '2022' in line and ('completed' in line_lower or 'completion' in line_lower):
            # Look for park-related project name in surrounding lines
            for j in range(max(0, i-5), min(len(lines), i+5)):
                context_line = lines[j].strip()
                if context_line and 'park' in context_line.lower():
                    # Clean up the line to extract project name
                    proj_name = context_line
                    proj_name = re.sub(r'^[•◦\s]+', '', proj_name)
                    proj_name = re.sub(r'^\w\s+', '', proj_name)  # Remove leading single char+space
                    proj_name = proj_name.strip()
                    
                    if proj_name and len(proj_name) > 5 and 'project' not in proj_name.lower()[:30]:
                        park_projects.append(proj_name)
                        break

# Remove duplicates
park_projects = list(set(park_projects))

print('Found park projects completed in 2022:', len(park_projects))
for p in park_projects:
    print('-', p)

# Find funding for these projects
total_funding = 0

# Create a mapping of simplified project names for matching
def simplify_name(name):
    return re.sub(r'[^a-z]', '', name.lower())

for park in park_projects:
    park_simple = simplify_name(park)
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_simple = simplify_name(fund_name)
        
        # Check if one name contains the other (simplified)
        if park_simple in fund_simple or fund_simple in park_simple:
            amount = int(fund['Amount'])
            total_funding += amount
            print('Matched:', park, '->', fund_name, ': $', amount)
            break

print('\nTotal funding for 2022 park projects: $', total_funding)

result = {
    'total_funding_dollars': total_funding,
    'project_count': len(park_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

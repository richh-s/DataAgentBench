code = """import json
import re

# Load the data files
civic_docs_file = var_functions.query_db:2
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = var_functions.query_db:4
funding_data = []
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for fund in funding_data:
    proj_name = fund['Project_Name']
    amount = int(fund['Amount'])
    funding_lookup[proj_name] = amount

print('Data loaded successfully')
print(f'Civic docs: {len(civic_docs)}')
print(f'Funding records: {len(funding_data)}')
print(f'Funding lookup projects: {len(funding_lookup)}')

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections in the text
    # Pattern to find project names followed by schedule information
    project_blocks = re.findall(r'([A-Z][a-zA-Z\s&\-\(\)]+?(?:Project)?)\s*\n\s*\(cid:\d+\)\s*(Updates|Project Schedule|Estimated Schedule):([^\n]*(?:\n\s*\(cid:\d+\)[^\n]*)*)', text)
    
    for proj_name, section_type, content in project_blocks:
        # Clean project name
        proj_name = proj_name.strip()
        
        # Check if content contains Spring 2022
        if 'Spring 2022' in content or '2022-Spring' in content:
            spring_2022_projects.append(proj_name)
            
    # Also look for projects with start dates mentioned
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name patterns (typically capitalized, often followed by Project)
        proj_match = re.match(r'^([A-Z][a-zA-Z\s&\-\(\)]+?(?:Project)?)$', line)
        if proj_match and len(line) > 10:  # Avoid very short matches
            current_project = line
            
        # Look for Spring 2022 in schedule lines
        if current_project and ('Spring 2022' in line or '2022-Spring' in line):
            spring_2022_projects.append(current_project)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print(f'Found {len(spring_2022_projects)} Spring 2022 projects')
print('Spring 2022 projects:', spring_2022_projects[:10])  # Show first 10

# Match with funding data
total_funding = 0
matched_projects = []

for proj in spring_2022_projects:
    if proj in funding_lookup:
        matched_projects.append({
            'project_name': proj,
            'funding': funding_lookup[proj]
        })
        total_funding += funding_lookup[proj]
    else:
        # Try partial matching
        for fund_proj, amount in funding_lookup.items():
            # Check if one is substring of the other
            if (proj.lower() in fund_proj.lower() or fund_proj.lower() in proj.lower()) and abs(len(proj) - len(fund_proj)) < 20:
                matched_projects.append({
                    'project_name': proj,
                    'matched_funding_name': fund_proj,
                    'funding': amount
                })
                total_funding += amount
                break

print(f'Matched {len(matched_projects)} projects with funding')
print(f'Total funding: ${total_funding:,}')

result = {
    'spring_2022_projects_count': len(spring_2022_projects),
    'matched_with_funding': len(matched_projects),
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

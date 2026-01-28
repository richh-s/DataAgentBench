code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:54']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Create funding map (lowercase project name -> amount)
funding_map = {}
for rec in funding_records:
    proj_name = rec['Project_Name'].lower().strip()
    amount = int(rec['Amount'])
    funding_map[proj_name] = amount

print('Created funding map with', len(funding_map), 'entries')

# Load civic documents with Spring 2022 projects
civic_path = locals()['var_functions.query_db:52']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')

# Find Spring 2022 projects
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project sections with Spring 2022 construction
    # Pattern: Project name line, then schedule lines with Spring 2022
    
    # Split by double newlines to find project sections
    sections = text.split('\n\n')
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
        
        # Check if this section has Spring 2022 construction date
        if re.search(r'Begin[^\n]*(?:Spring|March|April|May)[^\n]*2022', section):
            # Extract project name (first line that's not a header/category)
            lines = section.split('\n')
            for line in lines[:5]:
                line = line.strip()
                if (line and 
                    not line.startswith('(') and 
                    'cid:' not in line and 
                    '_' not in line and
                    'Capital Improvement' not in line and
                    'Design' not in line and
                    'Construction' not in line and
                    'Not Started' not in line and
                    'Completed' not in line and
                    len(line) < 100):
                    spring_2022_projects.add(line)
                    break

print('Found Spring 2022 projects:', spring_2022_projects)
print('Count:', len(spring_2022_projects))

# Match with funding
matched_projects = []
total_funding = 0

for proj in spring_2022_projects:
    proj_key = proj.lower()
    
    # Direct match
    if proj_key in funding_map:
        amount = funding_map[proj_key]
        matched_projects.append({'name': proj, 'funding': amount})
        total_funding += amount
        continue
    
    # Try to match with FEMA/CalOES suffixes removed
    base_proj = proj_key.replace(' (fema project)', '').replace(' (caljpia project)', '').replace(' (caloes project)', '')
    if base_proj in funding_map:
        amount = funding_map[base_proj]
        matched_projects.append({'name': proj, 'funding': amount})
        total_funding += amount
        continue
    
    # Try to find partial match (project name contained in funding name)
    for fund_name, amount in funding_map.items():
        if base_proj in fund_name or fund_name in base_proj:
            matched_projects.append({'name': proj, 'funding': amount})
            total_funding += amount
            break

print('Matched with funding:', len(matched_projects))
print('Total funding:', total_funding)

# Create final result
result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)

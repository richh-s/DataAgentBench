code = """import json
import re

# Load the data
civic_docs_file = locals()['var_functions.query_db:22']
funding_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Loaded', len(civic_docs), 'documents and', len(funding_data), 'funding records')

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all project sections
    lines = text.split('\n')
    
    current_project = None
    project_topic = None
    project_status = None
    project_end_time = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name lines (usually standalone, not bullet points)
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('-') and
            not any(keyword in line for keyword in ['Updates:', 'Schedule:', 'To:', 'Prepared by:', 'Date:', 'Page', 'Agenda Item'])):
            
            # Check if it looks like a project name
            if any(indicator in line for indicator in ['Project', 'Improvements', 'Repairs', 'Replacement', 'Structure', 'Walkway', 'System']):
                current_project = line
                
                # Check if it's park-related
                if 'park' in line.lower() or 'Park' in line:
                    project_topic = 'park'
                    
                    # Look ahead for status and completion date
                    for j in range(i+1, min(i+20, len(lines))):
                        next_line = lines[j].strip()
                        
                        # Look for completion status in 2022
                        if ('2022' in next_line and 
                            ('completed' in next_line.lower() or 'completion' in next_line.lower())):
                            project_status = 'completed'
                            project_end_time = '2022'
                            
                            park_projects_2022.append({
                                'Project_Name': current_project,
                                'topic': project_topic,
                                'status': project_status,
                                'et': project_end_time
                            })
                            break

# Remove duplicates
unique_projects = {}
for p in park_projects_2022:
    name = p['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = p

park_projects_2022 = list(unique_projects.values())

print('Found', len(park_projects_2022), 'park projects completed in 2022:')
for p in park_projects_2022:
    print('-', p['Project_Name'])

# Match with funding
total_funding = 0
matched_count = 0

# Create funding lookup dictionary
funding_lookup = {}
for fund in funding_data:
    project_name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_lookup[project_name] = amount

# Match projects and sum funding
for project in park_projects_2022:
    proj_name = project['Project_Name']
    
    # Direct match
    if proj_name in funding_lookup:
        total_funding += funding_lookup[proj_name]
        matched_count += 1
        print('Matched:', proj_name, 'with funding', funding_lookup[proj_name])
        continue
    
    # Partial/fuzzy match
    matched = False
    proj_lower = proj_name.lower()
    
    for fund_name, amount in funding_lookup.items():
        fund_lower = fund_name.lower()
        
        # Check if one is contained in the other
        if proj_lower in fund_lower or fund_lower in proj_lower:
            total_funding += amount
            matched_count += 1
            print('Partial matched:', proj_name, '->', fund_name, 'with funding', amount)
            matched = True
            break
    
    if not matched:
        print('No funding found for:', proj_name)

result = {'total_funding': total_funding, 'matched_projects': matched_count, 'total_projects': len(park_projects_2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

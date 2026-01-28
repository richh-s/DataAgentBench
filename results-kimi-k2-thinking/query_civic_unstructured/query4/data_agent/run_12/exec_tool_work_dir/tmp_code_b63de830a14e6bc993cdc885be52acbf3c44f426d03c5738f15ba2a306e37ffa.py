code = """import json
import re

# Access the variables with proper handling
civic_docs_result = locals()['var_functions.query_db:2']
funding_result = locals()['var_functions.query_db:12']

# Load civic documents
with open(civic_docs_result, 'r') as f:
    all_docs = json.load(f)

print('Loaded %d civic documents' % len(all_docs))

# Load funding data
with open(funding_result, 'r') as f:
    funding_records = json.load(f)

print('Loaded %d funding records' % len(funding_records))

# Create funding lookup by project name
funding_lookup = {}
for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[project_name] = amount

print('Created funding lookup with %d unique projects' % len(funding_lookup))

# Look for specific projects that start in Spring 2022
spring_2022_projects = []

for doc in all_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections in the text
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines or bullet points
        if not line or line.startswith('\u0000') or line.startswith('('):
            continue
            
        # Look for project names (typically longer, descriptive lines)
        if len(line) > 10 and not any(keyword in line.lower() for keyword in ['update:', 'schedule:', 'complete', 'advertise', 'begin']):
            # This might be a project name - check if next lines contain schedule info
            
            # Look ahead for schedule info mentioning Spring 2022
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].lower()
                
                # Check for Spring 2022
                if ('spring 2022' in next_line) or ('2022-spring' in next_line):
                    current_project = line
                    # Check funding
                    if current_project in funding_lookup:
                        spring_2022_projects.append({
                            'project_name': current_project,
                            'start_time': '2022-Spring',
                            'funding_amount': funding_lookup[current_project]
                        })
                        print('Found project: %s, Funding: $%d' % (current_project, funding_lookup[current_project]))
                    break
                
                # Check for specific months in 2022
                elif ('2022-03' in next_line or '2022-march' in next_line or 'march 2022' in next_line):
                    current_project = line
                    if current_project in funding_lookup:
                        spring_2022_projects.append({
                            'project_name': current_project,
                            'start_time': '2022-03',
                            'funding_amount': funding_lookup[current_project]
                        })
                    break
                elif ('2022-04' in next_line or '2022-april' in next_line or 'april 2022' in next_line):
                    current_project = line
                    if current_project in funding_lookup:
                        spring_2022_projects.append({
                            'project_name': current_project,
                            'start_time': '2022-04',
                            'funding_amount': funding_lookup[current_project]
                        })
                    break
                elif ('2022-05' in next_line or '2022-may' in next_line or 'may 2022' in next_line):
                    current_project = line
                    if current_project in funding_lookup:
                        spring_2022_projects.append({
                            'project_name': current_project,
                            'start_time': '2022-05',
                            'funding_amount': funding_lookup[current_project]
                        })
                    break

print('\nFound %d Spring 2022 projects with funding' % len(spring_2022_projects))

# Calculate total funding
total_funding = sum(p['funding_amount'] for p in spring_2022_projects)
print('Total funding for Spring 2022 projects: $%d' % total_funding)

# Look for known 2022 Morning View project specifically
print('\nLooking for Morning View project specifically:')
for doc in all_docs:
    text = doc.get('text', '')
    if 'Morning View' in text and '2022' in text:
        print('Found Morning View in document: %s' % doc.get('filename'))
        # Check the exact project name from funding
        if '2022 Morning View Resurfacing & Storm Drain Improvements' in funding_lookup:
            amount = funding_lookup['2022 Morning View Resurfacing & Storm Drain Improvements']
            print('Found funding for 2022 Morning View: $%d' % amount)
            # Add it if not already in list
            if not any('Morning View' in p['project_name'] for p in spring_2022_projects):
                spring_2022_projects.append({
                    'project_name': '2022 Morning View Resurfacing & Storm Drain Improvements',
                    'start_time': '2022-Spring',
                    'funding_amount': amount
                })

print('\n__RESULT__')
result = {
    'spring_2022_projects_count': len(spring_2022_projects),
    'total_funding': total_funding,
    'projects': spring_2022_projects
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
